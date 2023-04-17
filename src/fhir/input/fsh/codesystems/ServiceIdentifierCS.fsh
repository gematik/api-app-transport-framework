CodeSystem: ServiceIdentifierCS
Id: service-identifier-cs
Title: "Anwendungskennzeichen (CS)"
Description: "CodeSystem zum Anwendungskennzeichen zur Identifkation des UseCases, für welchen die FHIR-Instanzen verwendet werden"
* insert MetaCodeSystem(service-identifier-cs)
* #eRezept_Rezeptanforderung;Rezeptanfrage "Anfrage an einen Arzt ein Rezept auszustellen" // Empfänger schickt das Rezept zurück
* #eRezept_Rezeptanforderung;Rezeptanfrage_Storno "Abbruch der Rezeptanfrage"
* #eRezept_Rezeptanforderung;Rezeptbestaetigung "Bestätigung und Übermittlung eines ausgestellten Rezeptes"
* #eRezept_Rezeptanforderung;Abgabeanfrage "Anfrage zur Erfüllung eines Rezeptes und Abgabe des Medikaments"
* #eRezept_Rezeptanforderung;Abgabeanfrage_Storno "Abbruch der Rezeptanfrage"
* #eRezept_Rezeptanforderung;Abgabebestaetigung "Bestätigung der Erfüllung und Abgabe eines Medikamentes"
* #eRezept_ParenteraleZubereitung;Rezeptanfrage "Rezeptanfrage für eine parenterale Zubereitung"
* #eRezept_ParenteraleZubereitung;Rezeptanfrage_Storno "Abbruch der Rezeptanfrage für eine parenterale Zubereitung"
* #eRezept_ParenteraleZubereitung;Rezeptbestaetigung "Bestätigung und Übermittlung eines ausgestellten Rezeptes für eine parenterale Zubereitung"
* #eEB;Anfrage "Anfragedaten zum Erhalt von Versichertendaten"
* #eEB;Bescheinigung "Versichertendaten in verschiedenen Ausprägungen"
* #eEB;Fehler "Fehlermeldung bzgl. der Ermittlung der Daten des Versicherten"