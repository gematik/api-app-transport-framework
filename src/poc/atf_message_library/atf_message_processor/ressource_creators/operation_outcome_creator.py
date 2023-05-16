from fhir.resources.operationoutcome import OperationOutcome, OperationOutcomeIssue
from fhir.resources.meta import Meta
from fhir.resources.extension import Extension
from uuid import uuid4


class OperationOutcomeCreator:
    def create_operation_outcome_ressource(message_id: str, issues: list[OperationOutcomeIssue]) -> OperationOutcome:
        operation_outcome = OperationOutcome(
            id=str(uuid4()),
            meta=Meta.construct(
                profile=["https://gematik.de/fhir/atf/StructureDefinition/atf-operation-outcome"]),
            extension=[
                Extension(
                    url="https://gematik.de/fhir/atf/StructureDefinition/atf-message-id-ex",
                    valueString=message_id
                )
            ],
            issue=issues
        )
        return operation_outcome
