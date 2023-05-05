CodeSystem: ServiceIdentifierCS
Id: service-identifier-cs
Title: "Anwendungskennzeichen (CS)"
Description: "CodeSystem zum Anwendungskennzeichen zur Identifkation des UseCases, für welchen die FHIR-Instanzen verwendet werden"
* insert MetaCodeSystem(service-identifier-cs)
* ^caseSensitive = true
* #eRezept_Rezeptanforderung;Rezeptanfrage_an_Sender_zurueck "Anfrage an einen Arzt ein Rezept auszustellen und das Rezept an den Sender zurück zu schicken" // Empfänger schickt das Rezept zurück
* #eRezept_Rezeptanforderung;Rezeptanfrage_nur_Ausstellen "Anfrage an einen Arzt ein Rezept auszustellen" // Empfänger schickt das Rezept zurück
* #eRezept_Rezeptanforderung;Rezeptanfrage_weiterleiten_an_Apotheke "Anfrage an einen Arzt ein Rezept auszustellen und das Rezept an die Apotheke weiterzuleiten" // Sender schickt auch einen DispenseRequest mit, der weitergeleitet werden soll
* #eRezept_Rezeptanforderung;Rezeptanfrage_Storno "Abbruch der Rezeptanfrage"
* #eRezept_Rezeptanforderung;Rezeptbestaetigung "Bestätigung und Übermittlung eines ausgestellten Rezeptes"
* #eRezept_Rezeptanforderung;Abgabeanfrage "Anfrage zur Erfüllung eines Rezeptes und Abgabe des Medikaments"
* #eRezept_Rezeptanforderung;Abgabeanfrage_Storno "Abbruch der Rezeptanfrage"
* #eRezept_Rezeptanforderung;Abgabebestaetigung "Bestätigung der Erfüllung und Abgabe eines Medikamentes"
* #eRezept_ParenteraleErnaehrung;Rezeptanfrage "Rezeptanfrage für eine parenterale Zubereitung"
* #eRezept_ParenteraleErnaehrung;Rezeptanfrage_Storno "Abbruch der Rezeptanfrage für eine parenterale Zubereitung"
* #eRezept_ParenteraleErnaehrung;Rezeptbestaetigung "Bestätigung und Übermittlung eines ausgestellten Rezeptes für eine parenterale Zubereitung"
* #eEB;Anfrage "Anfragedaten zum Erhalt von Versichertendaten"
* #eEB;Bescheinigung "Versichertendaten in verschiedenen Ausprägungen"
* #eEB;Fehler "Fehlermeldung bzgl. der Ermittlung der Daten des Versicherten"
* #Selbsttest;Lieferung; "Diese Dienstkennung dient ausschließlich der Einrichtung des Kontos innerhalb eines PVS und des Testes, ob Nachrichten versendet und empfangen werden können. Diese Dienstkennung wird im PVS bei der normalen Abholung von Nachrichten ignoriert."