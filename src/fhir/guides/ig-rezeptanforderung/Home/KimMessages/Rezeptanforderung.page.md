## {page-title}

### KIM Rezeptanforderung

Die FHIR-Datensätze in Anfrage- und Antwortnachrichten werden ausschließlich als Anhang in der KIM Nachricht übertragen.
**siehe unten**

|KIM-Header              |Inhalt                                 |verpflichtend|
|------------------------|---------------------------------------|-------------|
|X-KIM-Dienstkennung     |eRezept_Rezeptanforderung;Rezeptanfrage|ja|
|X-KIM-Sendersystem      |\<PS-Bezeichnung>;\<Releaseversion>   |ja|
|X-KIM-Support           |\<Support-Email-Adresse PS-Hersteller>|nein|
|Subject                 |\<T/E>Rezeptanforderung\<UUID>                 |ja <br />T/E: *T*estsystem (RU) / *E*chtsystem (PU)<br />UUID: request bundle-identifier |
|Content-Type            | application/xml;<br />name="<T/E>Rezeptanforderung<UUID>.xml" |ja<br />T/E: Testsystem (RU) / Echtsystem (PU)<br />UUID: request bundle-identifier <br />
|Content-Transfer-Encoding |base64 |ja|
|Content-Disposition     |attachment; filename="<T/E>Rezeptanforderung<UUID>.xml" |ja<br />T/E: Testsystem (RU) / Echtsystem (PU)<br />UUID: request bundle-identifier|
|Content-Description     |Rezeptanforderung                               |ja|
Der Anhang enthält die Rezeptanforderung als FHIR-Ressource

### KIM Rezeptanforderung Beispielnachricht

    Date: Fri, 4 Nov 2022 13:02:59 +0100 (CET)
    From: pflegeeinrichtung@kim.telematik-test
    Reply-To: pflegeeinrichtung@kim.telematik-test
    To: praxisamplatzdersonne@kim.telematik-test
    Message-ID: <1015545854.7.1667563379499@localhost>
    Subject: Rezeptanforderung_7a1d5187-3070-4a23-a877-162bdd479b9b
    MIME-Version: 1.0
    Content-Type: multipart/mixed;
     boundary="----=_Part_6_1831919254.1667563379306"
    X-KIM-Dienstkennung: E-Rezept;Rezeptanforderung;V1.0
    X-KIM-Sendersystem: SmartPlegeTI;1.8.0

    ------=_Part_6_1831919254.1667563379306
    Content-Type: text/plain; charset=utf-8
    Content-Transfer-Encoding: 7bit

    Rezeptanforderung Rezeptanforderung_7a1d5187-3070-4a23-a877-162bdd479b9b
    ------=_Part_6_1831919254.1667563379306
    Content-Type: application/xml;
     name=Rezeptanforderung_7a1d5187-3070-4a23-a877-162bdd479b9b.xml
    Content-Transfer-Encoding: base64
    Content-Disposition: attachment;
     filename=Rezeptanforderung_7a1d5187-3070-4a23-a877-162bdd479b9b.xml
    Content-Description: eRezept_Rezeptanforderung;Rezeptanfrage
    PEJ1bmRsZSB4bWxucz0naHR0cDovL2hsNy5vcmcvZmhpcic+CiAgPGlkIHZhbHVlPSdVQzEtMS1QcmVzY3JpcHRpb24tUmVxdWVzdC1Uby1QcmVzY3JpYmVyJy8+CiAgPG1ldGE+CiAgICA8cHJvZmlsZSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL1N0cnVjdHVyZURlZmluaXRpb24vZXJwLXNlcnZpY2UtcmVxdWVzdC1tZXNzYWdlLWNvbnRhaW5lcicvPgogIDwvbWV0YT4KICA8aWRlbnRpZmllcj4KICAgIDxzeXN0ZW0gdmFsdWU9J3VybjppZXRmOnJmYzozOTg2Jy8+CiAgICA8dmFsdWUgdmFsdWU9J3Vybjp1dWlkOjI5ODg4ODg1LTY2MzktNDgxYy05MzRlLTRiN2I1MTc0NTA4NCcvPgogIDwvaWRlbnRpZmllcj4KICA8dHlwZSB2YWx1ZT0nbWVzc2FnZScvPgogIDx0aW1lc3RhbXA+CiAgICA8dmFsdWUgdmFsdWU9JzIwMTUtMDItMDdUMTM6Mjg6MTcuMjM5KzAyOjAwJy8+CiAgPC90aW1lc3RhbXA+CiAgPGVudHJ5PgogICAgPGZ1bGxVcmwgdmFsdWU9J2h0dHA6Ly9tZWRyZXEtdGVzdC5kZS9NZXNzYWdlSGVhZGVyL1VDMS1IZWFsdGhDYXJlU2VydmljZS10by1QcmFjdGl0aW9uZXItTWVzc2FnZUhlYWRlcicvPgogICAgPHJlc291cmNlPgogICAgICA8TWVzc2FnZUhlYWRlcj4KICAgICAgICA8aWQgdmFsdWU9J1VDMS1IZWFsdGhDYXJlU2VydmljZS10by1QcmFjdGl0aW9uZXItTWVzc2FnZUhlYWRlcicvPgogICAgICAgIDxtZXRhPgogICAgICAgICAgPHByb2ZpbGUgdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL2VycG1lZHJlcWNvbS9TdHJ1Y3R1cmVEZWZpbml0aW9uL2VycC1zZXJ2aWNlLXJlcXVlc3QtcmVxdWVzdC1oZWFkZXInLz4KICAgICAgICA8L21ldGE+CiAgICAgICAgPGV2ZW50Q29kaW5nPgogICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvYXRmL0NvZGVTeXN0ZW0vc2VydmljZS1pZGVudGlmaWVyLWNzJy8+CiAgICAgICAgICA8Y29kZSB2YWx1ZT0nZVJlemVwdF9SZXplcHRhbmZvcmRlcnVuZztSZXplcHRhbmZyYWdlJy8+CiAgICAgICAgPC9ldmVudENvZGluZz4KICAgICAgICA8ZGVzdGluYXRpb24+CiAgICAgICAgICA8ZW5kcG9pbnQgdmFsdWU9J2tsYXVzQHRlc3QuZGUnLz4KICAgICAgICAgIDxyZWNlaXZlcj4KICAgICAgICAgICAgPGlkZW50aWZpZXI+CiAgICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cDovL2dlbWF0aWsuZGUvZmhpci9zaWQvS0lNLUFkcmVzc2UnLz4KICAgICAgICAgICAgICA8dmFsdWUgdmFsdWU9J2hhbnNAeXRvcHAtZ2x1ZWNrbGljaC5raW0udGVsZW1hdGlrJy8+CiAgICAgICAgICAgIDwvaWRlbnRpZmllcj4KICAgICAgICAgICAgPGRpc3BsYXkgdmFsdWU9J1ByYXhpcyBIYW5zIFRvcHAtR2zDvGNrbGljaCcvPgogICAgICAgICAgPC9yZWNlaXZlcj4KICAgICAgICA8L2Rlc3RpbmF0aW9uPgogICAgICAgIDxzZW5kZXI+CiAgICAgICAgICA8aWRlbnRpZmllcj4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cDovL2dlbWF0aWsuZGUvZmhpci9zaWQvS0lNLUFkcmVzc2UnLz4KICAgICAgICAgICAgPHZhbHVlIHZhbHVlPSdwZmxlZ2VoZWltLmltbWVyZ3LDvG4uYXJ6dEBzYW5hLXBmbGVnZWhlaW1lLmtpbS50ZWxlbWF0aWsnLz4KICAgICAgICAgIDwvaWRlbnRpZmllcj4KICAgICAgICAgIDxkaXNwbGF5IHZhbHVlPSdQZmxlZ2VoZWltIEltbWVyZ3LDvG4nLz4KICAgICAgICA8L3NlbmRlcj4KICAgICAgICA8c291cmNlPgogICAgICAgICAgPGVuZHBvaW50IHZhbHVlPSdodHRwOi8vdGVzdC1wZmxlZ2VoZWltLmRlJy8+CiAgICAgICAgPC9zb3VyY2U+CiAgICAgICAgPGZvY3VzPgogICAgICAgICAgPHJlZmVyZW5jZSB2YWx1ZT0nU2VydmljZVJlcXVlc3QvVUMxLUluaXRpYWwtUHJlc2NyaXB0aW9uLVJlcXVlc3QnLz4KICAgICAgICA8L2ZvY3VzPgogICAgICA8L01lc3NhZ2VIZWFkZXI+CiAgICA8L3Jlc291cmNlPgogIDwvZW50cnk+CiAgPGVudHJ5PgogICAgPGZ1bGxVcmwgdmFsdWU9J2h0dHA6Ly9tZWRyZXEtdGVzdC5kZS9TZXJ2aWNlUmVxdWVzdC9VQzEtSW5pdGlhbC1QcmVzY3JpcHRpb24tUmVxdWVzdCcvPgogICAgPHJlc291cmNlPgogICAgICA8U2VydmljZVJlcXVlc3Q+CiAgICAgICAgPGlkIHZhbHVlPSdVQzEtSW5pdGlhbC1QcmVzY3JpcHRpb24tUmVxdWVzdCcvPgogICAgICAgIDxtZXRhPgogICAgICAgICAgPHByb2ZpbGUgdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL2VycG1lZHJlcWNvbS9TdHJ1Y3R1cmVEZWZpbml0aW9uL3NlcnZpY2UtcmVxdWVzdC1wcmVzY3JpcHRpb24tcmVxdWVzdCcvPgogICAgICAgIDwvbWV0YT4KICAgICAgICA8aWRlbnRpZmllcj4KICAgICAgICAgIDxzeXN0ZW0gdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL21lZHJlcS9zaWQvTmFtaW5nU3lzdGVtUmVxdWVzdElkZW50aWZpZXInLz4KICAgICAgICAgIDx2YWx1ZSB2YWx1ZT0nMScvPgogICAgICAgIDwvaWRlbnRpZmllcj4KICAgICAgICA8aWRlbnRpZmllcj4KICAgICAgICAgIDxzeXN0ZW0gdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL21lZHJlcS9zaWQvTmFtaW5nU3lzdGVtUHJlRGlzSWRlbnRpZmllcicvPgogICAgICAgICAgPHZhbHVlIHZhbHVlPSdQcmVEaXMtMScvPgogICAgICAgIDwvaWRlbnRpZmllcj4KICAgICAgICA8YmFzZWRPbj4KICAgICAgICAgIDxyZWZlcmVuY2UgdmFsdWU9J01lZGljYXRpb25SZXF1ZXN0L0V4YW1wbGUtSW5pdGlhbC1NZWRpY2F0aW9uLVJlcXVlc3QnLz4KICAgICAgICA8L2Jhc2VkT24+CiAgICAgICAgPHJlcXVpc2l0aW9uPgogICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvbWVkcmVxL3NpZC9OYW1pbmdTeXN0ZW1Qcm9jZWR1cmVJZGVudGlmaWVyJy8+CiAgICAgICAgICA8dmFsdWUgdmFsdWU9J0dyb3VwSUQtVUMxJy8+CiAgICAgICAgPC9yZXF1aXNpdGlvbj4KICAgICAgICA8c3RhdHVzIHZhbHVlPSdhY3RpdmUnLz4KICAgICAgICA8aW50ZW50IHZhbHVlPSdvcmRlcicvPgogICAgICAgIDxjb2RlPgogICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL0NvZGVTeXN0ZW0vc2VydmljZS1yZXF1ZXN0LXR5cGUtY3MnLz4KICAgICAgICAgICAgPGNvZGUgdmFsdWU9J3ByZXNjcmlwdGlvbi1yZXF1ZXN0Jy8+CiAgICAgICAgICA8L2NvZGluZz4KICAgICAgICA8L2NvZGU+CiAgICAgICAgPG9yZGVyRGV0YWlsPgogICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL0NvZGVTeXN0ZW0vcHJlc2NyaXB0aW9uLWZ1bGxmaWxsbWVudC10eXBlLWNzJy8+CiAgICAgICAgICAgIDxjb2RlIHZhbHVlPSdyZXR1cm4tdG8tcmVxdWVzdGVyJy8+CiAgICAgICAgICA8L2NvZGluZz4KICAgICAgICA8L29yZGVyRGV0YWlsPgogICAgICAgIDxzdWJqZWN0PgogICAgICAgICAgPHJlZmVyZW5jZSB2YWx1ZT0nUGF0aWVudC9FeGFtcGxlLVBhdGllbnQnLz4KICAgICAgICA8L3N1YmplY3Q+CiAgICAgICAgPG9jY3VycmVuY2VEYXRlVGltZSB2YWx1ZT0nMjAyMy0wMi0wMScvPgogICAgICAgIDxhdXRob3JlZE9uIHZhbHVlPScyMDIzLTAxLTI3Jy8+CiAgICAgICAgPHJlcXVlc3Rlcj4KICAgICAgICAgIDxyZWZlcmVuY2UgdmFsdWU9J09yZ2FuaXphdGlvbi9FeGFtcGxlLUhlYWx0aENhcmVTZXJ2aWNlLU9yZ2FuaXphdGlvbicvPgogICAgICAgIDwvcmVxdWVzdGVyPgogICAgICAgIDxwZXJmb3JtZXI+CiAgICAgICAgICA8aWRlbnRpZmllcj4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cDovL2dlbWF0aWsuZGUvZmhpci9zaWQvS0lNLUFkcmVzc2UnLz4KICAgICAgICAgICAgPHZhbHVlIHZhbHVlPSdoYW5zQHl0b3BwLWdsdWVja2xpY2gua2ltLnRlbGVtYXRpaycvPgogICAgICAgICAgPC9pZGVudGlmaWVyPgogICAgICAgIDwvcGVyZm9ybWVyPgogICAgICAgIDxyZWFzb25Db2RlPgogICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL0NvZGVTeXN0ZW0vbWVkaWNhdGlvbi1yZXF1ZXN0LXJlYXNvbi1jcycvPgogICAgICAgICAgICA8Y29kZSB2YWx1ZT0nbWVkaWNhdGlvbi1ydW5zLW91dCcvPgogICAgICAgICAgPC9jb2Rpbmc+CiAgICAgICAgPC9yZWFzb25Db2RlPgogICAgICAgIDxyZWFzb25SZWZlcmVuY2U+CiAgICAgICAgICA8cmVmZXJlbmNlIHZhbHVlPSdPYnNlcnZhdGlvbi9NZWRpY2F0aW9uLVJ1bnMtT3V0LUV4YW1wbGUtZGF0ZVRpbWUnLz4KICAgICAgICA8L3JlYXNvblJlZmVyZW5jZT4KICAgICAgICA8cmVhc29uUmVmZXJlbmNlPgogICAgICAgICAgPHJlZmVyZW5jZSB2YWx1ZT0nT2JzZXJ2YXRpb24vTWVkaWNhdGlvbi1SdW5zLU91dC1FeGFtcGxlLVF1YW50aXR5Jy8+CiAgICAgICAgPC9yZWFzb25SZWZlcmVuY2U+CiAgICAgICAgPG5vdGU+CiAgICAgICAgICA8dGV4dCB2YWx1ZT0nTWVkaWthbWVudCBsw6R1ZnQgYW0gMzEuMDEuMjAyMyBhdXMuIEVzIHNpbmQgbm9jaCA3IHN0ayDDvGJyaWcuICcvPgogICAgICAgIDwvbm90ZT4KICAgICAgPC9TZXJ2aWNlUmVxdWVzdD4KICAgIDwvcmVzb3VyY2U+CiAgPC9lbnRyeT4KICA8ZW50cnk+CiAgICA8ZnVsbFVybCB2YWx1ZT0naHR0cDovL21lZHJlcS10ZXN0LmRlL01lZGljYXRpb25SZXF1ZXN0L0V4YW1wbGUtSW5pdGlhbC1NZWRpY2F0aW9uLVJlcXVlc3QnLz4KICAgIDxyZXNvdXJjZT4KICAgICAgPE1lZGljYXRpb25SZXF1ZXN0PgogICAgICAgIDxpZCB2YWx1ZT0nRXhhbXBsZS1Jbml0aWFsLU1lZGljYXRpb24tUmVxdWVzdCcvPgogICAgICAgIDxtZXRhPgogICAgICAgICAgPHByb2ZpbGUgdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL2VycG1lZHJlcWNvbS9TdHJ1Y3R1cmVEZWZpbml0aW9uL2VycC1zZXJ2aWNlLXJlcXVlc3QtbWVkaWNhdGlvbi1yZXF1ZXN0Jy8+CiAgICAgICAgPC9tZXRhPgogICAgICAgIDxleHRlbnNpb24gdXJsPSdodHRwczovL2dlbWF0aWsuZGUvZmhpci9lcnBtZWRyZXFjb20vU3RydWN0dXJlRGVmaW5pdGlvbi9wcmVzY3JpcHRpb24taWQtZXgnPgogICAgICAgICAgPHZhbHVlSWRlbnRpZmllcj4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwL05hbWluZ1N5c3RlbS9HRU1fRVJQX05TX1ByZXNjcmlwdGlvbklkJy8+CiAgICAgICAgICAgIDx2YWx1ZSB2YWx1ZT0nMTYwLjEwMC4wMDAuMDAwLjAwMS4zNicvPgogICAgICAgICAgPC92YWx1ZUlkZW50aWZpZXI+CiAgICAgICAgPC9leHRlbnNpb24+CiAgICAgICAgPHN0YXR1cyB2YWx1ZT0nYWN0aXZlJy8+CiAgICAgICAgPGludGVudCB2YWx1ZT0nb3JkZXInLz4KICAgICAgICA8bWVkaWNhdGlvblJlZmVyZW5jZT4KICAgICAgICAgIDxyZWZlcmVuY2UgdmFsdWU9J01lZGljYXRpb24vRXhhbXBsZS1Jbml0aWFsLU1lZGljYXRpb24nLz4KICAgICAgICA8L21lZGljYXRpb25SZWZlcmVuY2U+CiAgICAgICAgPHN1YmplY3Q+CiAgICAgICAgICA8cmVmZXJlbmNlIHZhbHVlPSdQYXRpZW50L0V4YW1wbGUtUGF0aWVudCcvPgogICAgICAgIDwvc3ViamVjdD4KICAgICAgICA8YXV0aG9yZWRPbiB2YWx1ZT0nMjAyMi0wNS0yMCcvPgogICAgICAgIDxkb3NhZ2VJbnN0cnVjdGlvbj4KICAgICAgICAgIDx0ZXh0IHZhbHVlPScybWFsIHTDpGdsLiA1bWwnLz4KICAgICAgICA8L2Rvc2FnZUluc3RydWN0aW9uPgogICAgICAgIDxkaXNwZW5zZVJlcXVlc3Q+CiAgICAgICAgICA8cXVhbnRpdHk+CiAgICAgICAgICAgIDx2YWx1ZSB2YWx1ZT0nMScvPgogICAgICAgICAgICA8c3lzdGVtIHZhbHVlPSdodHRwOi8vdW5pdHNvZm1lYXN1cmUub3JnJy8+CiAgICAgICAgICAgIDxjb2RlIHZhbHVlPSd7UGFja2FnZX0nLz4KICAgICAgICAgIDwvcXVhbnRpdHk+CiAgICAgICAgPC9kaXNwZW5zZVJlcXVlc3Q+CiAgICAgICAgPHN1YnN0aXR1dGlvbj4KICAgICAgICAgIDxhbGxvd2VkQm9vbGVhbiB2YWx1ZT0ndHJ1ZScvPgogICAgICAgIDwvc3Vic3RpdHV0aW9uPgogICAgICA8L01lZGljYXRpb25SZXF1ZXN0PgogICAgPC9yZXNvdXJjZT4KICA8L2VudHJ5PgogIDxlbnRyeT4KICAgIDxmdWxsVXJsIHZhbHVlPSdodHRwOi8vbWVkcmVxLXRlc3QuZGUvTWVkaWNhdGlvbi9FeGFtcGxlLUluaXRpYWwtTWVkaWNhdGlvbicvPgogICAgPHJlc291cmNlPgogICAgICA8TWVkaWNhdGlvbj4KICAgICAgICA8aWQgdmFsdWU9J0V4YW1wbGUtSW5pdGlhbC1NZWRpY2F0aW9uJy8+CiAgICAgICAgPG1ldGE+CiAgICAgICAgICA8cHJvZmlsZSB2YWx1ZT0naHR0cHM6Ly9maGlyLmtidi5kZS9TdHJ1Y3R1cmVEZWZpbml0aW9uL0tCVl9QUl9FUlBfTWVkaWNhdGlvbl9QWk58MS4xLjAnLz4KICAgICAgICA8L21ldGE+CiAgICAgICAgPGV4dGVuc2lvbiB1cmw9J2h0dHBzOi8vZmhpci5rYnYuZGUvU3RydWN0dXJlRGVmaW5pdGlvbi9LQlZfRVhfQmFzZV9NZWRpY2F0aW9uX1R5cGUnPgogICAgICAgICAgPHZhbHVlQ29kZWFibGVDb25jZXB0PgogICAgICAgICAgICA8Y29kaW5nPgogICAgICAgICAgICAgIDxzeXN0ZW0gdmFsdWU9J2h0dHA6Ly9zbm9tZWQuaW5mby9zY3QnLz4KICAgICAgICAgICAgICA8dmVyc2lvbiB2YWx1ZT0naHR0cDovL3Nub21lZC5pbmZvL3NjdC85MDAwMDAwMDAwMDAyMDcwMDgvdmVyc2lvbi8yMDIyMDMzMScvPgogICAgICAgICAgICAgIDxjb2RlIHZhbHVlPSc3NjMxNTgwMDMnLz4KICAgICAgICAgICAgICA8ZGlzcGxheSB2YWx1ZT0nTWVkaWNpbmFsIHByb2R1Y3QgKHByb2R1Y3QpJy8+CiAgICAgICAgICAgIDwvY29kaW5nPgogICAgICAgICAgPC92YWx1ZUNvZGVhYmxlQ29uY2VwdD4KICAgICAgICA8L2V4dGVuc2lvbj4KICAgICAgICA8ZXh0ZW5zaW9uIHVybD0naHR0cHM6Ly9maGlyLmtidi5kZS9TdHJ1Y3R1cmVEZWZpbml0aW9uL0tCVl9FWF9FUlBfTWVkaWNhdGlvbl9DYXRlZ29yeSc+CiAgICAgICAgICA8dmFsdWVDb2Rpbmc+CiAgICAgICAgICAgIDxzeXN0ZW0gdmFsdWU9J2h0dHBzOi8vZmhpci5rYnYuZGUvQ29kZVN5c3RlbS9LQlZfQ1NfRVJQX01lZGljYXRpb25fQ2F0ZWdvcnknLz4KICAgICAgICAgICAgPGNvZGUgdmFsdWU9JzAwJy8+CiAgICAgICAgICA8L3ZhbHVlQ29kaW5nPgogICAgICAgIDwvZXh0ZW5zaW9uPgogICAgICAgIDxleHRlbnNpb24gdXJsPSdodHRwczovL2ZoaXIua2J2LmRlL1N0cnVjdHVyZURlZmluaXRpb24vS0JWX0VYX0VSUF9NZWRpY2F0aW9uX1ZhY2NpbmUnPgogICAgICAgICAgPHZhbHVlQm9vbGVhbiB2YWx1ZT0nZmFsc2UnLz4KICAgICAgICA8L2V4dGVuc2lvbj4KICAgICAgICA8ZXh0ZW5zaW9uIHVybD0naHR0cDovL2ZoaXIuZGUvU3RydWN0dXJlRGVmaW5pdGlvbi9ub3JtZ3JvZXNzZSc+CiAgICAgICAgICA8dmFsdWVDb2RlIHZhbHVlPSdOMScvPgogICAgICAgIDwvZXh0ZW5zaW9uPgogICAgICAgIDxjb2RlPgogICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cDovL2ZoaXIuZGUvQ29kZVN5c3RlbS9pZmEvcHpuJy8+CiAgICAgICAgICAgIDxjb2RlIHZhbHVlPScwODU4NTk5NycvPgogICAgICAgICAgPC9jb2Rpbmc+CiAgICAgICAgICA8dGV4dCB2YWx1ZT0nUHJvc3BhbsKuIEh1c3RlbnNhZnQgMTAwbWwnLz4KICAgICAgICA8L2NvZGU+CiAgICAgICAgPGZvcm0+CiAgICAgICAgICA8Y29kaW5nPgogICAgICAgICAgICA8c3lzdGVtIHZhbHVlPSdodHRwczovL2ZoaXIua2J2LmRlL0NvZGVTeXN0ZW0vS0JWX0NTX1NGSElSX0tCVl9EQVJSRUlDSFVOR1NGT1JNJy8+CiAgICAgICAgICAgIDxjb2RlIHZhbHVlPSdGTEUnLz4KICAgICAgICAgIDwvY29kaW5nPgogICAgICAgIDwvZm9ybT4KICAgICAgPC9NZWRpY2F0aW9uPgogICAgPC9yZXNvdXJjZT4KICA8L2VudHJ5PgogIDxlbnRyeT4KICAgIDxmdWxsVXJsIHZhbHVlPSdodHRwOi8vbWVkcmVxLXRlc3QuZGUvUGF0aWVudC9FeGFtcGxlLVBhdGllbnQnLz4KICAgIDxyZXNvdXJjZT4KICAgICAgPFBhdGllbnQ+CiAgICAgICAgPGlkIHZhbHVlPSdFeGFtcGxlLVBhdGllbnQnLz4KICAgICAgICA8bWV0YT4KICAgICAgICAgIDxwcm9maWxlIHZhbHVlPSdodHRwczovL2ZoaXIua2J2LmRlL1N0cnVjdHVyZURlZmluaXRpb24vS0JWX1BSX0ZPUl9QYXRpZW50fDEuMS4wJy8+CiAgICAgICAgPC9tZXRhPgogICAgICAgIDxpZGVudGlmaWVyPgogICAgICAgICAgPHR5cGU+CiAgICAgICAgICAgIDxjb2Rpbmc+CiAgICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cDovL2ZoaXIuZGUvQ29kZVN5c3RlbS9pZGVudGlmaWVyLXR5cGUtZGUtYmFzaXMnLz4KICAgICAgICAgICAgICA8Y29kZSB2YWx1ZT0nR0tWJy8+CiAgICAgICAgICAgIDwvY29kaW5nPgogICAgICAgICAgPC90eXBlPgogICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cDovL2ZoaXIuZGUvc2lkL2drdi9rdmlkLTEwJy8+CiAgICAgICAgICA8dmFsdWUgdmFsdWU9J1gyMzQ1Njc4OTAnLz4KICAgICAgICA8L2lkZW50aWZpZXI+CiAgICAgICAgPG5hbWU+CiAgICAgICAgICA8dXNlIHZhbHVlPSdvZmZpY2lhbCcvPgogICAgICAgICAgPGZhbWlseSB2YWx1ZT0nS8O2bmlnc3N0ZWluJz4KICAgICAgICAgICAgPGV4dGVuc2lvbiB1cmw9J2h0dHA6Ly9obDcub3JnL2ZoaXIvU3RydWN0dXJlRGVmaW5pdGlvbi9odW1hbm5hbWUtb3duLW5hbWUnPgogICAgICAgICAgICAgIDx2YWx1ZVN0cmluZyB2YWx1ZT0nS8O2bmlnc3N0ZWluJy8+CiAgICAgICAgICAgIDwvZXh0ZW5zaW9uPgogICAgICAgICAgPC9mYW1pbHk+CiAgICAgICAgICA8Z2l2ZW4gdmFsdWU9J0x1ZGdlcicvPgogICAgICAgIDwvbmFtZT4KICAgICAgICA8YmlydGhEYXRlIHZhbHVlPScxOTM1LTA2LTIyJy8+CiAgICAgICAgPGFkZHJlc3M+CiAgICAgICAgICA8dHlwZSB2YWx1ZT0nYm90aCcvPgogICAgICAgICAgPGxpbmUgdmFsdWU9J011c3RlcnN0ci4gMSc+CiAgICAgICAgICAgIDxleHRlbnNpb24gdXJsPSdodHRwOi8vaGw3Lm9yZy9maGlyL1N0cnVjdHVyZURlZmluaXRpb24vaXNvMjEwOTAtQURYUC1ob3VzZU51bWJlcic+CiAgICAgICAgICAgICAgPHZhbHVlU3RyaW5nIHZhbHVlPScxJy8+CiAgICAgICAgICAgIDwvZXh0ZW5zaW9uPgogICAgICAgICAgICA8ZXh0ZW5zaW9uIHVybD0naHR0cDovL2hsNy5vcmcvZmhpci9TdHJ1Y3R1cmVEZWZpbml0aW9uL2lzbzIxMDkwLUFEWFAtc3RyZWV0TmFtZSc+CiAgICAgICAgICAgICAgPHZhbHVlU3RyaW5nIHZhbHVlPSdNdXN0ZXJzdHIuJy8+CiAgICAgICAgICAgIDwvZXh0ZW5zaW9uPgogICAgICAgICAgPC9saW5lPgogICAgICAgICAgPGNpdHkgdmFsdWU9J0JlcmxpbicvPgogICAgICAgICAgPHBvc3RhbENvZGUgdmFsdWU9JzEwNjIzJy8+CiAgICAgICAgPC9hZGRyZXNzPgogICAgICA8L1BhdGllbnQ+CiAgICA8L3Jlc291cmNlPgogIDwvZW50cnk+CiAgPGVudHJ5PgogICAgPGZ1bGxVcmwgdmFsdWU9J2h0dHA6Ly9tZWRyZXEtdGVzdC5kZS9Pcmdhbml6YXRpb24vRXhhbXBsZS1IZWFsdGhDYXJlU2VydmljZS1Pcmdhbml6YXRpb24nLz4KICAgIDxyZXNvdXJjZT4KICAgICAgPE9yZ2FuaXphdGlvbj4KICAgICAgICA8aWQgdmFsdWU9J0V4YW1wbGUtSGVhbHRoQ2FyZVNlcnZpY2UtT3JnYW5pemF0aW9uJy8+CiAgICAgICAgPG1ldGE+CiAgICAgICAgICA8cHJvZmlsZSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL1N0cnVjdHVyZURlZmluaXRpb24vZXJwLXNlcnZpY2UtcmVxdWVzdC1vcmdhbml6YXRpb24nLz4KICAgICAgICA8L21ldGE+CiAgICAgICAgPGlkZW50aWZpZXI+CiAgICAgICAgICA8dHlwZT4KICAgICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgICA8c3lzdGVtIHZhbHVlPSdodHRwczovL2dlbWF0aWsuZGUvZmhpci9kaXJlY3RvcnkvQ29kZVN5c3RlbS9FbmRwb2ludERpcmVjdG9yeUNvbm5lY3Rpb25UeXBlJy8+CiAgICAgICAgICAgICAgPGNvZGUgdmFsdWU9J2tpbS0yLjAnLz4KICAgICAgICAgICAgPC9jb2Rpbmc+CiAgICAgICAgICA8L3R5cGU+CiAgICAgICAgICA8c3lzdGVtIHZhbHVlPSdodHRwOi8vZ2VtYXRpay5kZS9maGlyL3NpZC9LSU0tQWRyZXNzZScvPgogICAgICAgICAgPHZhbHVlIHZhbHVlPSdwZmxlZ2VoZWltLmltbWVyZ3LDvG4uYXJ6dEBzYW5hLXBmbGVnZWhlaW1lLmtpbS50ZWxlbWF0aWsnLz4KICAgICAgICA8L2lkZW50aWZpZXI+CiAgICAgICAgPGlkZW50aWZpZXI+CiAgICAgICAgICA8dHlwZT4KICAgICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgICA8c3lzdGVtIHZhbHVlPSdodHRwOi8vdGVybWlub2xvZ3kuaGw3Lm9yZy9Db2RlU3lzdGVtL3YyLTAyMDMnLz4KICAgICAgICAgICAgICA8Y29kZSB2YWx1ZT0nUFJOJy8+CiAgICAgICAgICAgIDwvY29kaW5nPgogICAgICAgICAgPC90eXBlPgogICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvc2lkL3RlbGVtYXRpay1pZCcvPgogICAgICAgICAgPHZhbHVlIHZhbHVlPScxLTAzMTIzNDU2NycvPgogICAgICAgIDwvaWRlbnRpZmllcj4KICAgICAgICA8aWRlbnRpZmllcj4KICAgICAgICAgIDx0eXBlPgogICAgICAgICAgICA8Y29kaW5nPgogICAgICAgICAgICAgIDxzeXN0ZW0gdmFsdWU9J2h0dHA6Ly90ZXJtaW5vbG9neS5obDcub3JnL0NvZGVTeXN0ZW0vdjItMDIwMycvPgogICAgICAgICAgICAgIDxjb2RlIHZhbHVlPSdCU05SJy8+CiAgICAgICAgICAgIDwvY29kaW5nPgogICAgICAgICAgPC90eXBlPgogICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9maGlyLmtidi5kZS9OYW1pbmdTeXN0ZW0vS0JWX05TX0Jhc2VfQlNOUicvPgogICAgICAgICAgPHZhbHVlIHZhbHVlPScwMzEyMzQ1NjcnLz4KICAgICAgICA8L2lkZW50aWZpZXI+CiAgICAgICAgPG5hbWUgdmFsdWU9J1BmbGVnZWhlaW0gSW1tZXJncsO8bicvPgogICAgICAgIDx0ZWxlY29tPgogICAgICAgICAgPHN5c3RlbSB2YWx1ZT0ncGhvbmUnLz4KICAgICAgICAgIDx2YWx1ZSB2YWx1ZT0nMDMwMTIzNDU2NycvPgogICAgICAgIDwvdGVsZWNvbT4KICAgICAgICA8YWRkcmVzcz4KICAgICAgICAgIDx0eXBlIHZhbHVlPSdib3RoJy8+CiAgICAgICAgICA8bGluZSB2YWx1ZT0nTXVzdGVyc3RyLiAyJz4KICAgICAgICAgICAgPGV4dGVuc2lvbiB1cmw9J2h0dHA6Ly9obDcub3JnL2ZoaXIvU3RydWN0dXJlRGVmaW5pdGlvbi9pc28yMTA5MC1BRFhQLWhvdXNlTnVtYmVyJz4KICAgICAgICAgICAgICA8dmFsdWVTdHJpbmcgdmFsdWU9JzInLz4KICAgICAgICAgICAgPC9leHRlbnNpb24+CiAgICAgICAgICAgIDxleHRlbnNpb24gdXJsPSdodHRwOi8vaGw3Lm9yZy9maGlyL1N0cnVjdHVyZURlZmluaXRpb24vaXNvMjEwOTAtQURYUC1zdHJlZXROYW1lJz4KICAgICAgICAgICAgICA8dmFsdWVTdHJpbmcgdmFsdWU9J011c3RlcnN0ci4nLz4KICAgICAgICAgICAgPC9leHRlbnNpb24+CiAgICAgICAgICA8L2xpbmU+CiAgICAgICAgICA8Y2l0eSB2YWx1ZT0nQmVybGluJy8+CiAgICAgICAgICA8cG9zdGFsQ29kZSB2YWx1ZT0nMTA2MjMnLz4KICAgICAgICA8L2FkZHJlc3M+CiAgICAgIDwvT3JnYW5pemF0aW9uPgogICAgPC9yZXNvdXJjZT4KICA8L2VudHJ5PgogIDxlbnRyeT4KICAgIDxmdWxsVXJsIHZhbHVlPSdodHRwOi8vbWVkcmVxLXRlc3QuZGUvT2JzZXJ2YXRpb24vTWVkaWNhdGlvbi1SdW5zLU91dC1FeGFtcGxlLWRhdGVUaW1lJy8+CiAgICA8cmVzb3VyY2U+CiAgICAgIDxPYnNlcnZhdGlvbj4KICAgICAgICA8aWQgdmFsdWU9J01lZGljYXRpb24tUnVucy1PdXQtRXhhbXBsZS1kYXRlVGltZScvPgogICAgICAgIDxtZXRhPgogICAgICAgICAgPHByb2ZpbGUgdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL2VycG1lZHJlcWNvbS9TdHJ1Y3R1cmVEZWZpbml0aW9uL2VycC1zZXJ2aWNlLXJlcXVlc3QtcmVtYWluaW5nLW1lZGljYXRpb24nLz4KICAgICAgICA8L21ldGE+CiAgICAgICAgPHN0YXR1cyB2YWx1ZT0nZmluYWwnLz4KICAgICAgICA8Y29kZT4KICAgICAgICAgIDxjb2Rpbmc+CiAgICAgICAgICAgIDxzeXN0ZW0gdmFsdWU9J2h0dHBzOi8vZ2VtYXRpay5kZS9maGlyL2VycG1lZHJlcWNvbS9Db2RlU3lzdGVtL21lZGljYXRpb24tb2JzZXJ2YXRpb24tY3MnLz4KICAgICAgICAgICAgPGNvZGUgdmFsdWU9J3JhbmdlLW9mLW1lZGljYXRpb24nLz4KICAgICAgICAgIDwvY29kaW5nPgogICAgICAgIDwvY29kZT4KICAgICAgICA8c3ViamVjdD4KICAgICAgICAgIDxyZWZlcmVuY2UgdmFsdWU9J1BhdGllbnQvRXhhbXBsZS1QYXRpZW50Jy8+CiAgICAgICAgPC9zdWJqZWN0PgogICAgICAgIDx2YWx1ZURhdGVUaW1lIHZhbHVlPScyMDIzLTAxLTMxJy8+CiAgICAgIDwvT2JzZXJ2YXRpb24+CiAgICA8L3Jlc291cmNlPgogIDwvZW50cnk+CiAgPGVudHJ5PgogICAgPGZ1bGxVcmwgdmFsdWU9J2h0dHA6Ly9tZWRyZXEtdGVzdC5kZS9PYnNlcnZhdGlvbi9NZWRpY2F0aW9uLVJ1bnMtT3V0LUV4YW1wbGUtUXVhbnRpdHknLz4KICAgIDxyZXNvdXJjZT4KICAgICAgPE9ic2VydmF0aW9uPgogICAgICAgIDxpZCB2YWx1ZT0nTWVkaWNhdGlvbi1SdW5zLU91dC1FeGFtcGxlLVF1YW50aXR5Jy8+CiAgICAgICAgPG1ldGE+CiAgICAgICAgICA8cHJvZmlsZSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL1N0cnVjdHVyZURlZmluaXRpb24vZXJwLXNlcnZpY2UtcmVxdWVzdC1yZW1haW5pbmctbWVkaWNhdGlvbicvPgogICAgICAgIDwvbWV0YT4KICAgICAgICA8c3RhdHVzIHZhbHVlPSdmaW5hbCcvPgogICAgICAgIDxjb2RlPgogICAgICAgICAgPGNvZGluZz4KICAgICAgICAgICAgPHN5c3RlbSB2YWx1ZT0naHR0cHM6Ly9nZW1hdGlrLmRlL2ZoaXIvZXJwbWVkcmVxY29tL0NvZGVTeXN0ZW0vbWVkaWNhdGlvbi1vYnNlcnZhdGlvbi1jcycvPgogICAgICAgICAgICA8Y29kZSB2YWx1ZT0ncmFuZ2Utb2YtbWVkaWNhdGlvbicvPgogICAgICAgICAgPC9jb2Rpbmc+CiAgICAgICAgPC9jb2RlPgogICAgICAgIDxzdWJqZWN0PgogICAgICAgICAgPHJlZmVyZW5jZSB2YWx1ZT0nUGF0aWVudC9FeGFtcGxlLVBhdGllbnQnLz4KICAgICAgICA8L3N1YmplY3Q+CiAgICAgICAgPHZhbHVlUXVhbnRpdHk+CiAgICAgICAgICA8dmFsdWUgdmFsdWU9JzcnLz4KICAgICAgICAgIDx1bml0IHZhbHVlPSdzdGsnLz4KICAgICAgICA8L3ZhbHVlUXVhbnRpdHk+CiAgICAgIDwvT2JzZXJ2YXRpb24+CiAgICA8L3Jlc291cmNlPgogIDwvZW50cnk+CjwvQnVuZGxlPg==
    ------=_Part_6_1831919254.1667563379306--