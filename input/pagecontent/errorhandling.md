## Fehlerhandling

Im MessageHeader.source ist anzugeben, welche Software den Request initiiert hat. Es SOLL außerdem die Möglichkeit bestehen, eine E-Mail-Adresse anzugeben, über die das sendende System im Fehlerfall automatisiert benachrichtigt werden kann. So kann bei nicht validierbaren oder nicht verarbeitbaren Daten möglichst frühzeitig ein Fehlerbericht generiert und an den Hersteller übermittelt werden. Zusätzlich SOLL der Nutzer darüber informiert werden, dass ein Fehler aufgetreten ist und der Hersteller benachrichtigt wurde.

Dieses Vorgehen unterstützt insbesondere in der Entwicklungs- und Einführungsphase, da der Endnutzer einer bereits ausgelieferten Software in der Regel nicht selbst auf solche Fehler reagieren oder diese beheben kann.

Neben dem direkten Kontakt zwischen den Systemen können fehlerhafte UseCases auch öffentlich diskutiert oder gemeldet werden:
- **GitHub Discussions:** Für jeden UseCase können gezielt [Discussions im GitHub-Repository](https://github.com/gematik/spec-E-Rezept-ServiceRequest/discussions) eröffnet werden, um offene Fragen oder Fehlverhalten strukturiert zu besprechen.
- **ERP-Find Tickets:** Alternativ können Tickets im [ERP-Find-System eröffnet werden](https://service.gematik.de/secure/CreateIssue!default.jspa). Diese werden durch die gematik betreut und ggf. intern weitergeleitet oder eskaliert, um betroffene Systeme zu identifizieren und gezielt bei der Fehlerbehebung zu unterstützen.

Ziel ist es, Fehlverhalten frühzeitig zu erkennen, systematisch zu klassifizieren und Herstellern eine präzise Rückmeldung zur Korrektur zu ermöglichen.

### Behandlung von Fehlern im OperationOutcome

Für die Rückmeldung von Fehlern im Rahmen des Nachrichtenaustauschs ist das FHIR-Resource-Typ `OperationOutcome` zu verwenden. Dabei gelten folgende Vorgaben für den Umgang mit Fehlern:

- **Severity:** Bei Fehlern MUSS `OperationOutcome.issue.severity = "error"` gesetzt werden.
- **Code:** Es sind ausschließlich die Codes `"invalid"` oder `"processing"` zu verwenden.

**Bedeutung der Codes:**

- **invalid:**  
  Dieser Code signalisiert einen technischen Fehler, beispielsweise eine ungültige Struktur oder ein nicht interpretierbares Format.  
  - Das empfangende System DARF den Inhalt des Datensatzes dem Nutzer NICHT anzeigen.
  - Stattdessen MUSS der Nutzer darauf hingewiesen werden, dass ein technischer Fehler aufgetreten ist.
  - Zusätzlich SOLL eine Option angeboten werden, den Fehler automatisiert oder manuell an den Support zu melden.

<div class="gem-ig-example" data-title="OperationOutcome (XML)">
    {% fragment OperationOutcome/ExampleFailedToValidateOperationOutcome XML %}
</div>

- **processing:**  
  Dieser Code signalisiert einen fachlichen Fehler, den der Nutzer ggf. selbst beheben kann (z.B. fehlende Pflichtangaben wie Medikamentenname).
  - Im Feld `OperationOutcome.issue.diagnostics` MUSS ein menschenlesbarer Text enthalten sein, der den Fehler beschreibt.
  - Dieser Text MUSS dem Nutzer angezeigt werden.
  - Dem Nutzer SOLL die Möglichkeit gegeben werden, den Datensatz zu korrigieren und erneut zu übermitteln.

<div class="gem-ig-example" data-title="OperationOutcome (XML)">
    {% fragment OperationOutcome/ExampleFailedToProcessOperationOutcome XML %}
</div>

**Hinweis:**  
Die eindeutige Unterscheidung zwischen technischen und fachlichen Fehlern unterstützt eine zielgerichtete Fehlerbehandlung und verbessert die Nutzererfahrung. Die automatisierte Weiterleitung technischer Fehler an den Support erleichtert zudem eine schnelle Fehleranalyse und Behebung.
