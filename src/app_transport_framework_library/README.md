# ATF Library

Die App-Transport-Framwork Library ist eine Python-Bibliothek zur Verarbeitung und Handhabung von App-Transport-Framwork (<https://simplifier.net/app-transport-framework>) Nachrichten im FHIR-Format. Die Bibliothek bietet eine einfache Möglichkeit, verschiedene Use-Cases und ihre zugehörigen Handler zu registrieren und zu verwalten.

## Installation

Um diese Bibliothek zu installieren, führen Sie den folgenden Befehl aus:

```
pip install app-transport-framework-library
```

## Verwendung

1. Importieren Sie die benötigten Klassen und Funktionen aus der Bibliothek:

```python
from app_transport_framework_library.atf_bundle_processor import ATF_BundleProcessor
```

2. Erstellen Sie eine Instanz des ATF_MessageProcessor und registrieren Sie die Handler für verschiedene Use-Cases:

```python
atf_processor = ATF_BundleProcessor(sender, source)

atf_processor.register_use_case_handler(
    "https://gematik.de/fhir/atf/CodeSystem/operation-identifier-cs",
    "eRezept_Rezeptanforderung;Rezeptanfrage",
    eRezept_Rezeptanforderung_RezeptanfrageHandler()
)

atf_processor.register_use_case_handler(
    "https://gematik.de/fhir/atf/CodeSystem/service-identifier-cs",
    "eRezept_Rezeptanforderung;Rezeptanfrage_Storno",
    eRezept_Rezeptanforderung_Rezeptanfrage_StornoHandler()
)

```

3. Events

Subscrieben Sie das 'message_to_send_event', um die generierten *ausgehenden Eingangsbestätigugen* zu erhalten und diese weiterzuleiten:

```python
from app_transport_framework_library.models.message_to_send import MessageToSend

def on_message_to_send_triggered(message_to_send: MessageToSend):
    # Sending message to original sender
    pass


atf_processor.message_to_send_event.subscribe(on_message_to_send_triggered)

```

Subscrieben Sie das 'received_Empfangsbestaetigung_event', um die *eingehenden Eingangsbestätigugen* des Belieferten Addressaten zu erhalten und die message_id der gesendeten Nacricht auszuwerten:

```python
from app_transport_framework_library.models.empfangsbestaetigung import Empfangsbestaetigung


def on_received_Empfangsbestaetigung(empfangsbestaetigung: Empfangsbestaetigung)
    print(f"'{receiver_address}' received Empfangsbestaetigung for '{empfangsbestaetigung.message_id}' from '{empfangsbestaetigung.sender}'")


atf_processor.received_Empfangsbestaetigung_event.subscribe(on_received_Empfangsbestaetigung)

```

Subscriben Sie das 'focus_Ressource_to_process_event', um die inhaltlichen Ressourcen den Anwenungsfalls zu erhalten und diese auswerten zu können:

```python
from app_transport_framework_library.models.bundle_focus_content import BundleFocusContent
from fhir.resources.communication import Communication

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


atf_processor.focus_Ressource_to_process_event.subscribe(on_focus_Ressource_to_process)

```

## Erweiterung

Um neue Anwendungsfälle hinzuzufügen, erstellen Sie einfach eine neue Handler-Klasse, die von der abstrakten Basisklasse 'BaseHandler' erbt und die 'handle'-Methode implementiert. Registrieren Sie dann die neue Handler-Klasse im ATF_MessageProcessor für den entsprechenden 'event_coding.system' und 'event_coding.code'.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe die LICENSE Datei für Details.
