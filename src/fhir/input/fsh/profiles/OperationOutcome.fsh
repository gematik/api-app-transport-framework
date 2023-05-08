Profile: ATFOperationOutcome
Parent: OperationOutcome
Id: atf-operation-outcome
Title: "ATF Operation Outcome"
Description: "Antwort auf eine eingegangene ATF Anfrage"
* extension contains ATFMessageIDEX named MessageID 1..1 MS

* issue MS
  * code MS
    * ^short = "Art der Antwort"
    * ^definition = "Gibt an, ob bei der Bearbeitung der Anfrage Fehler aufgetreten sind, oder die Anfrage erfolgreich bearbeitet wurde.
    Wenn die Bearbeitung erfolgreich war, wird der code #informational gesetzt und eine entsprechende Beschreibung unter .diagnostics hinzugefügt."
  * diagnostics 1..1 MS
    * ^short = "Zusatzinformationen"
    * ^definition = "Hier sind menschenlesbar Informationen zur Bearbeitung der Anfrage einzutragen."

Extension: ATFMessageIDEX
Id: atf-message-id-ex
Title: "ATF Message ID EX"
Description: "Extension zur Darstellung einer MessageID in "
* insert Meta (atf-message-id-ex)
* value[x] only string
  * ^short = "Angabe der ID der Nachricht, auf die sich dieser OperationOutcome bezieht"