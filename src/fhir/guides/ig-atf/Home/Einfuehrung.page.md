---
topic: Einfuehrung
---

# {{page-title}}

## Motivation und Hintergrund

FHIR etabliert sich zunehmend als Standard für den Austausch medizinischer Informationen im deutschen Gesundheitswesen. Parallel dazu bietet [KIM](https://www.gematik.de/anwendungen/kim) (Kommunikation im Gesundheitswesen) bereits ein sicheres Kommunikationsprotokoll für den medizinischen Datenaustausch.

Mit dieser Spezifikation wird der strukturierte Datenaustausch auf Basis von FHIR weiterentwickelt und ermöglicht die flexible Nutzung über verschiedene Austauschplattformen und -protokolle wie KIM und TIM. Ziel ist es, eine einheitliche, interoperable Lösung für den sicheren, effizienten Datenaustausch zu schaffen.

## Wie funktioniert das ATF?

Das App-Transport-Framework (ATF) ermöglicht eine strukturierte Kommunikation zwischen einem Sender und einem Empfänger, basierend auf standardisierten FHIR-Ressourcen. Die gesendete Nachricht enthält einen Betreff, der den Nachrichtentyp im jeweiligen Anwendungsfall festlegt, und einen Nachrichtentext, der bei Bedarf über XSLT generiert werden kann. Ein FHIR Bundle wird als Anhang hinzugefügt, das die eigentlichen Daten der Nachricht enthält.

Im FHIR Bundle befindet sich ein **MessageHeader**, der wichtige Informationen wie die Absenderadresse, das sendende System und den Code des Anwendungsfalls enthält. Dieser Code gibt an, um welche Art von Nachricht es sich handelt (z.B. Rezeptanforderung oder Befund). Die konkrete medizinische Information, die übertragen wird, ist in den **FHIR-Ressourcen des Anwendungsfalls** enthalten. Sollte eine maschinelle Verarbeitung nicht möglich sein, kann optional ein menschenlesbares PDF erstellt werden, das aus den FHIR-Ressourcen mithilfe eines XSLT-Stylesheets generiert wird.

Nach dem Senden der Nachricht erhält der Absender eine automatisierte **Empfangsbestätigung** vom Empfänger. Der Anhang der Antwort umfasst ein weiteres FHIR Bundle mit einem MessageHeader, der neben den üblichen Absender- und Empfängerinformationen auch die ID der ursprünglichen Nachricht enthält, die bestätigt wird.

Zusätzlich enthält die Antwort das Ergebnis der Nachrichtenauswertung. Dies gibt an, ob die Nachricht erfolgreich verarbeitet wurde oder ob ein Fehler aufgetreten ist. Bei einem Fehler wird eine detaillierte Fehlermeldung zurückgesendet, damit das Problem identifiziert und behoben werden kann.

![ATF Message Flow](src/fhir/guides/ig-atf/images/ATF-Message-Flow.png)

Durch diesen standardisierten Prozess wird sichergestellt, dass der Nachrichtenaustausch strukturiert und nachvollziehbar erfolgt. Der Sender hat stets die Sicherheit, dass die Nachricht angekommen und korrekt verarbeitet wurde, was die Effizienz und Zuverlässigkeit der Kommunikation im Gesundheitswesen deutlich verbessert.

## Technisches Konzept

Die Spezifikation basiert auf dem **"Messaging"-Konzept** von FHIR. Dabei kommen die Profile `BundleAppTransportFramework` (MessageBundle) und `MessageHeaderAppTransportFramework` (MessageHeader) zum Einsatz.

- **Bundle**: Dient als Container für den Nachrichtenaustausch und referenziert in `.entry` auf einen **MessageHeader**.
- **MessageHeader**: Enthält die Informationen zu Sender und Empfänger, vergleichbar mit einer E-Mail. Zudem wird über `.eventCoding` festgelegt, zu welchem Anwendungsfall die Nachricht gehört.

Derzeit sind **KIM** und **TIM** als primäre Austauschmedien vorgesehen, wobei eine Erweiterung auf weitere Protokolle in der Zukunft möglich ist.

Im MessageHeader verweist das Feld `.focus` auf eine oder mehrere Ressourcen, die den jeweiligen Anwendungsfall betreffen. Die genaue Definition variiert je nach Projekt, das diese Spezifikation umsetzt.

### Verwendung von MessageHeader.eventCode

Der **MessageHeader.eventCode** spielt eine zentrale Rolle bei der Verarbeitung der Nachricht im empfangenden System. Er gibt an, welcher Anwendungsfall behandelt wird und über welchen Übertragungsweg dies erfolgt. Aktuell orientieren sich die eventCodes an den KIM-Dienstkennungen, die ebenfalls in der umgebenden KIM-Nachricht zu finden sind.

Der **eventCode** definiert somit nicht nur den Anwendungsfall, sondern auch den Übertragungsweg innerhalb eines Anwendungsfalls.

## Einordnung und Abgrenzung

Diese Spezifikation definiert den übergeordneten Container (**MessageBundle**) und einen festen Bestandteil dieses Containers, den **MessageHeader**. Während spezifische Anwendungsfälle zusätzliche Einschränkungen oder Anforderungen an das Bundle und den MessageHeader haben können, bleibt das grundlegende Kommunikationsmuster unverändert.

Jede Nachricht besteht also aus einem Bundle, welches mindestens den MessageHeader und je nach Anwendungsfall weitere Ressourcen enthält.

## Stufenweise Einführung des App-Transport-Frameworks

Die Implementierung des App-Transport-Frameworks erfolgt schrittweise, um den reibungslosen Übergang und die schrittweise Optimierung der Kommunikation im medizinischen Umfeld zu gewährleisten.

### Stufe 1: Standardisierung und Zuverlässigkeit

Die erste Stufe des App-Transport-Frameworks (ATF) etabliert wichtige Grundlagen für die strukturierte und zuverlässige Kommunikation im medizinischen Bereich. Sie führt folgende wesentliche Verbesserungen ein:

- **Standardisierung und Klarheit**: Die klare **Use-Case-Definition** über das Codesystem des Anwendungsfalls sorgt für eine präzise und einheitliche Struktur beim Austausch von medizinischen Daten. Dies ermöglicht eine nahtlose Interoperabilität zwischen verschiedenen Systemen und Anwendungen, indem jeder Anwendungsfall klar definiert wird.

- **Nachvollziehbarkeit und Verantwortlichkeit**: Durch die **eindeutige Benennung des Absenders und des implementierenden Systems** wird die Transparenz im Nachrichtenaustausch erhöht. Dies schafft eine klare Identifikation aller Teilnehmer und fördert die Sicherheit sowie die Verantwortlichkeit im Kommunikationsprozess.

- **Sicherheit und Effizienz**: Die Einführung einer automatisierten **Empfangsbestätigung** gewährleistet, dass jede Nachricht korrekt empfangen und verarbeitet wurde. Der Absender erhält Rückmeldung über das Ergebnis der Verarbeitung, was die Effizienz des Kommunikationsprozesses verbessert und Fehler schnell identifiziert.

- **Fehlertoleranz**: Durch das **Fallback-Szenario mit XSLT-Stylesheets** können Nachrichten bei Bedarf als menschenlesbare PDF-Dokumente übermittelt werden, falls technische Probleme die maschinelle Verarbeitung verhindern. Dies erhöht die Ausfallsicherheit und stellt sicher, dass der Inhalt der Nachricht dennoch zugänglich bleibt.

**Zusammenfassung**: Stufe 1 legt die Grundlage für eine strukturierte, transparente und fehlertolerante Kommunikation im medizinischen Umfeld. Standardisierte Use Cases, klare Benennung der Systeme, automatisierte Empfangsbestätigungen und Fallback-Mechanismen verbessern die Sicherheit und Effizienz des Nachrichtenaustauschs erheblich.

### Outlook: Automatisierter Use Case-Abgleich

Als nächster Schritt wird das App-Transport-Framework um **Capability-Nachrichten** erweitert. Diese Nachrichten ermöglichen eine **machine-to-machine-Aushandlung** zwischen Sender und Empfänger, um zu verhandeln, welche Use Cases sie unterstützen und wie die Kommunikation ablaufen soll. Diese Erweiterung wird jedoch nur spezifiziert, wenn aus der Industrie oder von Anwendern eine klare Notwendigkeit dafür signalisiert wird. Das Framework bleibt somit anpassungsfähig und wird entsprechend den Anforderungen der Praxis erweitert.

## Implementierung des Proof of Concept

Ein [Proof of Concept](https://github.com/gematik/api-app-transport-framework/blob/main/src/poc/README.md) sowie eine [Beispielbibliothek](https://github.com/gematik/api-app-transport-framework/blob/main/src/app_transport_framework_library/README.md) demonstrieren die praktische Anwendung des App-Transport-Frameworks in Python.

Ein [Beispiel-Szenario](https://github.com/gematik/api-app-transport-framework/blob/main/src/poc/example.py), das die Übermittlung einer Selbsttest-Nachricht zeigt, verdeutlicht die Verwendung der Bibliothek in der Praxis.