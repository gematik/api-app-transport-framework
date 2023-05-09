# Inhalt

- [KIM MDN (Eingangsbestätigung)](#kim-mdn-eingangsbestaetigung)
  - [KIM MDN (Eingangsbestätigung) Beispielnachricht](#kim-mdn-eingangsbestaetigung-beispielnachricht)

## KIM MDN (Eingangsbestätigung)

Eingangsbestätigungen sind als Antwort auf jeglichen Nachrichtentyp im Kontext der eRezept-Rezeptanforderung zu versenden.

|KIM-Header              |Inhalt                                 |verpflichtend|
|------------------------|---------------------------------------|-------------|
|X-KIM-Dienstkennung     |eRezept-Rezeptanforderung;Eingangsbestaetigung;V1.0|ja|
|X-KIM-Sendersystem      |\<PS-Bezeichnung>;\<Releaseversion>   |ja|
|X-KIM-Support           |\<Support-Email-Adresse PS-Hersteller>|nein|
|Subject                 |eNachricht-Eingangsbestaetigung|ja|

Weitere Anforderungen der eNachricht-Eingangsbestätigung sind in der [Spezifikation MDN](https://partnerportal.kv-telematik.de/download/attachments/71095111/%C3%9Cbergreifende_Anforderungen_f%C3%BCr_KIM-Anwendungen_V1.0.1.pdf?version=1&modificationDate=1626757312000&api=v2) beschrieben.

### KIM MDN (Eingangsbestätigung) Beispielnachricht

    Content-Type: multipart/report; report-type=disposition-notification; boundary="----
    =_Part_124_456146547.1541654416816"
    MIME-Version: 1.0
    Message-ID:
    Date: Thu, 15 Dez 2022 11:51:21 +0100
    Subject: E-Rezept-Eingangsbestaetigung
    From: Arzt123@xyz.kim.telematik
    To: Pflegeheim@xyz.kim.telematik
    In-Reply-To:
    X-KIM-Dienstkennung: E-Rezept;Eingangsbestaetigung;V1.0
    X-KIM-Sendersystem: Beipsiel-PVS-Client;V6.4.4
    ------=_Part_128_456146547.1541654416816
    Content-Type: text/plain; charset=utf-8
    Content-Transfer-Encoding: 8bit
    menschenlesbarer informativer Textteil
    ------=_Part_128_456146547.1541654416816
    content-type: message/disposition-notification
    Original-Message-ID:
    Disposition: automatic-action/MDN-sent-automatically;processed
    ------=_Part_128_456146547.1541654416816--
