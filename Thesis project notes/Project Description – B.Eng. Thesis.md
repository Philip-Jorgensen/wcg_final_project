# Background:

In many different areas humans produce waste, whether that is as an individual or industry. Some of these waste products end up in the water and contaminate it. One of the most toxic waste products that can end up in the water is vinyl chloride (VC), one of the primary areas VC is found, is in the process of producing PVC. Vinyl chloride is highly volatile, making it hard to detect, which has created a need for a fast and simple solution for detecting the concentration of VC in water.

This has led the company Water Care Guard to develop an on-site lab kit that fits in a suitcase, which is able to test a water sample for the concentration of VC among other substances.

This project is done in collaboration with Roana from SDU Nano Syd and Water Care Guard.

# Problem:

The main thing with the project is going to be improving upon the suitcase lab, both hardware and software, as well as adding to the database and finding a correlation between the input and the response of the data.

The first work package would be to go to the lab and use the lab suitcase to gather more data points, to make the database more robust. Making the database more robust will aid in making it more accurate at estimating the contents of the water sample.

I would be doing some experiments where I am adding a known quantity of a monochloride like VC, and measuring the response, and comparing that response to the quantity added to the sample. The more data points I gather, the more reliable the correlation between the response and the quantity added will be.

 The second work package is to simplify the user interface of the suitcase laboratory. This involves both backend and frontend programming in Python and embedded C/C++. The programming that will be used throughout the project is on a higher level of abstraction, it is meant to work on an operating system like a mobile device.  The suitcase lab is working with an external software which houses the database in their cloud, we would be communicating with it through a REST API. This external software is more advanced and not targeted towards a person without a scientific background, so the software needs to be simplified to be more usable by an average person, when they are out in the field testing a water sample.

Simplifying the user interface is not only about the software part of it, but it could also involve the suitcase itself, and find ways to make it easier to use in both the hardware and software aspects.