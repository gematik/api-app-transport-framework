Profile: MessageHeaderAppTransportFramework
Parent: MessageHeader
Id: message-header-app-transport
Title: "MessageHeader"
Description: "MessageHeader des MessageBundles"
* insert Meta(message-header-app-transport)

* event[x] from ServiceIdentifierVS (required)

* id 1..1 MS
  * ^short = "Eindeutige ID der Nachricht, anzugeben als UUID"

// Sender
* sender 1..1 MS
* sender.identifier 1..1 MS
  * ^short = "Telematik-ID des Absenders"
* sender.identifier only $telematik-id
* sender.display 0..1 MS
  * ^short = "Anzeigename des Absenders"

// Empfänger
* destination 1..* MS
* destination.receiver 1..1
  * ^short = "Telematik-ID des Empfängers"
* destination.receiver.identifier 1..1 MS
* destination.receiver.identifier only $telematik-id
* destination.receiver.display 0..1 MS
  * ^short = "Anzeigename des Empfängers"
* destination.endpoint MS
  * ^short = "Bspw. KIM- oder TIM-Adresse des Empfängers"
  * ^comment = "Die FHIR Ressource sieht hier eine URL vor. Bspw. kann hier eine KIM-Adresse genutzt werden. Diese beginnt mit 'mailto:', da der Datentyp url ist."

* focus 1..* MS

// Quelle der Nachricht
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
    * ^short = "E-Mail Kontaktmöglichkeit zum Hersteller"
    * ^comment = "Es ist mindestens eine E-Mail anzugeben, um Kontakt mit dem Hersteller herstellen zu können"
    * system = #email (exactly)
  * endpoint MS
    * ^short = "Bspw. KIM- oder TIM-Adresse des Absenders"
    * ^comment = "Die FHIR Ressource sieht hier eine URL vor. Bspw. kann hier eine KIM-Adresse genutzt werden. Diese beginnt mit 'mailto:', da der Datentyp url ist."

//TODO Für IG und Instances: Referenzpunkt display als Anzeigename
