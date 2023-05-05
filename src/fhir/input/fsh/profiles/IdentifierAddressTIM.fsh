Profile: IdentifierAddressTIM
Parent: Identifier
Id: identifier-address-tim
Title: "TIM-Adresse Identifier"
Description: "Identifier zur Angabe der TIM-Adresse"
* insert Meta (identifier-address-tim)
* system = $tim (exactly)
* system 1..1 MS
* value 1..1
  * ^example.valueString = "example@super-care.tim.telematik"


Instance: NamingSystemAddressTIM
InstanceOf: NamingSystem
Usage: #definition
Title: "TIM-Adresse NamingSystem"
Description: "NamingSystem für eine TIM-Adresse"
* name = "NamingSystemAddressTIM"
* status = #active
* kind = #identifier
* date = "2023-02-01"
* publisher = "gematik GmbH"
* contact.telecom.system = #url
* contact.telecom.value = "https://www.gematik.de/"
* responsible = "gematik GmbH"
* description = "E-Rezept Token"
* uniqueId.type = #uri
* uniqueId.value = $tim
* uniqueId.preferred = true