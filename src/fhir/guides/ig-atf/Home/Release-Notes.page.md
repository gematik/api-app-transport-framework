## {{page-title}}

|Im Rahmen der Veröffentlichung wird das [Semantic Versioning](https://semver.org/lang/de/) verwendet.

Die erste Ziffer X bezeichnet ein Major-Release und regelt die Gültigkeit von Releases. Die dritte Ziffer Y (Release x.0.y) bezeichnet eine technische Korrektur und versioniert kleinere Änderungen (Packages) während eines Jahres, z. B. 1.0.1.

| Datum | Version | Kommentar |
|---|---|---|
|XXX| 1.0.0 | Initialer Release |
| 21.02.2024 | 1.0.4 | <ul><li>verpflichtende Angabe von</li><ul><li>`MessageHeader.id`</li><li>`MessageHeader.source`</li><li>`MessageHeader.source.name`</li><li>`MessageHeader.source.software`</li><li>`MessageHeader.source.version`</li><li>`MessageHeader.source.contact`</li></ul></ul><br> |
| 07.03.2024 | 1.1.0 | Änderung des MessageHeaders zur Angabe von KIM-Adresse und TelematikID in `MessageHeader.source` und `MessageHeader.destination` |
