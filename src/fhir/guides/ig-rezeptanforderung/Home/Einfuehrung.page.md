# {{page-title}}

## Motivation und Hintergrund

Im deutschen Gesundheitswesen etabliert sich FHIR als Standard für den Austausch medizinischer Informationen. Zusätzlich existiert bereits mit [KIM](https://www.gematik.de/anwendungen/kim) (Kommunikation im Gesundheitswesen) ein Kommunikationsprotokoll, um den sicheren Austausch von medizinischen Informationen zu gewährleisten.

Diese Spezifikation soll den Austausch von strukturierten Daten basierend auf FHIR für diverse Austauschplattformen und -protokolle ermöglichen.

## Konzept

Diese Spezifikation basiert auf dem "Messaging"-Konzept von FHIR. Dafür gibt es die Profile `BundleAppTransportFramework` und `MessageHeaderAppTransportFramework`.

Das Bundle stellt hierbei den Container für den Nachrichtenaustausch bereit und referenziert in .entry auf einen MessageHeader. Dieser MessageHeader hält die Informationen von Sender und Empfänger, analog zur Kommunikation via E-Mail.

Derzeit sind KIM und TIM als Austauschmedien angedacht, was sich in Zukunft noch erweitern lässt.

Das Feld `.focus` im MessageHeader verweist dann auf eine oder mehrere Ressourcen, die im Fokus des jeweiligen Anwendungsfalls stehen. Dies variiert und wird dann von den Projekten festgelegt, die von dieser Spezifikation erben.

### Verwendung von MessageHeader.eventCode

Historisch ist MessageHeader.eventCode ein wesentlicher Bezeichner, der angibt, wie das empfangene System die Nachricht zu verarbeiten hat. Derzeit entsprechen der .eventCode den KIM-Dienstkennungen, die auch in der Umgebenden KIM-Nachricht mit angegeben werden.

Der EventCode drückt aus, welcher Anwendungsfall und welcher Übertragungsweg innerhalb eines Anwendungsfalls behandelt wird.