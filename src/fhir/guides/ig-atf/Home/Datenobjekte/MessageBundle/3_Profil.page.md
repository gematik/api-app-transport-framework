## {{page-title}}

Die folgende FHIR Ressource stellt eine Anfrage an eine verordnende LEI dar. Enthalten sein muss eine strukturelle Angabe der angefragten Medikation.

{{tree:https://gematik.de/fhir/atf/StructureDefinition/bundle-app-transport-framework, diff}}

Folgende Felder sind entsprechend zu befüllen, bzw. können befüllt werden:

@```
from StructureDefinition
where name = 'BundleAppTransportFramework'
for differential.element
    select id, short, comment
```
