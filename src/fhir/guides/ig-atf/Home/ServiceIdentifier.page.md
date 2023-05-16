# {{page-title}}

## Verwendung von ServiceIdentifier

Diese Spezifikation stellt die Grundlegenden Elemente bereit, um standardisiert FHIR-Nachrichten im deutschen Gesundheitswesen auszutauschen. Die jeweiligen Spezifikationen, die auf dieser aufbauen verwenden die hier aufgelisteten Codes, um unter MessageHeader.eventCode anzugeben, auf welchen Anwendungsfall sich die Nachricht bezieht.

Folgende Codes wurden bisher festgelegt:

@```
from CodeSystem
where name = 'ServiceIdentifierCS'
for concept
    select code, display
```
