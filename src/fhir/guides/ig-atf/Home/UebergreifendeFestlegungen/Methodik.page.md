# {{page-title}}

## Normen und Spezifikationen
Anforderungen als Ausdruck normativer Festlegungen werden durch die dem [RFC2119](https://tools.ietf.org/html/rfc2119) entsprechenden, in Großbuchstaben geschriebenen deutschen Schlüsselworte MUSS, DARF NICHT, SOLL, SOLL NICHT, KANN sowie ihrer Pluralformen gekennzeichnet.

## Must Support
Felder der FHIR-Spezifikation, die mit "Must Support" (MS) geflaggt sind, SOLLEN derart umgesetzt werden, dass die Inhalte dem Nutzer sichtbar gemacht werden und wo möglich auch bearbeitbar sind.

### Im Kontext des Erstellens von FHIR-Ressourcen
Wenn die entsprechende Information vorliegt, bzw. eingeholt werden kann, MUSS dieses Feld befüllt werden.

### Im Kontext des Verarbeitens von FHIR-Ressourcen
Wenn ein Feld befüllt ist MUSS die entsprechende Information im Frontend sichtbar gemacht werden.
Felder, die Referenzen zu anderen Objekten aufweisen und mit "MS" gekennzeichnet sind, MUSS das referenzierte Objekt verarbeiten und darstellen können.