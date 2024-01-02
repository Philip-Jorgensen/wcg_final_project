---
date: 2023-09-19
type: lab_notes
subject: Thesis project
tags: 
Device: WCG Suitcase
---
## Files
**New update with filter for the spectrolink** (19/09/2023 12:09)

Hi Philip.

The update has been deployed. When you connect to your SpectroLink™ you should see a popup asking you to update to v1.6.5. Updating takes a few minutes. Be patient and **do not** unplug the device while updating is in progress. Once updated you should see the new noise filtering options. Play around with the settings and see what gives the best results for you. A good starting point could be boxcar filtering with a size of 5.

I hope this solves your problem. Don't hesitate to reach out again if you need further assistance.

Best regards
**Thomas Tølbøl Sørensen** **:** Product Architect **:** cphnano  
[Hørmarken 2, DK-3520 Farum, Denmark](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.google.com%2Fmaps%2Fplace%2FH%25C3%25B8rmarken%2B2%2C%2B3520%2BFarum&data=05%7C01%7Cphjoe20%40student.sdu.dk%7Cce9e0fe9a9dd46a170fa08dbb8f87dea%7C9a97c27db83e4694b35354bdbf18ab5b%7C0%7C0%7C638307149728251875%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=bCVY205I2Jc5faHpixnvKQCz8kUH07mLfSGKxk%2BNlXk%3D&reserved=0) **:** [www.cphnano.com](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.cphnano.com%2F&data=05%7C01%7Cphjoe20%40student.sdu.dk%7Cce9e0fe9a9dd46a170fa08dbb8f87dea%7C9a97c27db83e4694b35354bdbf18ab5b%7C0%7C0%7C638307149728251875%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=4XMUz7Kj13dlObm7BVjIJUpnTQWfS5yUjSxuQuaXau4%3D&reserved=0)  
Direct +45 29 86 10 56 **:** [thots@cphnano.com](mailto:thots@cphnano.com)

## Notes
There was an update to the spectrolink which added a filter. Trying again after the update.

>For measuring the background spectrum I am using the black piece instead of turning off the lamp.
### Try 1
**Settings:**

| Type             | Value           |
| ---------------- | --------------- |
| Cuvette          | HFTTQM 02       |
| Solvent          | Distilled Water |
| Integration time | 450 ms          |
| No. of scans     | 50              |
| Filter type      | boxcar          |
| Filter size      | 5                |

**Result**
![[Pasted image 20230919162329.png]]

---

### Try 2
**Settings:**

| Type             | Value           |
| ---------------- | --------------- |
| Cuvette          | HFTTQM 02       |
| Solvent          | Distilled Water |
| Integration time | 450 ms          |
| No. of scans     | 66            |
| Filter type      | boxcar          |
| Filter size      | 5                |

**Result**
![[Pasted image 20230919162754.png]]

---

### Try 3
**Settings**

| Type             | Value           |
| ---------------- | --------------- |
| Cuvette          | HFTTQM 02       |
| Solvent          | Distilled Water |
| Integration time | 450 ms          |
| No. of scans     | 66              |
| Filter type      | boxcar          |
| Filter size      | 9              |

**Result**
![[Pasted image 20230919163116.png]]

---
### Try 4
**Settings**

| Type             | Value           |
| ---------------- | --------------- |
| Cuvette          | HFTTQM 02       |
| Solvent          | Distilled Water |
| Integration time | 450 ms          |
| No. of scans     | 66              |
| Filter type      | gaussian          |
| Filter size      | 5              |

**Result**
![[Pasted image 20230919163554.png]]
