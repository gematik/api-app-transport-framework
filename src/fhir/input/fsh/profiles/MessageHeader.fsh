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
  * reference 0..1 MS
    * ^short = "Ressource des Absenders der Nachricht"
    * ^comment = "Hier kann eine FHIR-Ressource referenziert werden, die den Absender der Nachricht repräsentiert. Bspw. ein Practitioner oder eine Organization."
  * identifier 0..1 MS
    * ^short = "Business Identifer des Absenders der Nachricht"
    * ^comment = "Bspw. kann hier die Telematik-ID des Absenders angegeben werden"
  * display 1..1 MS
    * ^short = "Anzeigename des Absenders der Nachricht"
    * ^comment = "Es muss mindestens ein Anzeigename angegeben werden, um den Absender der Nachricht anzeigen zu können"

// Empfänger
* destination 1..* MS
* destination ^short = "Angaben zum Empfänger der Nachricht"
* destination.receiver MS
* destination.receiver obeys app-transport-message-header-1
* destination.receiver.identifier MS
  * ^short = "Identifier des Empfängers der Nachricht"
  * ^comment = "Bspw. kann hier die Telematik-ID des Empfängers angegeben werden"
* destination.receiver.display MS
  * ^short = "Anzeigename des Empfängers der Nachricht"
* destination.endpoint MS
  * ^short = "Adresse des Empfängers der Nachricht"
  * ^comment = "Bspw. KIM- oder TIM-Adresse des Empfängers. Die FHIR Ressource sieht hier eine URL vor. Bspw. kann hier eine KIM-Adresse genutzt werden. Diese beginnt mit 'mailto:', da der Datentyp url ist."

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
    * ^short = "Adresse des Absenders der Nachricht"
    * ^comment = "Bspw. KIM- oder TIM-Adresse des Absenders. Die FHIR Ressource sieht hier eine URL vor. Bspw. kann hier eine KIM-Adresse genutzt werden. Diese beginnt mit 'mailto:', da der Datentyp url ist."

Invariant: app-transport-message-header-1
Description: "Als Empfänger muss eine Referenz, Displaywert oder Identifier angegeben werden"
Expression: "reference.exists() or display.exists() or identifier.exists()"
Severity: #error
