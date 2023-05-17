# ATF Library

Die App-Transport-Framework (ATF) Library ist eine Python-Bibliothek zur Verarbeitung und Handhabung von ATF-Nachrichten (<https://simplifier.net/app-transport-framework>) im FHIR-Format. Die Bibliothek bietet eine einfache Möglichkeit, verschiedene Anwendungsfälle und ihre zugehörigen Handler zu registrieren und zu verwalten.

## Installation

Installieren Sie diese Bibliothek mit dem folgenden Befehl:

```
pip install app-transport-framework-library
```

## Verwendung

1. Importieren Sie die benötigten Klassen und Funktionen aus der Bibliothek:

```python
from app_transport_framework_library.atf_bundle_processor import ATF_BundleProcessor
```

2. Erstellen Sie eine Instanz des ATF_BundleProcessor und registrieren Sie die Handler für die Anwendungsfälle, die Sie erweitern möchten:

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

Abonnieren Sie das 'message_to_send_event', um die generierten ausgehenden Eingangsbestätigungen zu erhalten und weiterzuleiten:

```python
from app_transport_framework_library.models.message_to_send import MessageToSend

def on_message_to_send_triggered(message_to_send: MessageToSend):
    # Senden der Empfangsbestätigung an den ursprünglichen Absender
    pass


atf_processor.message_to_send_event.subscribe(on_message_to_send_triggered)

```

Abonnieren Sie das 'received_Empfangsbestaetigung_event', um die eingehenden Eingangsbestätigungen des belieferten Adressaten zu erhalten und die Message-ID der gesendeten Nachricht auszuwerten:

```python
from app_transport_framework_library.models.empfangsbestaetigung import Empfangsbestaetigung

def on_received_Empfangsbestaetigung(empfangsbestaetigung: Empfangsbestaetigung):
    print(f"'{receiver_address}' hat Empfangsbestätigung für '{empfangsbestaetigung.message_id}' von '{empfangsbestaetigung.sender}' erhalten")

atf_processor.received_Empfangsbestaetigung_event.subscribe(on_received_Empfangsbestaetigung)
```

Abonnieren Sie das 'focus_Ressource_to_process_event', um die inhaltlichen Ressourcen des Anwendungsfalls zu erhalten und auswerten zu können:

```python
from app_transport_framework_library.models.bundle_focus_content import BundleFocusContent
from fhir.resources.communication import Communication

def on_focus_Ressource_to_process(bundle_content: BundleFocusContent):
    from app_transport_framework_library.models.bundle_focus_content import BundleFocusContent
from fhir.resources.communication import Communication

def on_focus_Ressource_to_process(bundle_content: BundleFocusContent):
    print(f"Verarbeitung des Bundles mit Fokus auf '{bundle_content.code}'")
    if bundle_content.code == "Selbsttest;Lieferung":
        com_parsed = Communication.parse_raw(bundle_content.bundle_entries[0].json())
        decoded_message = base64.b64decode(com_parsed.payload[0].contentAttachment.data)

        print(f"Das Bundle enthält {len(bundle_content.bundle_entries)} Einträge")
        print(f"Die Kommunikation enthält die Payload '{decoded_message.decode('utf-8')}'")

atf_processor.focus_Ressource_to_process_event.subscribe(on_focus_Ressource_to_process)

```

## Beispielimplementierung

Eine Beispielimplementierung kann hier eingesehen werden:
<https://github.com/gematik/api-app-transport-framework/tree/main/src/poc>

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe die LICENSE-Datei für Details.
