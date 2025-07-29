// General rule for to handle versions for all structure definitions
RuleSet: Versioning
* ^status = #active
* ^experimental = false
* ^publisher = "gematik GmbH"
* ^version = "1.4"
* ^date = "2025-07-29"

RuleSet: Meta (profileName)
* insert Versioning
* ^url = "https://gematik.de/fhir/atf/StructureDefinition/{profileName}"

RuleSet: MetaValueSet(profileName)
* insert Versioning
* ^url = "https://gematik.de/fhir/atf/ValueSet/{profileName}"

RuleSet: MetaCodeSystem(profileName)
* insert Versioning
* ^url = "https://gematik.de/fhir/atf/CodeSystem/{profileName}"

RuleSet: MetaInstance(profileName)
* meta.profile = "https://gematik.de/fhir/atf/StructureDefinition/{profileName}"