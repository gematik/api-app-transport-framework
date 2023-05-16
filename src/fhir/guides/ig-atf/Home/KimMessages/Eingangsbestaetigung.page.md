## {page-title}

### KIM MDN (Empfangsbestätigung)

Eingangsbestätigungen sind als Antwort auf jeglichen Nachrichtentyp im Kontext der eRezept-Rezeptanforderung zu versenden.

|KIM-Header              |Inhalt                                 |verpflichtend|
|------------------------|---------------------------------------|-------------|
|X-KIM-Dienstkennung     |atf;Empfangsbestaetigung|ja|
|X-KIM-Sendersystem      |\<PS-Bezeichnung>;\<Releaseversion>   |ja|
|X-KIM-Support           |\<Support-Email-Adresse PS-Hersteller>|nein|
|Subject                 |eNachricht-Eingangsbestaetigung|ja|

Weitere Anforderungen der eNachricht-Eingangsbestätigung sind in der [Spezifikation MDN](https://partnerportal.kv-telematik.de/download/attachments/71095111/%C3%9Cbergreifende_Anforderungen_f%C3%BCr_KIM-Anwendungen_V1.0.1.pdf?version=1&modificationDate=1626757312000&api=v2) beschrieben.

#### KIM MDN (Empfangsbestätigung) Beispielnachricht

    Content-Type: multipart/report; report-type=disposition-notification; boundary="----
    =_Part_124_456146547.1541654416816"
    MIME-Version: 1.0
    Message-ID: 6f1882f6-22ff-4036-8f79-09a6cc14621d
    Date: Thu, 15 Dez 2022 11:51:21 +0100
    Subject: E-Rezept-Empfangsbestaetigung
    From: Arzt123@xyz.kim.telematik
    To: Pflegeheim@xyz.kim.telematik
    In-Reply-To:
    X-KIM-Dienstkennung: atf;Empfangsbestaetigung
    X-KIM-Sendersystem: Beipsiel-PVS-Client;V6.4.4
    ------=_Part_128_456146547.1541654416816
    Content-Type: text/plain; charset=utf-8
    Content-Transfer-Encoding: 8bit
    ggf. menschenlesbarer informativer Textteil
    ------=_Part_128_456146547.
    Content-Type: application/xml;
    name=Empfangsbestaetigung_d1fbcd96-74a9-4ec8-a4f4-1ce41fb1c90e.xml
    Content-Transfer-Encoding: base64
    Content-Disposition: attachment;
    filename=Empfangsbestaetigung_d1fbcd96-74a9-4ec8-a4f4-1ce41fb1c90e.xml
    PE9wZXJhdGlvbk91dGNvbWUgeG1sbnM9J2h0dHA6Ly9obDcub3JnL2ZoaXInPgogIDxpZCB2YWx1ZT0nRXhhbXBsZVN1Y2Nlc3NmdWxPcGVyYXRpb25PdXRjb21lJy8+CiAgPG1ldGE+CiAgICA8cHJvZmlsZSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvYXRmL1N0cnVjdHVyZURlZmluaXRpb24vYXRmLW9wZXJhdGlvbi1vdXRjb21lJy8+CiAgPC9tZXRhPgogIDxleHRlbnNpb24gdXJsPSdodHRwczovL2dlbWF0aWsuZGUvZmhpci9hdGYvU3RydWN0dXJlRGVmaW5pdGlvbi9hdGYtbWVzc2FnZS1pZC1leCc+CiAgICA8dmFsdWVTdHJpbmcgdmFsdWU9JzZmMTg4MmY2LTIyZmYtNDAzNi04Zjc5LTA5YTZjYzE0NjIxZCcvPgogIDwvZXh0ZW5zaW9uPgogIDxpc3N1ZT4KICAgIDxzZXZlcml0eSB2YWx1ZT0naW5mb3JtYXRpb24nLz4KICAgIDxjb2RlIHZhbHVlPSdpbmZvcm1hdGlvbmFsJy8+CiAgICA8ZGlhZ25vc3RpY3MgdmFsdWU9J0FuZnJhZ2UgZXJmb2xncmVpY2ggZW50Z2VnZW5nZW5vbW1lbicvPgogIDwvaXNzdWU+CiAgPGlzc3VlPgogICAgPHNldmVyaXR5IHZhbHVlPSdpbmZvcm1hdGlvbicvPgogICAgPGNvZGUgdmFsdWU9J2luZm9ybWF0aW9uYWwnLz4KICAgIDxkaWFnbm9zdGljcyB2YWx1ZT0nUmV6ZXB0YW5mcmFnZSB3dXJkZSBhbmdlbGVndCB1bmQgd2FydGV0IGF1ZiBCZXN0w6R0aWd1bmcnLz4KICA8L2lzc3VlPgo8L09wZXJhdGlvbk91dGNvbWU+
    ------=_Part_128_456146547.1541654416816--
