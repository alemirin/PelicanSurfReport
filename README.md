# Final Project Report

* Student Name: Alejandro Miranda
* Github Username: alemirin
* Semester: Fall 2023
* Course: CS5001



## Description
General overview of the project, what you did, why you did it, etc.

• The project's aim is to take raw data from the National Data Buoy Center (NOAA) and display the data that surfers would find important/ relevant in a neat and concise way.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on.

• The project reads the raw buoy data and extracts the relevant information in order to concisely portray the information to surfers. I am proud of my use of classes to neatly separate the buoy data into types of data and read the websites to organize the important data so that it is easy to display and connect to the html script.


## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.

• Once all of the things are downloaded, open a terminal window at the directory where surfapp.py, buoydatareader.py and the static and templates folder are located and run the webpage within terminal using python3 surfapp.py. Once the terminal gives a message that the app is running on your IP address, go to your browser on the device and access the webpage using the url localhost:5000 . I've also included screenshots of how the page appeared on my device. You can also access the data for San Juan by adding "/sanjuan" to the localhost url.



## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

• To run the project, you must download all of the files in the Github repository and make sure to download flask using pip install flask. Something that I had to do to get the webpage with real time data capture to work was go in Mac to Applications > Python > CertificatesInstall.command.


## What's Next
There's still much to do with this, naturally I can continue adding locations to the webpage, and add a navigation bar that displays different beaches or areas from which to gather buoy data. Also, I could add more specific beach locations and offer information on how deep the water is, what the ground below the water is like (sand, reef, cobblestones, etc.), information on currents, and much more. Also, I hoped to implement a user system and this way users can favorite locations or get alerts when preferred conditions arise. Also, the forecast data could be implemented to see how the conditions will change in the future.

