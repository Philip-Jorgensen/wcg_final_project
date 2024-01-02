---
date: 08-09-2023
type: subject
subject: Thesis project
---

# [[Thesis project overview]]

## Meeting notes

```dataview
table date as "Date"
from "Thesis project"
where type="meeting"
sort date desc
```


## Lab notes

```dataview
table date as "Date", measurement
from "Thesis project"
where type="lab_notes"
sort date desc
```


## All
```dataview
table date as "Date", type as "Type"
from "Thesis project"
where type != "meeting" and type != "lab_notes"
```

**Spectrolink in photonics lab**
KV2GMNPCMZB63
![[20230919_125120.jpg|400]]

