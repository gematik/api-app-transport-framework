## {{page-title}}

In diesem Anwendungsfall löst ein Anfragender (z.B. eine Pflegeeinrichtung) den Prozess aus und stellt eine Rezeptanfrage an einen verordnenden Arzt. Der Arzt kann nun die Anfrage bearbeiten und ein E-Rezept erstellen. Mit Erstellung des E-Rezepts erhält der Verordnende die Informationen "PrescriptionID" und "AccessCode" vom E-Rezept-Fachdienst und kann somit ein E-Rezept-Token erzeugen.

Nun entscheidet sich der weitere Verlauf je nach Zustelltyp (ServiceRequest.orderDetail.code). Wenn der Code "#issue-prescription" angegeben wurde wird nur eine Bestätigung ohne den Token an den Anfragenden versendet und der Workflow endet damit.

Der Code "#return-to-requester" signalisiert, dass der E-Rezept-Token an den Anfragenden zu übermitteln ist, damit dieser dann die Belieferungsanfrage an die Apotheke starten kann.

Falls der Code "#send-to-pharmacy" angegeben ist, so ist vom PS des Verordnenden eine Belieferungsanfrage zu stellen. Hierbei wird ebenfalls eine Bestätigung ohne Token an den Anfragenden geschickt.

Eine detaillierte fachliche Beschreibung findet sich im dazugehörigen Featuredokument [gemF_eRp_KIM](https://fachportal.gematik.de/schnelleinstieg/downloadcenter/feature-dokumente).

Ein Mapping der fachlichen Informationseinheiten des Featuredokuments zu den Profilen findet sich unten.
