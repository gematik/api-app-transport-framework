## {{page-title}}

Im Feature Dokument zu diesem Projekt ([gemF_eRp_KIM#3](//TODO)) werden die Anwendungsfälle fachlich beschrieben. Aus den dort aufgeführten fachlichen Informationsobjekten kann hier das Mapping auf die FHIR-Ressourcen nachvollzogen werden.

### ServiceRequestPrescriptionRequest Mappings

@```

from StructureDefinition
where name = 'ServiceRequestPrescriptionRequest'
for differential.element
    select id, join mapping { Feld: map, Fachliche_Informationseinheit: identity }
    order by Fachliche_Informationseinheit

```

### MedicationRequestPrescriptionRequest Mappings

@```
from StructureDefinition
where name = 'MedicationRequestPrescriptionRequest'
for differential.element
    select id, join mapping { Feld: map, Fachliche_Informationseinheit: identity }
    order by Fachliche_Informationseinheit

```

### ServiceRequestDispenseRequest Mappings

@```

from StructureDefinition
where name = 'ServiceRequestDispenseRequest'
for differential.element
    select id, join mapping { Feld: map, Fachliche_Informationseinheit: identity }
    order by Fachliche_Informationseinheit

```
