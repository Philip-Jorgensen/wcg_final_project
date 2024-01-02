---
date: 2023-11-22
type: lab_notes
subject: Thesis project
measurement:
  - PBS
tags: 
Device: UV-1900
properties: PBS + DI
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

| Cuvette (MNHVPV 06) | DI Source |
| ------- | --------- |
| ![[20231122_141752.jpg]]  |    ![[20231010_110549 7.jpg]]       |

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

#### PBS
##### Methodology
Firstly I am waiting for the spectrophotometer to warm up.

| Warming up                    | Ready                         |
| ----------------------------- | ----------------------------- |
| ![[20231122_132639.jpg]] | ![[20231122_140407.jpg]] |

I am during the base-line measurement of the spectrophotometer after it has finished warming up.

I then did a water reference measurement with 3ml of DI water in the cuvette, following the steps from Spectroworks.

I transferred a bit of the PBS into a glass vial from where I then pipetted 2.5 ml of the PBS into the cuvette.
I waited about 5 min after taking the PBS out of the fridge before using it to let it heat up slightly.

I am doing these measurements over a span of 30 minutes, with an $\approx 1$ minute gab between each measurement.

PBS source:
![[20231122_141418.jpg|300]]

Adding 2.5ml of PBS into the cuvette

After adding both DI and PBS into the cuvette I gently shake it for about 30 seconds.
All the measurements are done with the same cuvette.

The cuvette was rinsed with DI water twice between each PBS concentration 

The different measurements are:

| PBS Concentration (%) | DI Volume (ml) | PBS Volume (ml) |
| --------------------- | -------------- | --------------- |
| 100                   | 0              | 2.5             |
| 75                    | 0.625          | 1.875           |
| 50                    | 1.25           | 1.25            |
| 25                    | 1.875          | 0.625           |

#### Result

##### PBS 100%
![[Pasted image 20231122171320.png]]
![[Pasted image 20231122170920.png]]


**Properties**

| Property | Value |
| ---------- | ----- |
| PBS Concentration |100% |
| PBS volume | 2.5 ul |
| DI water volume | 0.0 ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.005318734684802262|
| RI Shift (*moving average*) |0.004759950949497771|
| Average fit quality | 86.68% |
| Average RI | 1.342894 |
| Average RI (last half) | 1.344025 |

**Standard deviation**

| Standard deviation | Value |
| ------------------ | ----- |
| $\sigma$ $\times 10^3$ | 1.9299 |
| $\sigma$ *(last 30 minutes)* $\times 10^3$ | 0.2901 |
| $\sigma$ *(Without outliers)* $\times 10^3$ | 1.7355 |
| $\sigma$ *(Without outliers, last 30 minutes)* $\times 10^3$ | 0.2812 |



##### PBS 75%
![[Pasted image 20231122171237.png]]
![[Pasted image 20231122171242.png]]

**Properties**

| Property | Value |
| ---------- | ----- |
| PBS Concentration |75% |
| PBS volume | 1.875 ul |
| DI water volume | 0.625 ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.001378561732439998|
| RI Shift (*moving average*) |0.0007407489983828341|
| Average fit quality | 87.13% |
| Average RI | 1.343912 |
| Average RI (last half) | 1.344079 |

**Standard deviation**

| Standard deviation | Value |
| ------------------ | ----- |
| $\sigma$ $\times 10^3$ | 1.0849 |
| $\sigma$ *(last 30 minutes)* $\times 10^3$ | 0.4488 |
| $\sigma$ *(Without outliers)* $\times 10^3$ | 0.4545 |
| $\sigma$ *(Without outliers, last 30 minutes)* $\times 10^3$ | 0.4246 |



##### PBS 50%
![[Pasted image 20231122171351.png]]
![[Pasted image 20231122171356.png]]

**Properties**

| Property | Value |
| ---------- | ----- |
| PBS Concentration |50% |
| PBS volume | 1.25 ul |
| DI water volume | 1.25 ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.0012982628005051566|
| RI Shift (*moving average*) |0.0008165369637938014|
| Average fit quality | 87.23% |
| Average RI | 1.343874 |
| Average RI (last half) | 1.344088 |

**Standard deviation**

| Standard deviation | Value |
| ------------------ | ----- |
| $\sigma$ $\times 10^3$ | 0.9126 |
| $\sigma$ *(last 30 minutes)* $\times 10^3$ | 0.3271 |
| $\sigma$ *(Without outliers)* $\times 10^3$ | 0.3841 |
| $\sigma$ *(Without outliers, last 30 minutes)* $\times 10^3$ | 0.2879 |



##### PBS 25%
![[Pasted image 20231122171432.png]]
![[Pasted image 20231122171436.png]]


**Properties**

| Property | Value |
| ---------- | ----- |
| PBS Concentration |25% |
| PBS volume | 0.625 ul |
| DI water volume | 1.875 ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.0014647008981005794|
| RI Shift (*moving average*) |0.0009080524097830889|
| Average fit quality | 87.17% |
| Average RI | 1.343635 |
| Average RI (last half) | 1.343758 |

**Standard deviation**

| Standard deviation | Value |
| ------------------ | ----- |
| $\sigma$ $\times 10^3$ | 1.0960 |
| $\sigma$ *(last 30 minutes)* $\times 10^3$ | 0.8380 |
| $\sigma$ *(Without outliers)* $\times 10^3$ | 0.4083 |
| $\sigma$ *(Without outliers, last 30 minutes)* $\times 10^3$ | 0.4286 |

