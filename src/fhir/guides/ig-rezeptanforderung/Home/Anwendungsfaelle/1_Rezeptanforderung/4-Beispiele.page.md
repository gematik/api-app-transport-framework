## {{page-title}}

### Beispiele für Zustelltyp #return-to-requester

Beispiele für diesen Anwendungsfall befinden sich im [Simplifier Projekt](https://simplifier.net/erezept-medicationrequest-communication/~resources?category=Example&exampletype=Bundle&sortBy=RankScore_desc). Beispiele für diesen Anwendungsfall sind benannt nach "UC1-*"

@```

from Bundle
where id.startsWith('UC1-')
select id

```

### Beispiele für Zustelltyp #send-to-pharmacy

Beispiele für diesen Anwendungsfall befinden sich im [Simplifier Projekt](https://simplifier.net/erezept-medicationrequest-communication/~resources?category=Example&exampletype=Bundle&sortBy=RankScore_desc). Beispiele für diesen Anwendungsfall sind benannt nach "UC2-*"

@```

from Bundle
where id.startsWith('UC2-')
select id

```

### Beispiele für Zustelltyp #issue-prescription

Beispiele für diesen Anwendungsfall befinden sich im [Simplifier Projekt](https://simplifier.net/erezept-medicationrequest-communication/~resources?category=Example&exampletype=Bundle&sortBy=RankScore_desc). Beispiele für diesen Anwendungsfall sind benannt nach "UC3-*"

@```

from Bundle
where id.startsWith('UC3-')
select id

```
