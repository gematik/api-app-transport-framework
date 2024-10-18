Instance: ExampleBundleMessageContainer
InstanceOf: BundleAppTransportFramework
Usage: #example
Title: "Example Selbsttest"
Description: "Request sent to a patient to confirm the completion of a self-test"
* identifier.value = "urn:uuid:86a87254-ce15-11ed-afa1-0242ac120002"
* timestamp.value = "2023-03-29T13:28:17.239+02:00"
* entry[MessageHeader].fullUrl = "urn:uuid:86a87254-ce15-11ed-afa1-0242ac120003"
* entry[MessageHeader].resource = ExampleMessageHeaderAppTransportFramework
* entry[1].fullUrl = "urn:uuid:86a87254-ce15-11ed-afa1-0242ac120004"
* entry[1].resource = SuccessOperationOutcome

Instance: ExampleMessageHeaderAppTransportFramework
InstanceOf: MessageHeaderAppTransportFramework
Usage: #example
Title: "Example MessageHeader"
Description: "Example MessageHeader for Empfangsbestätigung"
* eventCoding = OperationIdentifierCS#atf;Empfangsbestaetigung
* sender.identifier = ExampleTelematikIdIdentifierPractitioner
* sender.display = "Sender Example"
* destination.endpoint = "mailto:receiver@example.klaus.kim.telematik"
* destination.receiver.identifier = ExampleTelematikIdIdentifierPharmacy
* destination.receiver.display = "Receiver Example"
* focus.reference = "urn:uuid:86a87254-ce15-11ed-afa1-0242ac120004"
* source.name = "TopDoc Systems"
* source.software = "TopDoc TI"
* source.version = "2.4.5"
* source.endpoint = "mailto:sender@example.peter.kim.telematik"
* source.contact
  * system = #email
  * value = "support@topdoc-systems.de"

Instance: ExampleTelematikIdIdentifierPharmacy
InstanceOf: IdentifierTelematikId
Usage: #inline
Title: "Example Identifier with TelematikID for pharmacy"
* value = "3-test-telematik-id"

Instance: ExampleTelematikIdIdentifierPractitioner
InstanceOf: IdentifierTelematikId
Usage: #inline
Title: "Example Identifier with TelematikID for practitioner"
* value = "1-test-telematik-id"

Instance: SuccessOperationOutcome
InstanceOf: OperationOutcome
Usage: #example
Title: "Success Operation Outcome"
Description: "Example for success operation outcome"
* issue
  * severity = #information
  * code = #informational
  * diagnostics = "Anfrage erfolgreich entgegengenommen"
