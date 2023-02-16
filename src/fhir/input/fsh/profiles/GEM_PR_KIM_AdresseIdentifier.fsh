Profile: GEM_PR_KIM_AdressIdentifier
Parent: Identifier
Id: GEM-PR-MEDREQ-KIM-Adresse
Title: "GEM PR MEDREQ KIM-Adresse"
Description: "Identifier zur Angabe der KIM-Adresse"
* insert Meta (GEM-PR-MEDREQ-KIM-Adresse)
* system = $kim (exactly)
* system 1..1 MS
* value 1..1
  * ^example.valueString = "example@super-care.kim.telematik"

Instance: GEM-NS-KIM-Adresse
InstanceOf: NamingSystem
Usage: #definition
Title: "GEM NS KIM-Adresse"
Description: "NamingSystem for Gematik KIM-Adresse"
* name = "GEM_NS_KIM-Adresse"
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

Instance: Pflegeheim-Immergrün-Identifier
InstanceOf: GEM_PR_KIM_AdressIdentifier
Usage: #inline
Title: "Pflegeheim-Immergrün-Identifier"
Description: "Beispiel Identifier für Pflegeheim Immergrün"
* value = "pflegeheim.immergrün.arzt@sana-pflegeheime.kim.telematik"

Instance: Hans-Topp-Glücklich-Identifier
InstanceOf: GEM_PR_KIM_AdressIdentifier
Usage: #inline
Title: "Hans-Topp-Glücklich-Identifier"
Description: "Beispiel Identifier für den Arzt Hans Topp Glücklich"
* value = "hans@ytopp-gluecklich.kim.telematik"

Instance: Test-Apotheke-Identifier
InstanceOf: GEM_PR_KIM_AdressIdentifier
Usage: #inline
Title: "Test-Apotheke-Identifier"
Description: "Beispiel Identifier für die ausführende Apotheke"
* value = "arbeitsplatz-1@test-apotheke.kim.telematik"