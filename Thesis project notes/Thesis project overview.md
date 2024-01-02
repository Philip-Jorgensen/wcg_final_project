---
date: 2023-09-08
type: subject
subject: Thesis project
---
Try water with salt and water with sugar and see the refractive index
To reduce the number of unknowns

Try to remove the human element
We can't exclude errors in the spectrometer and the cuvettes

---
Do water in different cuvettes
100% PBS
75%
50%
25%
5%

---

# [[Thesis project overview]]

## Meeting notes

```dataview
table dateformat(date, "dd/MM") as "Date"
from "Thesis project"
where type="meeting"
sort date desc
```


## Lab notes

```dataview
table dateformat(date,"dd/MM") as "Date", measurement, Device, properties
from "Thesis project"
where type="lab_notes"
sort date desc, measurement
```


## All
```dataview
table dateformat(date, "dd/MM") as "Date", type as "Type"
from "Thesis project"
where type != "meeting" and type != "lab_notes"
sort date desc
```

**Spectrolink in photonics lab**
KV2GMNPCMZB63
![[20230919_125120.jpg|400]]

Working with the Shimadzu UV-1900 in spectroworks
- https://knowledge.cphnano.com/en/pages/shimadzu-uv-1900-uv-vis-spectrophotometer
- 15 mm scan height

[[Thesis Report - Brainstorming]]

![[Project Formulation overview.canvas]]