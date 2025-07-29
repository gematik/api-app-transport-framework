## App Transport Framework

Die gematik legt mit dem **App-Transport-Framework (ATF)** einen wichtigen Grundstein für den strukturierten und standardisierten Datenaustausch medizinischer Informationen im deutschen Gesundheitswesen. 

Das ATF zielt darauf ab, die Effizienz der Kommunikation zu steigern, indem es klare Standards für den Austausch von Nachrichten über etablierte Dienste wie **KIM** und **TIM** bereitstellt. Die vorgestellten Profile dienen als flexible Grundlage für eine Vielzahl von Anwendungsfällen, in denen medizinische Daten sicher und zuverlässig übermittelt werden.

Für eine Einführung in das Konzept des ATF und den strukturierten Datenaustausch finden Sie weitere Informationen in der [Einführung](./einfuehrung.html). Das detaillierte Konzept für den Nachrichtenaustausch, einschließlich des Handshake-Mechanismus, wird unter [Nachrichtenaustausch](./handshake.html) erläutert.

Diese Spezifikation unterstützt den Aufbau einer interoperablen und teilautomatisierten Kommunikationsinfrastruktur im Gesundheitswesen und ermöglicht eine effizientere Zusammenarbeit zwischen verschiedenen Akteuren.

### Hauptmerkmale

- **Offenes Framework**: Das ATF ist nicht auf bestimmte Anwendungsfälle beschränkt und kann flexibel in verschiedenen Bereichen eingesetzt werden.
- **FHIR-basierte Kommunikation**: Nutzt FHIR-Standards für strukturierte und standardisierte Kommunikation zwischen medizinischen Systemen.
- **Dezentral und skalierbar**: Unterstützt sowohl zentrale als auch dezentrale Kommunikation und ist damit anpassungsfähig für verschiedene medizinische Umgebungen wie Krankenhäuser, Apotheken und Labore.
- **Integration im OSI-Schichtenmodell**: Das ATF arbeitet hauptsächlich auf der Anwendungsschicht (Layer 7) des OSI-Modells und definiert, wie Nachrichten strukturiert und verarbeitet werden.
- **Teilautomatisierung**: Entwickelt, um eine teilweise Automatisierung des Nachrichtenaustauschs zu ermöglichen, wodurch der manuelle Aufwand reduziert und die Effizienz gesteigert wird.

## Weitere Informationen
Für detailliertere Informationen zum ATF siehe folgende Präsentationen:

- [Kurze Präsentation](https://gematik.github.io/api-app-transport-framework/slides/atf-presentation/ATF_Presentation_Short.html)
- [Detaillierte Präsentation](https://gematik.github.io/api-app-transport-framework/slides/atf-presentation/ATF_Presentation_Detail.html)


### Abhängigkeiten

{% include dependency-table.xhtml %}

### Kontakt und Feedback

Für Fragen und Feedback wenden Sie sich bitte an [erp-umsetzung@gematik.de](mailto:erp-umsetzung@gematik.de) oder nutzen Sie das [GitHub-Repository](https://github.com/gematik/app-transport-framework/issues).

### Rechtliche Hinweise

Dieser Implementation Guide wurde von der [gematik GmbH](https://www.gematik.de/) erstellt und veröffentlicht.

Copyright © 2025 gematik GmbH

HL7®, HEALTH LEVEL SEVEN®, FHIR® und das FHIR®-Logo sind Marken von Health Level Seven International, eingetragen beim United States Patent and Trademark Office.
