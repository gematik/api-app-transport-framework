Instance: ExampleSuccessfulOperationOutcome
InstanceOf: ATFOperationOutcome
Usage: #example
Title: "Example Successful Operation Outcome"
Description: "Beipsiel einer erfolgreichen Antwort"
* extension[MessageID].valueString = "6f1882f6-22ff-4036-8f79-09a6cc14621d"
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
* extension[MessageID].valueString = "da669fc6-b9f9-4ced-8f31-95fe35564601"
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
* extension[MessageID].valueString = "8573faac-abf6-4021-be80-750c8619ec06"
* issue[+]
  * severity = #fatal
  * code = #invalid
  * diagnostics = "Ressourcen konnten nicht validiert werden"