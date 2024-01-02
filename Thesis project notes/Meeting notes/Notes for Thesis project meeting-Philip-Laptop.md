---
date: 2023-08-10
---

Bachelor thesis here.

Upcoming project with region and a company called DMR
DMR
- Consultants to the region, they take water samples. They want to try *our* water and see how it performs.

Any specific requirements?

Water care guard (https://www.watercareguard.com/)
- Make water analysis available in the field
- A suitcase for making samples in the field
- When putting the sample into the suitcase everything is handled in *Spectroworks* which is made for a lot of different spectrometers.
	- Our suitcase only has a single spectrometer
	- They are using Python as an API

- Spectroworks is an app with a frontend and a backend
	- The database is in the cloud (backend)
	- The code for the backend is in Python
- We want to make it simpler and more customized, so you don't have to go through the entire spectroworks.
- We are going to ask for the data from spectroworks
	- This communication is done via APIs
	- We have access to a sample APIs
	- We would like to get more endpoints
- Using this we are going to build our own app.

Roana will send a paper draft going over what we have so far. It is not published yet, so keep it confidential.

Spectroworks is from copenhagen nano systems
- Simplify so the user only have the needed information.
	- How much minochlorite there is in the sample.
	- Spectroworks is for more advanced, we want to simplify the interface.

When you come to SDU you should see the whole solution.

Right now we describe what would be the next step in the evolution of the prototype. Make it easier to use by a user client.
It is programming on a higher level of abstraction. Meant to work on an operating system, mobile device.

The kind of task of knowledge it requires.
- Backend programming
- Content programming
- The content you do with the suitcase is a step up from embedded programming.
- It is not a must that the programming must be done in Python.
- In embedded you use C/C++

I don't know what you would like to present for your thesis.
If you want to add something?

It is not a must that you do the entire thing, maybe you can do something that is closer to your profile as a mechatronics guy.

The app is about web development, not much about Mechatronics, maybe machine learning.

You have to know some knowledge about method requests, database.

Those would be the skills.
I don't see any particular relevant mechanical stuff.
Maybe if you want to add something?

The first *work package* would be to go to the lab and try and use the lab. and built some data points.
We need some more data to built a more robust database.
We need some experiments that show the same points for a concrete database

The second step could be to try to simplify the interface.

Meeting about the REST api endpoints.
- What do we want, do we need some write access and not only read access?
- Meeting with CBS
- So they don't open up too much so we can't *damage* something.

The calculation of monochlorite.
- We would measure the precise concentration from the lab.
- You do some serious of experiments where you are adding a known concentration and see the response and you built a table where you can see a correlation.
- Then you have a robust database.
- Then you have an output 2+- 2ppm e.g.
- You will have an error bar.
- Don't rely on anything from CBS, we can built our own database, we have some data but we need more.

Write the short document for the introduction into what you would do for the Thesis and sent it to Roana and let her look through it.

We will start from the 1st of September and have some weekly meetings. (Maybe Monday the 4th instead?)