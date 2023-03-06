Profile: GEM_PR_KIM_MessageHeader
Parent: MessageHeader
Id: GEM-PR-KIM-MessageHeader
Title: "GEM PR KIM MessageHeader"
Description: "Basic Message Header for communication of FHIR Ressources with KIM Messages"
* ^status = #draft
* event[x] from GEM_VS_KIM_Dienstkennung (required)

* sender 1..1 MS
* sender.identifier 1..1 MS
* sender.identifier only GEM_PR_KIM_AdressIdentifier or GEM_PR_TIM_AdressIdentifier
* sender.display 0..1 MS
  * ^short = "Anzeigename der KIM Adresse"
* destination 1..* MS
* destination.receiver 1..1
* destination.receiver.identifier 1..1 MS
* destination.receiver.identifier only GEM_PR_KIM_AdressIdentifier or GEM_PR_TIM_AdressIdentifier
* destination.receiver.display 0..1 MS
  * ^short = "Anzeigename der KIM Adresse"
* focus 1..*

//TODO Für IG und Instances: Referenzpunkt display als Anzeigename
//TODO Für IG und Instances: Im source.endpoint und destination.endpoint 1..1, sollten diese als KIM Adresse genutzt werden! Diese müssten mit "mailto:" beginnen, da der Datentyp url ist.
