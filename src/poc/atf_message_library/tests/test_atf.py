import os
import unittest
from uuid import uuid4
from fhir.resources.bundle import BundleEntry
from fhir.resources.messageheader import MessageHeader
from fhir.resources.messageheader import MessageHeaderDestination, MessageHeaderSource
from fhir.resources.communication import Communication, CommunicationPayload
from fhir.resources.fhirtypes import ReferenceType, CodeableConceptType
from fhir.resources.attachment import Attachment
from fhir.resources.identifier import Identifier

from atf_message_library.atf_message_processor.ressource_creators.message_header_creator import MessageHeaderCreator
from atf_message_library.atf_message_processor.ressource_creators.operation_outcome_bundle_creator import OperationOutcomeBundleCreator


class TestAtf(unittest.TestCase):
    def setUp(self):
        self.message_sender = self.create_message_sender()
        self.message_receiver = self.create_message_receiver()
        self.destinations = [MessageHeaderDestination(endpointUrl="https://receiver.example.com/endpoint",
                                                      receiver=self.message_receiver)]

    def write_result_ressource(self, file_name: str, ressource: str):
        if not os.path.exists("generated"):
            os.makedirs("generated")
        with open(f"generated/{file_name}", "w") as file:
            file.write(ressource)
            file.close()

    def create_message_sender(self) -> ReferenceType:
        return ReferenceType(
            identifier=Identifier(
                system="http://gematik.de/fhir/sid/KIM-Adresse",
                value="example@gematik.kim.de"
            ),
            display="Sender Example"
        )

    def create_message_receiver(self) -> ReferenceType:
        return ReferenceType(
            identifier=Identifier(
                system="http://gematik.de/fhir/sid/KIM-Adresse",
                value="receiver@example.com",
            ),
            display="Receiver Example"
        )

    def test_create_message_header(self):
        source = MessageHeaderSource(
            endpointUrl="https://sender.example.com/endpoint",
        )
        focus_reference = "urn:uuid:86a87254-ce15-11ed-afa1-0242ac120004"
        use_case = "Selbsttest;Lieferung"
        message_header = MessageHeaderCreator.create_message_header(
            str(uuid4()),
            self.message_sender,
            source,
            self.destinations,
            "https://gematik.de/fhir/atf/CodeSystem/service-identifier-cs",
            use_case,
            "Diese Dienstkennung dient ausschließlich der Einrichtung des Kontos innerhalb eines PVS und des Testes, ob Nachrichten versendet und empfangen werden können. Diese Dienstkennung wird im PVS bei der normalen Abholung von Nachrichten ignoriert.",
            focus_reference)

        self.assertIsInstance(message_header, MessageHeader)
        self.assertEqual(message_header.sender, self.message_sender)
        self.assertEqual(
            message_header.destination[0].receiver, self.message_receiver)
        self.assertEqual(message_header.eventCoding.code, use_case)

    def create_communication(self, id: str, status: str, priority: str, subject_display: str, sender_display: str,
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

    def test_create_message_bundle(self):
        bundle = self.create_test_bundle()

        self.write_result_ressource(
            "Bundle-ExampleBundleMessageContainer.json",
            bundle.json(indent=True)
        )

        self.assertEqual(len(bundle.entry), 2)
        self.assertEqual(
            bundle.entry[0].resource.resource_type, "MessageHeader")
        self.assertEqual(
            bundle.entry[1].resource.resource_type, "Communication")

    def create_test_bundle(self):
        communication_id = "86a87254-ce15-11ed-afa1-0242ac120004"
        source = MessageHeaderSource(
            endpointUrl="https://sender.example.com/endpoint",
        )

        message_header = MessageHeaderCreator.create_message_header(
            str(uuid4()),
            self.message_sender,
            source,
            self.destinations,
            code_system="https://gematik.de/fhir/atf/CodeSystem/service-identifier-cs",
            use_case="Selbsttest;Lieferung",
            use_case_display="Diese Dienstkennung dient ausschließlich der Einrichtung des Kontos innerhalb eines PVS und des Testes, ob Nachrichten versendet und empfangen werden können. Diese Dienstkennung wird im PVS bei der normalen Abholung von Nachrichten ignoriert.",
            focus_reference=communication_id)

        communication = self.create_communication(
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
                fullUrl="urn:uuid:d0c5454d-bdff-4d7f-bf8b-ea498406210a",
                resource=communication
            )
        ]

        bundle = OperationOutcomeBundleCreator.create_message_bundle(
            message_header=message_header,
            resources=resources
        )

        return bundle


if __name__ == '__main__':
    unittest.main()
