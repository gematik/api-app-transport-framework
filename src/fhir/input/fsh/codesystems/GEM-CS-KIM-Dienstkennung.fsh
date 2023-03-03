CodeSystem: GEM_CS_KIM_Dienstkennung
Id: GEM-CS-KIM-Dienstkennung
Title: "Kim Dienstkennung CS"
Description: "Dienstkennungen von KIM für FHIR-Nachrichten"
* insert MetaCodeSystem(GEM-CS-MEDREQ-KIM-Dienstkennung)
* #eRezept_Rezeptanforderung_Rezeptanfrage_an_Sender_zurueck "Anfrage an einen Arzt ein Rezept auszustellen und das Rezept an den Sender zurück zu schicken" // Empfänger schickt das Rezept zurück
* #eRezept_Rezeptanforderung_Rezeptanfrage_nur_Ausstellen "Anfrage an einen Arzt ein Rezept auszustellen" // Empfänger schickt das Rezept zurück
* #eRezept_Rezeptanforderung_Rezeptanfrage_weiterleiten_an_Apotheke "Anfrage an einen Arzt ein Rezept auszustellen und das Rezept an die Apotheke weiterzuleiten" // Sender schickt auch einen DispenseRequest mit, der weitergeleitet werden soll
* #eRezept_Rezeptanforderung_Rezeptanfrage_Storno "Abbruch der Rezeptanfrage"
* #eRezept_Rezeptanforderung_Rezeptbestaetigung "Bestätigung und übermittlung eines ausgestellten Rezeptes"
* #eRezept_Rezeptanforderung_Abgabeanfrage "Anfrage zur Erfüllung eines Rezeptes und Abgabe des Medikaments"
* #eRezept_Rezeptanforderung_Abgabeanfrage_Storno "Abbruch der Rezeptanfrage"
* #eRezept_Rezeptanforderung_Abgabebestaetigung "Bestätigung der Erfüllung und Abgabe eines Medikamentes"
* #eRezept_ParenteraleErnaehrung_Rezeptanfrage "Rezeptanfrage für eine parenterale Zubereitung"
* #eRezept_ParenteraleErnaehrung_Rezeptanfrage_Storno "Abbruch der Rezeptanfrage für eine parenterale Zubereitung"
* #eRezept_ParenteraleErnaehrung_Rezeptbestaetigung "Bestätigung und übermittlung eines ausgestellten Rezeptes für eine parenterale Zubereitung"
* #eRezept_Klaerfall "Klärfall im Kontext des Erezpetes"
* #eRezept_ParenteraleErnaehrung "Rezeptanforderung für Parenterale Ernährung"
* #eEB_Anfrage "Anfragedaten zum Erhalt von Versichertendaten"
* #eEB_Bescheinigung "Versichertendaten in verschiedenen Ausprägungen"
* #eEB_Fehler "Fehlermeldung bzgl. der Ermittlung der Daten des Versicherten"

//TODO CodeSystem um weitere bekannte Anwendungsfälle erweitern Zum Beispiel aus dem KIM Team