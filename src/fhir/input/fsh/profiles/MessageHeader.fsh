Profile: MessageHeaderAppTransportFramework
Parent: MessageHeader
Id: message-header-app-transport
Title: "MessageHeader"
Description: "MessageHeader des MessageBundles"
* insert Meta(message-header-app-transport)

* event[x] from ServiceIdentifierVS (required)

* meta.profile MS

* id 1..1 MS
  * ^short = "Eindeutige ID der Nachricht, anzugeben als UUID"

* sender 1..1 MS
* sender.identifier 1..1 MS
* sender.identifier only IdentifierAddressKIM or IdentifierAddressTIM
* sender.display 0..1 MS
  * ^short = "Anzeigename der Absender Adresse"
* destination 1..* MS
* destination.receiver 1..1
* destination.receiver.identifier 1..1 MS
* destination.receiver.identifier only IdentifierAddressKIM or IdentifierAddressTIM
* destination.receiver.display 0..1 MS
  * ^short = "Anzeigename der Empfänger Adresse"
* focus 1..*

* source MS
  * ^short = "Angabe der Informationen des Absendenden Systems"
  * ^comment = "Diese Infomation ist verpflichtend"
  * name 1..1 MS
    * ^short = "Name des Softwareherstellers"
    * ^comment = "Diese Infomation ist verpflichtend, um das sendende System identifizieren zu können"
  * software 1..1 MS
    * ^short = "Name der Software"
    * ^comment = "Diese Infomation ist verpflichtend, um das sendende System identifizieren zu können"
  * version 1..1 MS
    * ^short = "Version der Software"
    * ^comment = "Diese Infomation ist verpflichtend, um das sendende System identifizieren zu können"
  * contact 1..1 MS
    * ^short = "Kontaktinformation zum Hersteller"
    * ^comment = "Es ist mindestens eine Email anzugeben, um Kontakt mit dem Hersteller herzustellen"

//TODO Für IG und Instances: Referenzpunkt display als Anzeigename
//TODO Für IG und Instances: Im source.endpoint und destination.endpoint 1..1, sollten diese als KIM Adresse genutzt werden! Diese müssten mit "mailto:" beginnen, da der Datentyp url ist.
