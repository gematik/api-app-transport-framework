CodeSystem: ProcessResultCS
Id: process-result-cs
Title: "Verarbeitungsergebniskennzeichen (CS)"
Description: "CodeSystem, das das Ergebnis der Verarbeitung von FHIR-Ressourcen klassifiziert"
* insert MetaCodeSystem(process-result-cs)
* ^caseSensitive = true
* #Success "FHIR Ressourcen konnten erfolgreich verarbeitet werden" // Empfänger schickt das Rezept zurück
* #Failure;Instance_invalid "Mindestens eine FHIR Ressource konnte nicht fehlerfrei verarbeitet werden." // Empfänger schickt das Rezept zurück
* #Failure;Instance_missing "Mindestens eine für den Anwendungsfall notwendige FHIR Ressource konnte nicht identifiziert werden." // Empfänger schickt das Rezept zurück
