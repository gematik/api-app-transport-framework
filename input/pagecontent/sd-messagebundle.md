## Message Bundle

### Motivation

Dieses Profil dient der Bereitstellung eines Containers, der mindestens genau einen MessageHeader enthält. Weitere für den jeweiligen Anwendungsfall nötige Ressourcen lassen sich beliebig hinzufügen. 

### Kompatibiltät
Dieses Profil basiert auf dem Profil [Bundle der FHIR-Core Spezifikation (R4)](http://hl7.org/fhir/R4/bundle.html).

### Profil

Die folgende FHIR Ressource stellt eine Anfrage an eine verordnende LEI dar. Enthalten sein muss eine strukturelle Angabe der angefragten Medikation.

{{tree:https://gematik.de/fhir/atf/StructureDefinition/bundle-app-transport-framework, diff}}

Folgende Felder sind entsprechend zu befüllen, bzw. können befüllt werden:

@```
from StructureDefinition
where name = 'BundleAppTransportFramework'
for differential.element
    select id, short, comment
```

### Beispiele

Valides Beispiel einer Verordnungsanfrage:

{{json:ExampleBundleMessageContainer}}
