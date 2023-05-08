Instance: ExampleSuccessfulOperationOutcome
InstanceOf: ATFOperationOutcome
Usage: #example
Title: "Example Successful Operation Outcome"
Description: "Beipsiel einer erfolgreichen Antwort"
* issue[+]
  * severity = #information
  * code = #informational
  * diagnostics = "Anfrage erfolgreich entgegengenommen"
* issue[+]
  * severity = #information
  * code = #informational
  * diagnostics = "Rezeptanfrage wurde angelegt und wartet auf Bestätigung"

Instance: ExampleFailedToProcessOperationOutcome
InstanceOf: ATFOperationOutcome
Usage: #example
Title: "Example Failed To Process Operation Outcome"
Description: "Anfrage konnte nicht bearbeitet werden"
* issue[+]
  * severity = #error
  * code = #processing
  * diagnostics = "MessageHeader verweist auf keine Ressource unter .focus"
* issue[+]
  * severity = #warning
  * code = #processing
  * diagnostics = "MessageHeader.sender konnte nicht gefunden werden"

Instance: ExampleFailedToValidateOperationOutcome
InstanceOf: ATFOperationOutcome
Usage: #example
Title: "Example Failed To Validate Operation Outcome"
Description: "FHIR Datensatz konnte nicht gelesen/ validiert werden"
* issue[+]
  * severity = #fatal
  * code = #invalid
  * diagnostics = "Ressourcen konnten nicht validiert werden"