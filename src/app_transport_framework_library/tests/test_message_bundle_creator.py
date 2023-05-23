import unittest
from fhir.resources.bundle import Bundle
from fhir.resources.messageheader import MessageHeader

from app_transport_framework_library.ressource_creators.message_bundle_creator import MessageBundleCreator
from app_transport_framework_library.ressource_creators.message_header_creator import MessageHeaderCreator




class TestAtf(unittest.TestCase):

    def test_create_message_header(self):
        sender = "example@gematik.kim.de"
        sender_display = "Sender Example"
        receiver = "receiver@example.com"
        receiver_display = "Receiver Example"
        use_case = "Selbsttest;Lieferung"

        message_header = MessageHeaderCreator.create_message_header(
            sender, sender_display, receiver, receiver_display, use_case)
        self.assertIsInstance(message_header, MessageHeader)
        self.assertEqual(message_header.sender.identifier.value, sender)
        self.assertEqual(message_header.sender.display, sender_display)
        self.assertEqual(
            message_header.destination[0].receiver.identifier.value, receiver)
        self.assertEqual(
            message_header.destination[0].receiver.display, receiver_display)
        self.assertEqual(message_header.eventCoding.code, use_case)

    def test_create_message_bundle(self):
        bundle_id = "example-bundle"
        timestamp = "2023-05-13T10:00:00Z"

        # Create a MessageHeader for the test
        message_header = MessageHeader()

        # Create a list of BundleEntry resources for the use case
        resources = [
            # Add other BundleEntry resources for the use case here
        ]

        message_bundle = MessageBundleCreator.create_message_bundle(
            bundle_id, timestamp, message_header, resources)
        self.assertIsInstance(message_bundle, Bundle)
        self.assertEqual(message_bundle.id, bundle_id)
        self.assertEqual(message_bundle.timestamp.as_json(), timestamp)
        self.assertIsInstance(message_bundle.entry[0].resource, MessageHeader)


if __name__ == '__main__':
    unittest.main()
