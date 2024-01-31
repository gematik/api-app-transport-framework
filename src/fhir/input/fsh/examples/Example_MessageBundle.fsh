Alias: $loinc = http://loinc.org

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
* entry[1].resource = ExampleCommunication

Instance: ExampleMessageHeaderAppTransportFramework
InstanceOf: MessageHeaderAppTransportFramework
Usage: #example
Title: "Example MessageHeader"
Description: "Example MessageHeader for Selbsttest"
* eventCoding = ServiceIdentifierCS#atf;Selbsttest
* source.endpoint = "https://sender.example.com/endpoint"
* sender.identifier = ExampleKimAddress
* sender.display = "Sender Example"
* destination.endpoint = "https://receiver.example.com/endpoint"
* destination.receiver.identifier.system = $kim
* destination.receiver.identifier.value = "receiver@example.klaus.kim.telematik"
* destination.receiver.display = "Receiver Example"
* focus.reference = "urn:uuid:86a87254-ce15-11ed-afa1-0242ac120004"
* source.name = "TopDoc Systems"
* source.software = "TopDoc TI"
* source.version = "2.4.5"
* source.endpoint = "https://topdoc-systems.de"
* source.contact
  * system = #email
  * value = "support@topdoc-systems.de"

Instance: ExampleCommunication
InstanceOf: Communication
Usage: #example
Title: "Example Communication for Selbsttest"
Description: "Communication to confirm the completion of a self-test"
* status = #completed
* category[0].coding[0].system = $loinc
* category[0].coding[0].code = #45012-6
* category[0].coding[0].display = "Communication regarding test results"
* priority = #routine
* subject.display = "Max Mustermann"
* sender.display = "Dr. Anna Schmidt"
* payload[0].contentAttachment.title = "Selbsttest Bestätigung"
* payload[0].contentAttachment.contentType = #text/plain
* payload[0].contentAttachment.data = "U2VsYnN0dGVzdCBhYnNjaGxpZXNzZW4uIEJpdHRlIGtsYXJlbiBTaWUgZGllIFRlc3RlcmdlYm5pc3NlIGFiLg=="
* sent = "2023-03-29T13:28:17.239+02:00"
* received = "2023-03-29T13:30:00.000+02:00"
