---
date: 2023-11-23
type: lab_notes
subject: Thesis project
measurement:
  - VC+E T18
tags: 
Device: UV-1900
properties: VC 4ug/ml + 5x E
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
| Wavelength range (nm) | 550-800 |
| Scan speed            | Survey  |
| Scan resolution       | 1.0nm   |
| Filter                | None        |

| Cuvette (MNHVPV 10) | DI Source |
| ------- | --------- |
|  ![[20231123_172120.jpg]]  | ![[20231123_171602.jpg]]          |

#### Measurement

**Results**

| Parameter             | Value      |
| --------------------- | ---------- |
| Refractive Index      | 1.33562723 |
| Reference fit quality | 91.3875    |
| Sample fit quality    | 90.7275    |
| Item ID               | 088cfa6a           |


**Plot**
![[LABT_20231123_173657__spectra..png]]

### Measurements


| Property | Value |
| -------- | ----- |
|Enzyme mass|4555.585670465049 g|
|Concentration|129415.90601487482|
|Concentration multiplier|5|

**Experiment properties**

| Property | Value |
| -------- | ----- |
| VC Volume | 20.0 $\mu l$ |
| Enzyme required | 1.360 $\mu g$ |
|Water volume |10 ml |
| VC Concentration|4 $\mu g / ml$|


#### VC+E - T18
##### Methodology
Firstly I am waiting for the spectrophotometer to warm up.

| Warming up                    | Ready                         |
| ----------------------------- | ----------------------------- |
| ![[20231122_132639.jpg]] | ![[20231122_140407.jpg]] |

I am during the base-line measurement of the spectrophotometer after it has finished warming up.

I then did a water reference measurement with 3ml of DI water in the cuvette, following the steps from Spectroworks.

I used new Vinyl Chloride and a relatively new enzyme along with a new cuvette.

The steps taken for the VC measurement:
1. Added 10 ml of DI water into a glass vial
2. Added 20 $\mu l$ of VC into the class vial *(done in the fume hood)*
3. Got the enzyme from the freezer and started a stopwatch, to make sure that I didn't have the enzyme out for more than 15 minutes
4. Went to the scale to weigh out <1.5 mg of enzyme. (Final was 1.31 mg)
	1. ![[20231123_182908.jpg|200]]
5. Then added a 1:1 ratio of DI water to the enzyme (1.31 ml of DI)
6. And transferred that solution into a small plastic vial
	1. ![[20231123_183617.jpg|200]]
7. Then shook the solution for about 30 seconds.
8. Then I took 1.36 $\mu l$ of the enzyme solution (corresponding to 1.36 $\mu g$ of enzyme) and added it to the glass vial with the VC solution. 1.36 $\mu g$ corresponds with a 5x concentration compared to the standard enzyme to VC concentration.
9. I started a stopwatch from the moment that I had added the enzyme into the VC solution.
10. I gently shook the solution for 30 seconds.
11. I then took 3 ml of the solution and transferred it into a Nanocuvette One
12. I then took the cuvette into the Shimadzu UV-1900
13. I chose the water measurement I did earlier as the reference measurement
14. I then started the A-side measurement of the cuvette
15. Then I did the B-side measurement
16. I then entered the information from the measurement into spectroworks
	1. Measurement number
	2. Current time
	3. DI volume
	4. VC volume
	5. Enzyme mass
17. I then repeated steps 13-16 approximately every minute for 60 minutes.

##### Results
![[Pasted image 20231123195220.png]]
![[Pasted image 20231123195225.png]]


**Properties**

| Property | Value |
| ---------- | ----- |
| Test number |T18 |
| Vinyl Chloride volume | 20.0 ul |
| Enzyme weight | 1.36 ug |
| DI water volume | 10.0 ml |
| VC Concentration | 4.0 ug/ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|9.261423975526206e-05|
| RI Shift (*moving average*) |0.00027724321568922683|
| Average fit quality | 90.22% |
| Average RI | 1.342092 |
| Average RI (last half) | 1.342272 |

**Standard deviation**

| Standard deviation | Value |
| ------------------ | ----- |
| $\sigma$ $\times 10^3$ | 0.4242 |
| $\sigma$ *(last 30 minutes)* $\times 10^3$ | 0.1491 |
| $\sigma$ *(Without outliers)* $\times 10^3$ | 0.2834 |
| $\sigma$ *(Without outliers, last 30 minutes)* $\times 10^3$ | 0.1461 |

