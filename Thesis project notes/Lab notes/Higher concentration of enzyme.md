---
date: 2023-11-08
type: lab_notes
subject: Thesis project
measurement:
  - VC+E T13
tags: 
Device: UV-1900
properties: VC 5ug/ml + E x2
---
## Files
**Chemical safety:** [[Chemical safety]]
**Procedure:** [[Measurements procedure]]

## Notes
Taking a higher concentration of enzyme than usual. Doing it with a concentration 2x the standard concentration.

| Property | Value |
| -------- | ----- |
|Enzyme mass|4555.585670465049 g|
|Concentration|129415.90601487482|
|Concentration multiplier|2|
|Testing concentration|3.9999999999999996e-05|

**Experiment properties**

| Property | Value |
| -------- | ----- |
| VC Volume | 25.0 ul |
| Enzyme required | 6.8e-07 micro grams |
|Water volume |10 ml |
| VC Concentration|5 ug/ml|
### Water reference

#### Setup
**Settings**

| Parameter             | Value |
| --------------------- | ----- |
| Wavelength range (nm) | 550-800      |
| Scan speed            |     Survey  |
| Scan resolution       |  1.0 nm     |
| Filter                      |  None     |

| Cuvette | DI Source |
| ------- | --------- |
| IMAGE   | IMAGE          |

#### Measurement

**Results**

| Parameter             | Value |
| --------------------- | ----- |
| Refractive Index      |   1.33545285    |
| Reference fit quality |     88.9120  |
| Sample fit quality    |     87.4040  |
| Item ID               |     015ca74f  |


**Plot**
![[LABT_20231108_131617__spectra..png]]

### Measurements

#### VC - T
##### Methodology


##### Results

![[Pasted image 20231108151233.png]]
![[Pasted image 20231108151221.png]]


**Properties**

| Property | Value |
| ---------- | ----- |
| Test number |T13 |
| Vinyl Chloride volume | 25.0 ul |
| Enzyme weight | 0.68 ug |
| DI water volume | 10.0 ml |
| VC Concentration | 5.0 ug/ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.0007369773414696024|
| RI Shift (*moving average*) |0.0005550059074499458|
| Average fit quality | 86.56% |
| Standard deviation ($\sigma$) $\times 10^3$ | 0.3861 |
| Standard deviation ($\sigma$) *(last 30 minutes)* $\times 10^3$ | 0.3099 |


**Hypothesis**
Thinking that the reason for the *jitter* could be because of not enough enzyme.

Comparing this graph with the previous graph [[VC Measurement with UV-1900]], on the same scale we get the following graphs.
The fluctuations are still big, but not as drastic as it looked before. Although it doesn't have the expected jump at around the 20 minute mark.
![[Pasted image 20231108183028.png]]
![[Pasted image 20231108183052.png]]