from typing import List, Tuple
from fhir.resources.R4B.bundle import Bundle
from fhir.resources.R4B.operationoutcome import OperationOutcome, OperationOutcomeIssue
from fhir.resources.R4B.messageheader import MessageHeader
from fhir.resources.R4B.bundle import BundleEntry

from app_transport_framework_library.base_use_case_validator import BaseUseCaseValidator
from app_transport_framework_library.models.empfangsbestaetigung import Empfangsbestaetigung


class EmpfangsbestaetigungHandler(BaseUseCaseValidator):

    def resolve_reference(self, reference_str: str, bundle: Bundle):
        for entry in bundle.entry:
            if entry.resource.id == reference_str.split('urn:uuid:')[-1]:
                return entry.resource
        return None

    def handle(self, message_header: MessageHeader, bundle: Bundle) -> Tuple[List[BundleEntry], List[OperationOutcomeIssue]]:
        self.bundleEntries = []
        self.issues = []
        message_header = self.get_ressource_by_type(bundle, MessageHeader)
        outcome = self.get_ressource_by_type(bundle, OperationOutcome)
        message_id = outcome.extension[0].valueString.split(
            'urn:uuid:')[-1]
        empfangsbestaetigung = Empfangsbestaetigung(
            message_id, True, message_header.sender.identifier.value, message_header.destination[0].receiver.identifier.value, outcome.issue[0])

        self.received_Empfangsbestaetigung_event.trigger(empfangsbestaetigung)
        return self.bundleEntries, self.issues

    def get_ressource_by_type(self, bundle: Bundle, type):
        return next((entry.resource for entry in bundle.entry if isinstance(
            entry.resource, type)), None)
