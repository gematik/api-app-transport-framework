## {{page-title}}

|Im Rahmen der Veröffentlichung wird das [Semantic Versioning](https://semver.org/lang/de/) verwendet.

Die erste Ziffer X bezeichnet ein Major-Release und regelt die Gültigkeit von Releases. Die dritte Ziffer Y (Release x.0.y) bezeichnet eine technische Korrektur und versioniert kleinere Änderungen (Packages) während eines Jahres, z. B. 1.0.1.

| Datum | Version | Kommentar |
|---|---|---|
| 12.05.2023 | 1.0.0 | Initialer Release |
| 21.02.2024 | 1.0.4 | <ul><li>verpflichtende Angabe von</li><ul><li>`MessageHeader.id`</li><li>`MessageHeader.source`</li><li>`MessageHeader.source.name`</li><li>`MessageHeader.source.software`</li><li>`MessageHeader.source.version`</li><li>`MessageHeader.source.contact`</li></ul></ul><br> |
| 12.03.2024 | 1.1.0 | Änderung des MessageHeaders zur Angabe von KIM-Adresse und TelematikID in `MessageHeader.source` und `MessageHeader.destination` |
| 18.03.2024 | 1.2.0 | Öffnen der Angaben zu `MessageHeader.destination.receiver`. Damit muss sich der Sender maximal ausweisen und minimal eine Angabe zum Empfänger machen |
| 19.03.2024 | 1.3.0 | Hinzufügen von KIM und TIM-Address Identifiern |
| 29.11.2025 | 1.4.0 | Verbesserung der Readme und Beschreibung der schrittweise Einführung des ATF |
