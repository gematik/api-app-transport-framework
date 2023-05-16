from typing import Tuple
from fhir.resources.messageheader import MessageHeader
from fhir.resources.bundle import Bundle
from fhir.resources.bundle import Bundle
from fhir.resources.operationoutcome import OperationOutcome, OperationOutcomeIssue
from fhir.resources.messageheader import MessageHeader
from fhir.resources.communication import Communication
from fhir.resources.bundle import BundleEntry

from atf_message_library.atf_message_processor.base_use_case_handler import BaseUseCaseHandler


class SelbsttestLieferungHandler(BaseUseCaseHandler):
    def resolve_reference(self, reference_str: str, bundle: Bundle):
        for entry in bundle.entry:
            if entry.resource.id == reference_str.split('urn:uuid:')[-1]:
                return entry.resource
        return None

    def handle(self, message_header: MessageHeader, bundle: Bundle) -> Tuple[list[BundleEntry], list[OperationOutcomeIssue]]:
        self.bundleEntries = []
        self.issues = []
        if not any([isinstance(self.resolve_reference(focus_ref.reference, Bundle.parse_raw(bundle.json())), Communication) for focus_ref in message_header.focus]):
            self.issues.append(
                OperationOutcomeIssue(
                    severity="fatal",
                    code="invalid",
                    diagnostics="Eine Communication-Ressource wurde im MessageHeader.focus nicht gefunden"
                )
            )
        else:
            self.issues.append(
                OperationOutcomeIssue(
                    severity="information",
                    code="informational",
                    diagnostics="Anfrage erfolgreich entgegengenommen"
                )
            )

            for entry in bundle.entry:
                if not isinstance(entry.resource, (MessageHeader, OperationOutcome)):
                    self.bundleEntries.append(entry.resource)

        return self.bundleEntries, self.issues
