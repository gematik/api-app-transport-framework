Profile: BundleAppTransportFramework
Parent: Bundle
Id: bundle-app-transport-framework
Title: "MessageBundle für den Nachrichtentransport"
Description: "Bundle zum Zusammenfasssen der FHIR-Instanzen, welche in innerhalb dieses UseCases zusammengefasst werden sollen."
* ^status = #draft
* obeys resolve-references-in-bundle
* identifier 1..
* identifier.system 1..
* identifier.system = "urn:ietf:rfc:3986" (exactly)
* identifier.value 1..
* identifier.value ^short = "Eindeutige UUID"
* type = #message (exactly)
* timestamp 1..
* entry 1..
* entry ^slicing.discriminator.type = #type
* entry ^slicing.discriminator.path = "resource"
* entry ^slicing.rules = #open

* entry contains
    MessageHeader 1..1
* entry[MessageHeader].resource 1..1
* entry[MessageHeader].resource only MessageHeaderAppTransportFramework
* entry[MessageHeader].fullUrl 1..1

// Invariante zum Auflösen der Referenzen
Invariant: resolve-references-in-bundle
Description: "Alle Referenzen innerhalb eines Bundles müssen aufgelöst werden können"
//Expression: "Bundle.entry.resource.descendants().reference.where($this.startsWith('#').not()).all((%resource.entry.fullUrl.join('|') + '|').contains($this + '|'))"
Expression: "Bundle.entry.resource.descendants().reference.where($this.startsWith('#').not()).all(canResolveReference($this))"
Severity: #error