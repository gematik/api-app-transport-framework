Profile: IdentifierAddressKim
Parent: Identifier
Id: identifier-address-kim
Title: "KIM-Adresse Identifier"
Description: "Identifier zur Angabe der KIM-Adresse"
* insert Meta (identifier-address-kim)
* system = $kim (exactly)
* system 1..1 MS
* value 1..1
* value obeys KIM-adresse-validieren
  * ^example.valueString = "example@super-care.kim.telematik"

Invariant: KIM-adresse-validieren
Description: "Dies ist keine gültge KIM-Adresse"
Expression: "$this.toString().matches('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')"
Severity: #warning

Instance: NamingSystemAddressKim
InstanceOf: NamingSystem
Usage: #definition
Title: "KIM-Adresse NamingSystem"
Description: "NamingSystem für eine KIM-Address"
* name = "NamingSystemAddressKim"
* status = #active
* kind = #identifier
* date = "2023-02-01"
* publisher = "gematik GmbH"
* contact.telecom.system = #url
* contact.telecom.value = "https://www.gematik.de/"
* responsible = "gematik GmbH"
* description = "E-Rezept Token"
* uniqueId.type = #uri
* uniqueId.value = $kim
* uniqueId.preferred = true