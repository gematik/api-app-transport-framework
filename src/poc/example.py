
import base64
from uuid import uuid4
from atf_message_library.atf_message_processor.atf_bundle_processor import ATF_BundleProcessor
from atf_message_library.atf_message_processor.models.bundle_focus_content import BundleFocusContent
from atf_message_library.atf_message_processor.models.empfangsbestaetigung import Empfangsbestaetigung
from atf_message_library.atf_message_processor.models.message_to_send import MessageToSend
from atf_message_library.atf_message_processor.ressource_creators.test_message_creator import CommunicationCreator, TestMessageCreator


from fhir.resources.fhirtypes import ReferenceType
from fhir.resources.identifier import Identifier
from fhir.resources.messageheader import MessageHeaderSource
from fhir.resources.communication import Communication, CommunicationPayload

from example_helper.communication_mock import Communicator

sender_address = "client1@gematik.kim.de"
sender = ReferenceType(
    identifier=Identifier(
        system="http://gematik.de/fhir/sid/KIM-Adresse",
        value=sender_address
    ),
    display="Sender"
)
sender_source = MessageHeaderSource(
    endpointUrl="https://sender.example.com/endpoint",
)

receiver_address = "client2@gematik.kim.de"
receiver = ReferenceType(
    identifier=Identifier(
        system="http://gematik.de/fhir/sid/KIM-Adresse",
        value=receiver_address,
    ),
    display="Receiver"
)
receiver_source = MessageHeaderSource(
    endpointUrl="https://receiver.example.com/endpoint",
)

communicator = Communicator()
sender_processor = ATF_BundleProcessor(sender, sender_source)
receiver_processor = ATF_BundleProcessor(receiver, receiver_source)


def on_message_from_receiver_to_sender(message_to_send: MessageToSend):
    communicator.send(message_to_send.receiver,
                      message_to_send.message_type, message_to_send.operation_outcome_bundle.json(indent=4))
    sender_processor.process_bundle(message_to_send.operation_outcome_bundle)


def on_message_from_sender_to_receiver(message_to_send: MessageToSend):
    communicator.send(message_to_send.receiver,
                      message_to_send.message_type, message_to_send.operation_outcome_bundle.json(indent=4))
    receiver_processor.process_bundle(message_to_send.operation_outcome_bundle)


def on_sender_received_Empfangsbestaetigung(empfangsbestaetigung: Empfangsbestaetigung):
    print(f"'{sender_address}' received Empfangsbestaetigung for '{empfangsbestaetigung.message_id}' from '{empfangsbestaetigung.sender}'")
    print(empfangsbestaetigung.details.json(indent=4))


def on_receiver_received_Empfangsbestaetigung(empfangsbestaetigung: Empfangsbestaetigung):
    print(f"'{receiver_address}' received Empfangsbestaetigung for '{empfangsbestaetigung.message_id}' from '{empfangsbestaetigung.sender}'")
    print(empfangsbestaetigung.details.json(indent=4))


def on_focus_Ressource_to_process(bundle_content: BundleFocusContent):
    print(f"Processing Bundle with focus on '{bundle_content.code}'")
    if bundle_content.code == "Selbsttest;Lieferung":
        com_parsed = Communication.parse_raw(
            bundle_content.bundle_entries[0].json())
        decoded_message = base64.b64decode(
            com_parsed.payload[0].contentAttachment.data)

        print(f"Bundle contains {len(bundle_content.bundle_entries)} entries")
        print(
            f"Communication holds payload '{decoded_message.decode('utf-8')}'")


sender_processor.message_to_send_event.subscribe(
    on_message_from_sender_to_receiver)
sender_processor.received_Empfangsbestaetigung_event.subscribe(
    on_sender_received_Empfangsbestaetigung)
sender_processor.focus_Ressource_to_process_event.subscribe(
    on_focus_Ressource_to_process)
receiver_processor.message_to_send_event.subscribe(
    on_message_from_receiver_to_sender)
receiver_processor.received_Empfangsbestaetigung_event.subscribe(
    on_receiver_received_Empfangsbestaetigung)
receiver_processor.focus_Ressource_to_process_event.subscribe(
    on_focus_Ressource_to_process)


# Testnachricht erstellen
message_id = str(uuid4())
testbundle = TestMessageCreator.create_test_bundle(
    sender, receiver, message_id)
print(f"Sending Test-Message with message_id '{message_id}'")
# Testnachricht "senden"
communicator.send(receiver_address,
                  f"Selbsttest;Lieferung", testbundle.json(indent=4))

# Testnachricht (beim Empfänger) verarbeiten
receiver_processor.process_bundle(testbundle)
