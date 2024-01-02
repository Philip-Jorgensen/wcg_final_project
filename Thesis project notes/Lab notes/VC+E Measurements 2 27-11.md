---
date: 2023-11-27
type: lab_notes
subject: Thesis project
measurement:
  - VC+E T20
tags: 
Device: UV-1900
properties:
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

| Cuvette | DI Source |
| ------- | --------- |
|  ![[20231127_162705.jpg]]  | ![[20231123_171602.jpg]]          |

#### Measurement

**Results**

| Parameter             | Value |
| --------------------- | ----- |
| Refractive Index      |       |
| Reference fit quality |       |
| Sample fit quality    |       |
| Item ID               |       |


**Plot**

### Measurements


| Property | Value |
| -------- | ----- |
|Concentration multiplier|10|

**Experiment properties**

| Property | Value |
| -------- | ----- |
| VC Volume | 10.0 $\mu l$ |
| Enzyme required | 1.360 $\mu g$ |
|Water volume |10 ml |
| VC Concentration|2 $\mu g / ml$|

#### VC - T
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
3. Then gently shook the solution for 60 seconds
4. Got the enzyme from the freezer and started a stopwatch, to make sure that I didn't have the enzyme out for more than 15 minutes
5. Went to the scale to weigh out <1.5 mg of enzyme. (Final was 1.31 mg)
	1. ![[20231123_182908.jpg|200]]
6. Then added a 1:1 ratio of DI water to the enzyme (1.31 ml of DI)
7. And transferred that solution into a small plastic vial
	1. ![[20231123_183617.jpg|200]]
8. Then shook the solution for about 30 seconds.
9. Then I took 1.36 $\mu l$ of the enzyme solution (corresponding to 1.36 $\mu g$ of enzyme) and added it to the glass vial with the VC solution. 1.36 $\mu g$ corresponds with a 5x concentration compared to the standard enzyme to VC concentration.
10. I started a stopwatch from the moment that I had added the enzyme into the VC solution.
11. I gently shook the solution for  seconds.
12. I then took 3 ml of the solution and transferred it into a Nanocuvette One
13. I then took the cuvette into the Shimadzu UV-1900
14. I chose the water measurement I did earlier as the reference measurement
15. I then started the A-side measurement of the cuvette
16. Then I did the B-side measurement
17. I then entered the information from the measurement into spectroworks
	1. Measurement number
	2. Current time
	3. DI volume
	4. VC volume
	5. Enzyme mass
18. I then repeated steps 13-16 approximately every minute for 60 minutes.

##### Results

![[Pasted image 20231127200922.png]]
![[Pasted image 20231127200935.png]]


**Properties**

| Property | Value |
| ---------- | ----- |
| Test number |T20 |
| Vinyl Chloride volume | 10.0 $\mu l$ |
| Enzyme weight | 1.36 $\mu g$ |
| DI water volume | 10.0 ml |
| VC Concentration | 2.0 $\mu g / ml$ |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.0012106055106768654|
| RI Shift (*moving average*) |0.0011151908663364907|
| Average fit quality | 87.74% |
| Average RI | 1.335070 |
| Average RI (last half) | 1.335302 |

**Standard deviation**

| Standard deviation | Value |
| ------------------ | ----- |
| $\sigma$ $\times 10^3$ | 0.5811 |
| $\sigma$ *(last 30 minutes)* $\times 10^3$ | 0.3073 |
| $\sigma$ *(Without outliers)* $\times 10^3$ | 0.4093 |
| $\sigma$ *(Without outliers, last 30 minutes)* $\times 10^3$ | 0.3101 |

