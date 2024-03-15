## {{page-title}}

In jeder Übertragung gibt es genau einen MessageHeader. Dieser hält vier wesentliche Informationen

* Adresse des Absenders
* Adresse des Empfängers
* .eventCode zur Angabe des Anwendungsfalls
* Unter .focus angegebene Ressourcen, die als Startpunkt der Auswertung angesehen werden können

Diese Informationen können in dem vorliegenden Profil angegeben werden.

Hinweis: MessageHeader.destination.receiver ist bewusst offen spezifiziert worden. Je genauer der Empfänger in der Nachricht angegeben werden kann, desto besser. Daher sollte z.B. unter `MessageHeader.destination.receiver.identifier` nach Möglichkeit die Telematik-ID des Empfängers angegeben werden. Dies ermöglicht eine genauere Zustellung im empfangenden System.