Profile: MessageHeaderAppTransportFramework
Parent: MessageHeader
Id: message-header-app-transport
Title: "MessageHeader"
Description: "MessageHeader des MessageBundles"
* ^status = #draft
* event[x] from ServiceIdentifierVS (required)

* sender 1..1 MS
* sender.identifier 1..1 MS
* sender.identifier only IdentifierAddressKim or IdentifierAddressTim
* sender.display 0..1 MS
  * ^short = "Anzeigename der Absender Adresse"
* destination 1..* MS
* destination.receiver 1..1
* destination.receiver.identifier 1..1 MS
* destination.receiver.identifier only IdentifierAddressKim or IdentifierAddressTim
* destination.receiver.display 0..1 MS
  * ^short = "Anzeigename der Empfänger Adresse"
* focus 1..*

//TODO Für IG und Instances: Referenzpunkt display als Anzeigename
//TODO Für IG und Instances: Im source.endpoint und destination.endpoint 1..1, sollten diese als KIM Adresse genutzt werden! Diese müssten mit "mailto:" beginnen, da der Datentyp url ist.
