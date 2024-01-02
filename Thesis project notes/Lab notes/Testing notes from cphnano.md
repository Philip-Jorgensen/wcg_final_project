---
date: 2023-09-14
type: lab_notes
subject: Thesis project
tags: 
Device: USB 650 UV
---
## Files
**Email response from CPHNANO**
Hi Philip.

It seems that there is a lot of noise on your spectrum.

Are you using SpectroLink™? If so you can take the following steps to reduce noise:

- Start by turning on the lamp/light source, set the number of averages to 1 and, without anything in the cuvette holder, click on "Auto" to automatically set the integration time to the optimal value.
- Now increase the number of averages until the noise is minimized. A good value is 50-100.
- Click "Measure" next to "Light source spectrum".
- Use a black block to block out the light or turn off the lamp. Click "Measure" next to "Background spectrum".
- Once you have a good light source and background spectrum you can now start capturing attenuance spectra.
- Add your NanoCuvette and capture a spectrum. Your spectrum should be nice and smooth with very little noise. If your spectrum is still noisy increase the number of averages and try again. Note that you have to measure light source and background spectrum again when changing the number of averages.

Let me know if that solves your problem.

Best regards,

Thomas

## Notes

Reference measurement
![[Pasted image 20230914120846.png]]
![[Pasted image 20230914120910.png]]

Tried with a different cuvette
![[Pasted image 20230914130317.png]]

Trying the tips from cphnano hasn't resolved the issue, the best result that I got was 23% fit quality which is too low, and I was not able to replicate this score.

**Possible causes for the problem**
- Problem with the cuvettes
	- Although I tried multiple cuvettes from the same box
- Not pure water, Distilled water not deionized.
- Problem with the calibration of the spectrolink
	- Although I followed the tips from cphnano