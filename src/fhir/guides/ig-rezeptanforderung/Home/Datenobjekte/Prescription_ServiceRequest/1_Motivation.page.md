## {{page-title}}

Als zentrales Element in einer Anfrage gelten in dieser Spezifikation ServiceRequests. Diese Bündeln die Informationen für eine konkrete Anfrage an einen anderen Leistungserbringer.

Der ServiceRequestPrescriptionRequest ist eine Anfrage zum Ausstellen einer Verordnung an einen Arzt. Alle für den Arzt relevanten Informationen zum Ausstellen einer entsprechenden Verordnung sind hier aufgeführt, bzw. referenziert.

Die Identifikation als ServiceRequestPrescriptionRequest (Verordnungsanfrage) wird über .code.coding.code = #prescription-request angegeben.
