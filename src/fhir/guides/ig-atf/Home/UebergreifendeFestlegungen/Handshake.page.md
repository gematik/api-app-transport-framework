---
topic: Nachrichtenaustausch
---

# {page-title}

Diese Seite beschreibt das grobe Konzept für den Nachrichtenaustausch.

## Sicherstellung der Verarbeitbarkeit

Je nach gewähltem Transportmedium kann zunächst überprüft werden, ob das empfangene System den Anwendungsfall unterstützt. Für KIM wäre das bspw. die Überprüfung des Verzeichnisdienstes (VZD), ob die [Dienstkennung](https://fachportal.gematik.de/toolkit/dienstkennung-kim-kom-le) von der empfangenen Adresse unterstützt wird. Weitere Informationen zu KIM finden sich im [Fachportal](https://fachportal.gematik.de/anwendungen/kommunikation-im-medizinwesen)
Beispielnachrichten für KIM befinden sich unter {{pagelink:Home/KimMessages}}.

Nach der Prüfung kann die Nachricht dann zusammengestellt werden.

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

Wenn Nachrichten mit dem ATF ausgetauscht werden, ist es für die Interoperabilität und Darstellung hilfreich, wenn rückgemeldet wird, ob der empfangene Auftrag technisch verarbeitet werden konnte. Hierzu wurde ein {{pagelink:Home/Datenobjekte/OperationOutcome}} modelliert, um entsprechende Auskunft darüber zu geben.

### Struktur der Empfangsbestätigung

Wie für alle Nachrichten im ATF notwendig, ist der OperationOutcome im MessageBundle mit MessageHeader anzuführen.

MessageHeader.eventCode ist hierbei "atf;Empfangsbestaetigung". Der OperationOutcome ist unter MessageHeader.focus zu referenzieren.

### Senden der Empfangsbestätigung

Dieses Bundle soll nach Überprüfung der Verarbeitbarkeit der gesendeten Ressourcen übermittelt werden.

Unter .issue können dem sendenden System als Antwort mehrere Einträge übermittelt werden. Enthalten alle Einträge nur issues mit OperationOutcome.issue.severity = "warning" oder "information" ist davon auszugehen, dass die Nachricht wie gewünscht verarbeitet werden kann.

Sobald ein OperationOutcome.issue.sverity = "error" oder "fatal" enthält, ist davon auszugehen, dass der Vorgang abgebrochen wurde und die Anfrage nicht erfolgreich war.

## Darstellung des Nachrichtenaustausches

Hier beispielhaft ein Nachrichtenaustausch im Anwendungsfall ["E-Rezept Rezeptanforderung"](https://simplifier.net/erezept-servicerequest)

{{render:guides/ig-atf/images/Nachrichtenaustausch.png}}