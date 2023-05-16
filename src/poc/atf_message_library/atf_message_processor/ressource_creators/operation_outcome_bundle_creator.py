from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.messageheader import MessageHeaderDestination, MessageHeaderSource
from fhir.resources.fhirtypes import ReferenceType
from fhir.resources.operationoutcome import OperationOutcome

from uuid import uuid4
from atf_message_library.atf_message_processor.ressource_creators.message_bundle_creator import MessageBundleCreator

from atf_message_library.atf_message_processor.ressource_creators.message_header_creator import MessageHeaderCreator


class OperationOutcomeBundleCreator:
    def create_operation_outcome_receipt_bundle(message_sender: ReferenceType,
                                                source: MessageHeaderSource,
                                                destinations: list[MessageHeaderDestination],
                                                operation_outcome: OperationOutcome) -> Bundle:

        message_header = MessageHeaderCreator.create_message_header(
            str(uuid4()),
            message_sender,
            source,
            destinations,
            code_system="https://gematik.de/fhir/atf/CodeSystem/operation-identifier-cs",
            use_case="atf;Empfangsbestaetigung",
            use_case_display="Empfangsbestätigung und Auskunft über FHIR Interpretierbarkeit der Nachricht",
            focus_reference=operation_outcome.id)

        resources = [
            BundleEntry(
                fullUrl=f"urn:uuid:{operation_outcome.id}",
                resource=operation_outcome
            )
        ]

        bundle = MessageBundleCreator.create_message_bundle(
            message_header=message_header,
            resources=resources
        )

        return bundle
