import logging
from json import JSONDecodeError
from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.messageheader import MessageHeader, MessageHeaderSource, MessageHeaderDestination
from fhir.resources.operationoutcome import OperationOutcomeIssue
from fhir.resources.fhirtypes import ReferenceType

from atf_message_library.atf_message_processor.base_use_case_handler import BaseUseCaseHandler
from atf_message_library.atf_message_processor.models.bundle_focus_content import BundleFocusContent
from atf_message_library.atf_message_processor.models.event import Event
from atf_message_library.atf_message_processor.models.message_to_send import MessageToSend
from atf_message_library.atf_message_processor.ressource_creators.operation_outcome_creator import OperationOutcomeCreator
from atf_message_library.atf_message_processor.ressource_creators.operation_outcome_bundle_creator import OperationOutcomeBundleCreator
from atf_message_library.atf_message_processor.use_cases.empfangsbestaetigung_handler import EmpfangsbestaetigungHandler
from atf_message_library.atf_message_processor.use_cases.selbsttest_lieferung_handler import SelbsttestLieferungHandler


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ATF_BundleProcessor:
    def __init__(self, sender: ReferenceType, source: MessageHeaderSource):
        self.sender = sender
        self.source = source
        self.use_case_handlers = {}
        self.message_to_send_event = Event()
        self.received_Empfangsbestaetigung_event = Event()
        self.focus_Ressource_to_process_event = Event()
        self.empfangsbestaetigungs_handler = EmpfangsbestaetigungHandler(
            self.sender, self.source)
        self.register_standard_use_case_handlers()
        self.empfangsbestaetigungs_handler.received_Empfangsbestaetigung_event.subscribe(
            self.on_empfangsbestaetigung_to_forwarded)

    def on_empfangsbestaetigung_to_forwarded(self, empfangsbestaetigung):
        self.received_Empfangsbestaetigung_event.trigger(empfangsbestaetigung)

    def register_standard_use_case_handlers(self):
        self.register_use_case_handler(
            "https://gematik.de/fhir/atf/CodeSystem/operation-identifier-cs",
            "atf;Empfangsbestaetigung",
            self.empfangsbestaetigungs_handler
        )

        self.register_use_case_handler(
            "https://gematik.de/fhir/atf/CodeSystem/service-identifier-cs",
            "Selbsttest;Lieferung",
            SelbsttestLieferungHandler(self.sender, self.source)
        )

    def register_use_case_handler(self, system: str, code: str, handler: BaseUseCaseHandler):
        self.use_case_handlers[(system, code)] = handler

    def process_bundle(self, bundle: Bundle) -> BundleFocusContent:
        parsed_bundle = self.parse_bundle(bundle)

        if parsed_bundle is None:
            return

        if not self.is_valid_atf_message(parsed_bundle):
            return

        message_header = self.get_message_header(parsed_bundle)

        if message_header is None:
            logger.error(
                "Die empfangene Nachricht ist keine gültige ATF-Nachricht. Ein MessageHeader fehlt.")
            return

        handler_key = (message_header.eventCoding.system,
                       message_header.eventCoding.code)

        if handler_key in self.use_case_handlers:
            handler = self.use_case_handlers[handler_key]
            ressources, issues = handler.handle(message_header, parsed_bundle)

            if issues:
                self.send_empfangsbestätigung(message_header, issues)

            if ressources:
                focusRessource = BundleFocusContent(
                    message_header.eventCoding.system, message_header.eventCoding.code, ressources)
                self.focus_Ressource_to_process_event.trigger(focusRessource)

        else:
            issues = self.create_unsupported_use_case_issues(
                message_header.eventCoding.code)
            self.send_empfangsbestätigung(message_header, issues)
            return

    def parse_bundle(self, bundle: Bundle):
        try:
            return Bundle.parse_raw(bundle.json())
        except JSONDecodeError:
            logger.error(
                "Die empfangene Nachricht ist keine gültige FHIR-Nachricht.")
            return None

    def is_valid_atf_message(self, parsed_bundle: Bundle):
        bundle_codesystem = parsed_bundle.meta.profile[0]
        if bundle_codesystem != "https://gematik.de/fhir/atf/StructureDefinition/bundle-app-transport-framework":
            logger.error(
                "Die empfangene Nachricht ist keine gültige ATF-Nachricht.")
            return False

        return True

    def get_message_header(self, parsed_bundle: Bundle):
        return next((entry.resource for entry in parsed_bundle.entry if isinstance(
            entry.resource, MessageHeader)), None)

    def create_unsupported_use_case_issues(self, event_code: str):
        return [
            OperationOutcomeIssue(
                severity="error",
                code="processing",
                diagnostics=f"Die empfangene Nachricht mit dem {event_code} kann nicht verarbeitet werden, da der Use-Case nicht unterstützt wird."
            )
        ]

    def send_empfangsbestätigung(self, message_header, issues):
        operation_outcome = OperationOutcomeCreator.create_operation_outcome_ressource(
            message_id=message_header.id,
            issues=issues)

        message_to_send = self.create_MessageToSend(
            message_header, operation_outcome)

        self.message_to_send_event.trigger(message_to_send)

    def create_MessageToSend(self, message_header, operation_outcome):
        destination = [MessageHeaderDestination(endpointUrl=message_header.source.endpointUrl,
                                                receiver=message_header.sender)]

        operationOutcomeBundle = OperationOutcomeBundleCreator.create_operation_outcome_receipt_bundle(
            self.sender, self.source, destination, operation_outcome)
        message_to_send = MessageToSend(
            operation_outcome_bundle=operationOutcomeBundle,
            receiver=message_header.sender.identifier.value,
            message_type="atf;Empfangsbestaetigung"
        )

        return message_to_send
