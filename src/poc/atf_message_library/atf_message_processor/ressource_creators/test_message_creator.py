from uuid import uuid4
from fhir.resources.messageheader import MessageHeaderDestination, MessageHeaderSource
from fhir.resources.bundle import BundleEntry
from fhir.resources.communication import Communication, CommunicationPayload
from fhir.resources.fhirtypes import ReferenceType, CodeableConceptType
from fhir.resources.attachment import Attachment
from .message_bundle_creator import MessageBundleCreator

from .message_header_creator import MessageHeaderCreator


class CommunicationCreator:
    def __init__(self):
        pass

    def create(id: str, status: str, priority: str, subject_display: str, sender_display: str,
               content_attachment_title: str, content_attachment_content_type: str,
               content_attachment_data: str, sent: str, received: str) -> Communication:
        communication = Communication(
            id=id,
            status=status,
            priority=priority,
            subject=ReferenceType(display=subject_display),
            sender=ReferenceType(display=sender_display),
            payload=[
                CommunicationPayload(
                    contentAttachment=Attachment(
                        title=content_attachment_title,
                        contentType=content_attachment_content_type,
                        data=content_attachment_data
                    )
                )
            ],
            sent=sent,
            received=received
        )
        category_coding = CodeableConceptType(
            system="http://loinc.org",
            code="45012-6",
            display="Communication regarding test results"
        )
        communication.category = [
            CodeableConceptType(coding=[category_coding])]
        return communication


class TestMessageCreator:
    def create_test_bundle(sender: ReferenceType,  receiver: ReferenceType, message_id: str):
        communication_id = str(uuid4())

        source = MessageHeaderSource(
            endpointUrl="https://sender.example.com/endpoint",
        )
        message_receiver = receiver
        destination = [MessageHeaderDestination(endpointUrl="https://receiver.example.com/endpoint",
                                                receiver=message_receiver)]

        message_header = MessageHeaderCreator.create_message_header(
            message_id,
            sender,
            source,
            destination,
            code_system="https://gematik.de/fhir/atf/CodeSystem/service-identifier-cs",
            use_case="Selbsttest;Lieferung",
            use_case_display="Diese Dienstkennung dient ausschließlich der Einrichtung des Kontos innerhalb eines PVS und des Testes, ob Nachrichten versendet und empfangen werden können. Diese Dienstkennung wird im PVS bei der normalen Abholung von Nachrichten ignoriert.",
            focus_reference=communication_id)

        communication = CommunicationCreator.create(
            id=communication_id,
            status="completed",
            priority="routine",
            subject_display="Max Mustermann",
            sender_display="Dr. Anna Schmidt",
            content_attachment_title="Selbsttest Bestätigung",
            content_attachment_content_type="text/plain",
            content_attachment_data="U2VsYnN0dGVzdCBhYnNjaGxpZXNzZW4uIEJpdHRlIGtsYXJlbiBTaWUgZGllIFRlc3RlcmdlYm5pc3NlIGFiLg==",
            sent="2023-03-29T13:28:17.239+02:00",
            received="2023-03-29T13:30:00.000+02:00"
        )

        resources = [
            BundleEntry(
                fullUrl=f"urn:uuid:{communication_id}",
                resource=communication
            )
        ]

        bundle = MessageBundleCreator.create_message_bundle(
            message_header=message_header,
            resources=resources
        )

        return bundle
