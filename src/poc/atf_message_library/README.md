# ATF Processor Library

Die App-Transport-Framwork  (ATF) Processor Library ist eine Python-Bibliothek zur Verarbeitung und Handhabung von App-Transport-Framwork (https://simplifier.net/app-transport-framework) Nachrichten im FHIR-Format. Die Bibliothek bietet eine einfache Möglichkeit, verschiedene Use-Cases und ihre zugehörigen Handler zu registrieren und zu verwalten.

# Installation

Um diese Bibliothek zu installieren, führen Sie den folgenden Befehl aus:

```
pip install .
```

# Verwendung

1. Importieren Sie die benötigten Klassen und Funktionen aus der Bibliothek:
```python
from atf_message_processor import ATF_MessageProcessor
from empfangsbestaetigung_handler import EmpfangsbestaetigungHandler
from selbsttest_lieferung_handler import SelbsttestLieferungHandler

```
2. Erstellen Sie eine Instanz des ATF_MessageProcessor und registrieren Sie die Handler für verschiedene Use-Cases:
```python
atf_processor = ATF_MessageProcessor(sender, source)

atf_processor.register_use_case_handler(
    "https://gematik.de/fhir/atf/CodeSystem/operation-identifier-cs",
    "atf;Empfangsbestaetigung",
    EmpfangsbestaetigungHandler()
)

atf_processor.register_use_case_handler(
    "https://gematik.de/fhir/atf/CodeSystem/service-identifier-cs",
    "Selbsttest;Lieferung",
    SelbsttestLieferungHandler()
)

```
3. Verarbeiten Sie das Bundle:

```python
operation_outcome = atf_processor.process_bundle(bundle)
```

# Erweiterung
Um neue Anwendungsfälle hinzuzufügen, erstellen Sie einfach eine neue Handler-Klasse, die von der abstrakten Basisklasse 'BaseHandler' erbt und die 'handle'-Methode implementiert. Registrieren Sie dann die neue Handler-Klasse im ATF_MessageProcessor für den entsprechenden 'event_coding.system' und 'event_coding.code'.

# Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe die LICENSE Datei für Details.