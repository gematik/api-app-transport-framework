---
topic: Einfuehung
---

# {{page-title}}

## Motivation und Hintergrund

Im deutschen Gesundheitswesen etabliert sich FHIR als Standard für den Austausch medizinischer Informationen. Zusätzlich existiert bereits mit [KIM](https://www.gematik.de/anwendungen/kim) (Kommunikation im Gesundheitswesen) ein Kommunikationsprotokoll, um den sicheren Austausch von medizinischen Informationen zu gewährleisten.

Diese Spezifikation soll den Austausch von strukturierten Daten basierend auf FHIR für diverse Austauschplattformen und -protokolle ermöglichen.

## Konzept

Diese Spezifikation basiert auf dem "Messaging"-Konzept von FHIR. Dafür gibt es die Profile `BundleAppTransportFramework` (MessageBundle) und `MessageHeaderAppTransportFramework` (MessageBundle).

Das Bundle stellt hierbei den Container für den Nachrichtenaustausch bereit und referenziert in .entry auf einen MessageHeader. Dieser MessageHeader hält die Informationen von Sender und Empfänger, analog zur Kommunikation via E-Mail, sowie unter .eventCoding einen Code der angibt, zu welchem Anwendungsfall die gesendete Nachricht zuzuordnen ist.

Derzeit sind KIM und TIM als Austauschmedien angedacht, was sich in Zukunft noch erweitern lässt.

Das Feld `.focus` im MessageHeader verweist dann auf eine oder mehrere Ressourcen, die im Fokus des jeweiligen Anwendungsfalls stehen. Dies variiert und wird dann von den Projekten festgelegt, die diese Spezifikation umsetzen.

### Verwendung von MessageHeader.eventCode

Historisch ist MessageHeader.eventCode ein wesentlicher Bezeichner, der angibt, wie das empfangene System die Nachricht zu verarbeiten hat. Derzeit entsprechen der .eventCode den KIM-Dienstkennungen, die auch in der Umgebenden KIM-Nachricht mit angegeben werden.

Der EventCode drückt aus, welcher Anwendungsfall und welcher Übertragungsweg innerhalb eines Anwendungsfalls behandelt wird.

## Einordnung und Abgrenzung

Diese Spezifikation beschreibt den umgebenden Container (MessageBundle) und einen Eintrag in diesem Bundle, der immer vorhanden sein muss. Die Anwendungsfälle, die von diesem Projekt abhängen werden möglicherweise weitere Einschränkungen am Bundle und MessageHeader vornehmen, aber das Kommunikationspattern übernehmen.

Jede Nachricht besteht also aus einem Bundle, welches mindestens den MessageHeader und je nach Anwendungsfall weitere Ressourcen enthält.

{{render:src/fhir/guides/ig-atf/images/ATF-Scope.png}}

## Implementierung des Proof of Concept

Die exemplarische [Implementierung des App-Transport-Frameworks](https://github.com/gematik/api-app-transport-framework/blob/main/src/poc/README.md) und einer [Beispielbibliothek](https://github.com/gematik/api-app-transport-framework/blob/main/src/app_transport_framework_library/README.md) demonstriert die Anwendung in Python.

Eine exemplarische Verwendung dieser Bibliothek, in der Form der Übermittlung einer Selbsttest-Nachricht, ist in einem [Beispiel](https://github.com/gematik/api-app-transport-framework/blob/main/src/poc/example.py) dargestellt.
