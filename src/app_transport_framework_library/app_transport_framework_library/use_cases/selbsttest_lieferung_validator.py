from typing import List, Tuple
from fhir.resources.R4B.messageheader import MessageHeader
from fhir.resources.R4B.bundle import Bundle
from fhir.resources.R4B.bundle import Bundle
from fhir.resources.R4B.operationoutcome import OperationOutcome, OperationOutcomeIssue
from fhir.resources.R4B.messageheader import MessageHeader
from fhir.resources.R4B.communication import Communication
from fhir.resources.R4B.bundle import BundleEntry
from app_transport_framework_library.base_use_case_validator import BaseUseCaseValidator

class SelbsttestLieferungValidator(BaseUseCaseValidator):
    def resolve_reference(self, reference_str: str, bundle: Bundle):
        for entry in bundle.entry:
            if entry.resource.id == reference_str.split('urn:uuid:')[-1]:
                return entry.resource
        return None

    def handle(self, message_header: MessageHeader, bundle: Bundle) -> Tuple[List[BundleEntry], List[OperationOutcomeIssue]]:
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
