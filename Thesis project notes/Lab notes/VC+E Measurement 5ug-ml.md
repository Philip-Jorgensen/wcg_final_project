---
date: 2023-10-30
type: lab_notes
subject: Thesis project
measurement:
  - VC T10
  - T11
tags: 
Device: UV-1900
properties: VC 5ug/ml
---
## Files
**Chemical safety:** [[Chemical safety]]
**Procedure:** [[Measurements procedure]]

## Notes

### Water reference

#### Setup
**Settings**

| Parameter             | Value   |
| --------------------- | ------- |
| Wavelength range (nm) | 200-800 |
| Scan speed            | Survey  |
| Scan resolution       | 1.0nm   |
| Filter                | None        |

| Cuvette (JNHQFB 02) | DI Source |
| ------- | --------- |
|  ![[20231030_133855.jpg]]  |  ![[20231010_110549 5.jpg]]         |

#### Measurement
3 ml of DI water
The first time I ran the B-side reference measurement it gave me a fit of 43% but it looked like everything was scaled wrong, so I did another baseline measurement and tried again, then I got 83% fit quality.

**Results**

| Parameter             | Value         |
| --------------------- | ------------- |
| Refractive Index      | 1.33721941 nD |
| Reference fit quality | 83.2778 %     |
| Sample fit quality    | 82.0440 %     |
| Item ID               | 6226e90f              |


**Plot**
![[LABT_20231030_133906__spectra..png]]

### Measurements
(look at 550 - 800 nm instead)
#### VC - T
##### Methodology
1. First I took a cuvette from the photonics lab and brought it to the chemistry lab to get 3ml of DI water in it
2. Then I brought the cuvette back to the photonics lab to get the reference measurement
3. I put the cuvette with DI into the UV-1900
4. Went to the "Create" tab in Spectroworks and entered the Cuvette "JNHQFB 02"
5. Then I measured pressed "Capture" (while the cuvette was in the B-position)
6. Then I rotated the cuvette to the A-position and pressed "Capture"
7. Then I rotated the cuvette to the B-position and pressed "Capture"
8. Then I took the cuvette to the chemistry lab and added 7.5 ul of VC into the cuvette (inside the fumehood)
9. Then I stirred the cuvette for ~30s
10. Then I brought the cuvette back to the photonics lab
11. Then I pressed "Create" in spectroworks
12. Then I choose the previous reference measurement in the top left corner
13. Then I measured the A-side of the cuvette with VC
14. Then I measured the B-side of the cuvette with VC
15. Then I repeated the steps every other minute until I reached 60 minutes

##### Results
| Time (min) | Fit quality (%) | Refractive index (nD) |
| ---------- | --------------- | --------------------- |
| 4          | 85.5696         | 1.34027352            |
| 6          | 82.1199         | 1.33782942            |
| 8          | 85.8906         | 1.34158767            |
| 10         | 85.6129         | 1.33970580            |
| 12         | 85.9374         | 1.34184893            |
| 14         | 85.6885         | 1.34112822            |
| 16         | 85.7672         | 1.34091512            |
| 18         | 85.9661         | 1.34189847            |
| 20         | 85.8557         | 1.33997378            |
| 22         | 85.9116         | 1.34018431            |
| 24         | 86.1801         | 1.34234891            |
| 26         | 86.2114         | 1.34176644            |
| 28         | 86.0397         | 1.34173344            |
| 30         | 85.7620         | 1.34044463            |
| 33         | 85.8793         | 1.34088071            |
| 34.5       | 86.1541         | 1.34172497            |
| 36         | 85.7917         | 1.34022877            |
| 38         | 85.7617         | 1.34034075            |
| 40         | 86.0245         | 1.34154729            |
| 42         | 85.8702         | 1.34052169            |
| 44         | 85.9657         | 1.34067988            |
| 46         | 86.0699         | 1.34224910            |
| 48         | 85.9260         | 1.34069667            |
| 50         | 85.7709         | 1.34073543            |
| 52         | 86.2475         | 1.34238005            |
| 54         | 85.6436         | 1.34035613            |
| 56         | 85.9802         | 1.34177947            |
| 58         | 85.8023         | 1.34062106            |
| 60         | 85.7075         | 1.34029237                      |

![[Pasted image 20231030150443.png]]

RI Shift: 0.0021065267161315404
Analyte: VC 7.5ul
Vinyl Chloride volume: 7.5 ul
DI water volume: 3.0 ml
VC Concentration: 5.0 ug/ml


**Properties**

| Property | Value |
| ---------- | ----- |
| Test number |T10 |
| Vinyl Chloride volume | 7.5 ul |
| Enzyme weight | 0 ug |
| DI water volume | 3.0 ml |
| VC Concentration | 5.0 ug/ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.0021065267161315404|
| RI Shift (*moving average*) |0.0014272603045135668|
| Average fit quality | 85.76% |
| Standard deviation ($\sigma$) $\times 10^3$ | 0.9547 |
| Standard deviation ($\sigma$) *(last 30 minutes)* $\times 10^3$ | 0.7068 |


#### VC+E Measurement T11
Settings:
Wavelength range 550-800 nm
The rest is the same

| Time (min) | Fit quality (%) | Refractive index (nD) |
| ---------- | --------------- | --------------------- |
| 5          | 85.6116         | 1.33972926            |
| 7          | 85.6997         | 1.33982580            |
| 8.5        | 85.7450         | 1.33994931            |
| 10         | 86.2323         | 1.34199510            |
| 11.5       | 86.4109         | 1.34214514            |
| 13         | 85.8771         | 1.34137825            |
| 14.5       | 85.7083         | 1.34012212            |
| 16         | 86.0208         | 1.34043135            |
| 17.5       | 86.4567         | 1.34283443            |
| 19         | 86.1532         | 1.34050332            |
| 20         | 85.9190         | 1.34080686            |
| 21.5       | 85.7513         | 1.34036201            |
| 22.5       | 85.9091         | 1.34243610            |
| 23.5       | 86.0217         | 1.34052913            |
| 24.5       | 85.8989         | 1.34062857            |
| 25.5       | 85.8781         | 1.34056599            |
| 26.5       | 86.0847         | 1.34131432            |
| 27.5       | 86.0556         | 1.34076566            |
| 28.5       | 85.9260         | 1.34054457            |
| 29.5       | 85.8659         | 1.34113839            |
| 31         | 85.7893         | 1.34052709            |
| 33         | 85.8834         | 1.34050273            |
| 35         | 85.9928         | 1.34065429            |
| 37         | 85.6290         | 1.34053134            |
| 39         | 85.5052         | 1.34043897            |
| 41         | 85.5413         | 1.34060078            |
| 43         | 85.9965         | 1.34220840            |
| 45         | 86.3670         | 1.34303729            |
| 47         | 85.7606         | 1.34081478            |
| 49         | 85.9349         | 1.34123350            |
| 51         | 85.9436         | 1.34092004            |
| 53         | 85.9624         | 1.34086164            |
| 55         | 85.7535         | 1.34072684            |
| 57         | 85.9233         | 1.34167948            |
| 59         | 85.8045         | 1.34078906                      |

![[Pasted image 20231030170026.png]]

RI Shift: 0.003308028638019822
Analyte: VC 7.5ul + Enzyme
Vinyl Chloride volume: 7.5 ul
DI water volume: 3.0 ml
VC Concentration: 5.0 ug/ml
Enzyme required for 7.5ul of VC: 0.102 micro grams


**Properties**

| Property | Value |
| ---------- | ----- |
| Test number |T11 |
| Vinyl Chloride volume | 7.5 ul |
| Enzyme weight | 0 ug |
| DI water volume | 3.0 ml |
| VC Concentration | 5.0 ug/ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.00270683750717593|
| RI Shift (*moving average*) |0.0020047074834366185|
| Average fit quality | 85.91% |
| Standard deviation ($\sigma$) $\times 10^3$ | 0.7966 |
| Standard deviation ($\sigma$) *(last 30 minutes)* $\times 10^3$ | 0.6613 |

