## {{page-title}}

Um sicherzustellen, dass die Nachricht verarbeitet werden kann wird über das ATF eine OperationOutcome übermittelt. Diese enthält die information, ob die Verarbeitung der Nachricht erfolgreich war (.issue.code = #informational), oder ob die Anfrage aufgrund von Verarbeitungs- (.issue.code = #processing) oder strukturellen Fehlern (.issue.code = #invalid) nicht bearbeitet werden kann.