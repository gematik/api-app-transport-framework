---
topic: Nachrichtenaustausch
---

# {{page-title}}

Diese Seite beschreibt das grobe Konzept für den Nachrichtenaustausch.

## Komposition der Nachricht

Das MessageBundle dient als Container, der alle für den Anwendungsfall relevanten Ressourcen enthält. Ein Constraint fordert hierbei, dass alle im Bundle angegebenen Ressourcen und Referenzen auflösbar sein müssen. D.h. es dürfen keine Referenzen angegeben werden, deren Zielressource sich nicht im Bundle befindet.

### MessageHeader

Als erste Ressource muss hierbei der MessageHeader angegeben werden. Hier sind Sender und Empfänger anzugeben.
Weiterhin ist unter .eventCode der Anwendungsfall aus ServiceIdentifierCS anzugeben (bspw. "eRezept_Rezeptanforderung;Rezeptanfrage").
MessageHeader.id enthält hierbei eine eindeutige und einzigartige UUID, um eine Nachricht zu identifizieren.

MessageHeader.focus verweist auf die Ressource, die für den jeweiligen Anwendungsfall führend ist, bzw. als Trägerressource dient. Näheres dazu wird im ImplementationGuide des jeweiligen Anwendungsfalls beschrieben.

### MessageBundle

Nachdem der MessageHeader erstellt und unter Bundle.entry hinzugefügt wurde können nun auch alle für den jeweiligen Anwendungsfall relevanten Ressourcen dem Bundle hinzugefügt werden.

## Senden der Nachricht

Das fertiggestellte Bundle kann nun mit einem Übertragungsmedium der Wahl übermittelt werden. Bisher ist KIM vorgesehen. In Zukunft wird auch der Nachrichtenaustausch über TIM und möglicherweise weiteren Diensten möglich sein.

## Empfangsbestätigung

Wenn Nachrichten mit dem ATF ausgetauscht werden, muss (ab ATF Stufe 2) dem sendenden System rückgemeldet werden, ob der empfangene Auftrag technisch verarbeitet werden konnte. Hierzu wurde ein {{pagelink:Home/Datenobjekte/OperationOutcome}} modelliert, um entsprechende Auskunft darüber zu geben.

### Struktur der Empfangsbestätigung

Wie für alle Nachrichten im ATF notwendig, ist der OperationOutcome im MessageBundle mit MessageHeader anzuführen.

MessageHeader.eventCode ist hierbei "atf;Empfangsbestaetigung". Der OperationOutcome ist unter MessageHeader.focus zu referenzieren.

### Senden der Empfangsbestätigung

Nachdem eine Nachricht im System angekommen ist SOLL das System (ab ATF Stufe 2) mit einer Bestätigung antworten. Diese Bestätigung enthält die Information, ob die übermittelten FHIR-Ressourcen interpretiert werden konnten und eine weiterverarbeitung im empfangenden System möglich ist.
Das bedeutet, dass das empfangende System bei Eingang einer Nachricht die Ressourcen validieren und feststellen soll, ob alle Inhalte für die Weiterverarbeitung vorhanden sind.

Unter .issue können dem sendenden System als Antwort mehrere Einträge übermittelt werden. Enthalten alle Einträge nur issues mit OperationOutcome.issue.severity = "warning" oder "information" ist davon auszugehen, dass die Nachricht wie gewünscht verarbeitet werden kann. Das sendende System geht dann davon aus, dass die Nachricht verstanden wurde und die Übertragung erfolgreich war.

Sobald ein OperationOutcome.issue.sverity = "error" oder "fatal" enthält, ist davon auszugehen, dass der Vorgang abgebrochen wurde und die Anfrage nicht erfolgreich war.

## Darstellung des Nachrichtenaustausches

Hier beispielhaft ein Nachrichtenaustausch im Anwendungsfall ["E-Rezept Rezeptanforderung"](https://simplifier.net/erezept-servicerequest)

{{render:src/fhir/guides/ig-atf/images/Nachrichtenaustausch.png}}

## Fehlerhandling

Im MessageHeader ist unter .source anzugeben welche Software den Request abgesetzt hat. Falls die ankommenden Daten nicht validiert oder verarbeitet werden können, soll es hier die Möglichkeit geben mindestens eine E-Mail anzugeben. So kann im Fehlerfall möglichst automatisiert ein Fehlerbericht an das sendende System übermittelt werden. Der Nutzer SOLL dann auch benachrichtigt werden, dass es zu einem Fehler kam und der Hersteller entsprechend informiert wurde.
