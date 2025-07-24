## Operation Outcome

### Motivation

Um sicherzustellen, dass die Nachricht verarbeitet werden kann wird über das ATF eine OperationOutcome übermittelt. Diese enthält die information, ob die Verarbeitung der Nachricht erfolgreich war (.issue.code = #informational), oder ob die Anfrage aufgrund von Verarbeitungs- (.issue.code = #processing) oder strukturellen Fehlern (.issue.code = #invalid) nicht bearbeitet werden kann.

### Kompatibilität

Dieses Profil basiert auf dem Profil [OperationOutcome der FHIR-Core Spezifikation (R4)](http://hl7.org/fhir/R4/operationoutcome.html).

### Profil

Die folgende FHIR Ressource stellt eine Anfrage an eine verordnende LEI dar. Enthalten sein muss eine strukturelle Angabe der angefragten Medikation.

{{tree:https://gematik.de/fhir/atf/StructureDefinition/atf-operation-outcome, diff}}

Folgende Felder sind entsprechend zu befüllen, bzw. können befüllt werden:

@```
from StructureDefinition
where name = 'ATFOperationOutcome'
for differential.element
    select id, short, comment
```

### Beispiele

Valides Beispiel einer erfolgreichen OperationOutcome:

{{json:OperationOutcome/ExampleSuccessfulOperationOutcome}}
