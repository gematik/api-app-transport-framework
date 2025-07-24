## Message Header

### Motivation

In jeder Übertragung gibt es genau einen MessageHeader. Dieser hält vier wesentliche Informationen

* Adresse des Absenders
* Adresse des Empfängers
* .eventCode zur Angabe des Anwendungsfalls
* Unter .focus angegebene Ressourcen, die als Startpunkt der Auswertung angesehen werden können

Diese Informationen können in dem vorliegenden Profil angegeben werden.

Hinweis: MessageHeader.destination.receiver ist bewusst offen spezifiziert worden. Je genauer der Empfänger in der Nachricht angegeben werden kann, desto besser. Daher sollte z.B. unter `MessageHeader.destination.receiver.identifier` nach Möglichkeit die Telematik-ID des Empfängers angegeben werden. Dies ermöglicht eine genauere Zustellung im empfangenden System.

### Kompatibilität

Dieses Profil basiert auf dem Profil [MessageHeader der FHIR-Core Spezifikation (R4)](http://hl7.org/fhir/R4/messageheader.html).

### Profil

Die folgende FHIR Ressource stellt eine Anfrage an eine verordnende LEI dar. Enthalten sein muss eine strukturelle Angabe der angefragten Medikation.

{{tree:https://gematik.de/fhir/atf/StructureDefinition/message-header-app-transport, diff}}

Folgende Felder sind entsprechend zu befüllen, bzw. können befüllt werden:

@```
from StructureDefinition
where name = 'MessageHeaderAppTransportFramework'
for differential.element
    select id, short, comment
```

### Beispiele

Valides Beispiel einer Verordnungsanfrage:

{{json:MessageHeader/ExampleMessageHeaderAppTransportFramework}}
