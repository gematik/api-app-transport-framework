Profile: IdentifierAddressKIM
Parent: Identifier
Id: identifier-address-kim
Title: "KIM-Adresse Identifier"
Description: "Identifier zur Angabe der KIM-Adresse"
* insert Meta (identifier-address-kim)
* system = $kim (exactly)
* system 1..1 MS
* value 1..1
  * ^example.valueString = "example@super-care.kim.telematik"

Instance: NamingSystemAddressKIM
InstanceOf: NamingSystem
Usage: #definition
Title: "KIM-Adresse NamingSystem"
Description: "NamingSystem für eine KIM-Address"
* name = "NamingSystemAddressKIM"
* status = #active
* kind = #identifier
* date = "2023-02-01"
* publisher = "gematik GmbH"
* contact.telecom.system = #url
* contact.telecom.value = "https://www.gematik.de/"
* responsible = "gematik GmbH"
* description = "Namingsystem für das Profil IdentifierAddressKIM"
* uniqueId.type = #uri
* uniqueId.value = $kim
* uniqueId.preferred = true

Instance: ExampleKimAddress
InstanceOf: IdentifierAddressKIM
Usage: #inline
Title: "ExampleKimAddress"
Description: "Beispiel KIM Adresse"
* value = "example@gematik.kim.telematik"
