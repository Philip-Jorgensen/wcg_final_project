---
date: 2023-10-09
type: lab_notes
subject: Thesis project
measurement:
  - VC T5
tags:
  - filter_testing
Device: WCG Suitcase
properties: VC 9.6ug/ml
---
## Files


## Notes
Because it is a xenon lamp it is pulsing so the integration time doesn't matter much, having a low integration time with a high number of scans is better.\
The light source is **PX-2 From Ocean Insight (Pulsed Xenon lamp**


### Setting up
- 2.5 ml DI water


**Light source spectrum:**\
![[Pasted image 20231009144220.png]]

**Background spectrum:**\
![[Pasted image 20231009144308.png]]

#### Filter settings
*This is with the Lamb ON and no cuvette in the holder*\
Integration time: 20 ms\
No. of scans: 500\

| Spectrum                             | Filter Type | Filter size |
| ------------------------------------ | ----------- | ----------- |
| ![[Pasted image 20231009162742.png]] | None        |             |
| ![[Pasted image 20231009154356.png]] | Boxcar      | 3           |
| ![[Pasted image 20231009154426.png]] | Boxcar      | 5           |
| ![[Pasted image 20231009154450.png]] | Boxcar      | 7           |
| ![[Pasted image 20231009154516.png]] | Boxcar      | 9           |
| ![[Pasted image 20231009154538.png]] | Boxcar      | 11          |
| ![[Pasted image 20231009154603.png]] | Gaussian    | 3           |
| ![[Pasted image 20231009154626.png]] | Guassian    | 5           |
| ![[Pasted image 20231009154658.png]] | Gaussian    | 7           |
| ![[Pasted image 20231009154727.png]] | Gaussian    | 9           |
| ![[Pasted image 20231009154751.png]] | Gaussian    | 11          |
| ![[Pasted image 20231009154821.png]] | Median      | 3           |
| ![[Pasted image 20231009154847.png]] | Median      | 5           |
| ![[Pasted image 20231009154914.png]] | Median      | 7           |
| ![[Pasted image 20231009154943.png]] | Median      | 9           |
| ![[Pasted image 20231009155009.png]] | Median      | 11          |

#### Water measurement
*Going through with the measurements regardless of fit quality*

| Cuvette                  | Sample source |
| ------------------------ | ------------- |
| ![[20231009_164204.jpg]] |     ![[20231009_164258.jpg]]          |

| Image                                | Settings |
| ------------------------------------ | -------- |
| ![[Pasted image 20231009164726.png]] | ![[Pasted image 20231009164049.png]]         |

**Results**

| Property              | Value      |
| --------------------- | ---------- |
| Refractive index      | 1.55959097 |
| Reference fit quality | 1.7902 %   |
| Sample fit quality    | 1.0840 %   |
| Item ID               | 0bdd6c01           |

### With Vinyl Chloride

|                              | Value        |
| ---------------------------- | ------------ |
| DI volume                    | 2.5 ml       |
| Vinyl Chloride concentration | 10 $\mu$g/ml |
| Vinyl Chloride volume        | 12 $\mu$l             |

| Time (m) | Refractive index (nD) | Sample fit (%) |
| -------- | --------------------- | -------------- |
| 4        | 2.01187869            | 3.4598         |
| 6        | 1.00000000            | 2.6243         |
| 8        | 1.59598009            | 39.3778        |
| 10       | N/A                   | N/A            |
| 12       | 1.56615758            | 7.1502         |
| 14       | 1.55402159            | 1.1353         |
| 16       | 1.27356621            | 1.5568         |
| 18       | 1.62015372            | 11.6613        |
| 20       | 1.51346925            | 0.8147         |
| 22       | 1.59685616            | 32.0183        |
| 24       | 1.78699427            | 5.9686         |
| 26       | N/A                   | N/A            |
| 28       | 1.52448131            | 13.6574        |
| 30       | 1.53031612            | 48.8465        |
| 33       | N/A                   | N/A               |


![[Pasted image 20231114201803.png]]

**Properties**

| Property | Value |
| ---------- | ----- |
| Test number |T5 |
| Vinyl Chloride volume | 12.0 ul |
| Enzyme weight | 0 ug |
| DI water volume | 2.5 ml |
| VC Concentration | 9.6 ug/ml |

**Results**

| Property | Value |
| -------- | ----- |
| RI Shift (*outliers removed*)|0.0|
| RI Shift (*moving average*) |0.0|
| Average fit quality | 14.02% |
| Standard deviation ($\sigma$) $\times 10^3$ | 234.5632 |
| Standard deviation ($\sigma$) *(last 30 minutes)* $\times 10^3$ | 94.2525 |

