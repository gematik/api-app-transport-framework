## Verwendung von ServiceIdentifier

Diese Spezifikation stellt die Grundlegenden Elemente bereit, um standardisiert FHIR-Nachrichten im deutschen Gesundheitswesen auszutauschen. Das Leitparadigma für das ATF sind [FHIR-Messages](https://hl7.org/fhir/R4/messaging.html). Eine Message enthält ein Bundle mit type = `message` und einen MessageHeader. Dieser Header enthält unter `.eventCode` einen eindeutigen Code.

Jeder Nachrichtenweg in einem Anwendungsfall des ATF ist eineindeutig definiert, um darauf Businesslogik für den jeweiligen Use Case aufzubauen und die automatisierte Verarbeitung von Daten zu ermöglichen.

### Hierarchien

Das CodeSystem ist hierarchisch aufgebaut. Die erste Ebene von Codes sind unterstützte Anwendungsfälle des ATF. Die zweite Ebene sind die für einen Anwendungsfall definierten Kommunikationswege.

Folgende Codes wurden bisher festgelegt:

{% include CodeSystem-service-identifier-cs-html.xhtml %}

### Auswertung des eventCode

Der erste Schritt in der Auswertung einer ATF Nachricht, nach einer generischen XML Schemavalidierung, ist es den eventCode auszuwerten. Dieser bestimmt die Logik sowie die Elemente, welche im Datensatz vorhanden sein müssen. Diese werden als Constraints in den Projekten der Anwendungsfälle definiert.
Hierzu kann ein FHIR-Validator, wie z.B. [HAPI FHIR](https://github.com/hapifhir/org.hl7.fhir.core/releases), oder eine eigene Implementierung genutzt werden.

Wichtig ist, dass die Informationen an der richtigen Stelle im korrekten Format vorliegen, die zur Weiterverarbeitung im empfangenen System benötigt werden.
Nach der Validierung und Sicherstellung, dass alle notwendigen Informationen vorliegen kann der Datensatz zur Weiterverarbeitung der Businesslogik übergeben werden.


<div class="gem-ig-svg-container">
    {% include atf_validation.svg %}
</div>