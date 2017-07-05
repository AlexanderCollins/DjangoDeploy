# DjangoDeploy                                                                              [![Build Status](https://travis-ci.com/AlexanderCollins/DjangoDeploy.svg?token=npni315gymyQYezKVkZU&branch=master)](https://travis-ci.com/AlexanderCollins/DjangoDeploy)
DjangoDeploy is a collection of bash scripts which can be used to deploy your django application onto a remote Ubuntu16.04 server with gunicorn and nginx. 
This repository is not a full proof solution and is only intended to speed up the tedious nature of deploying a django rest_framework application.

# Getting Started
1. Clone this repository onto your development/production server using a non root sudo user.

$ ```git clone https://www.github.com/alexandercollins/djangodeploy.git```

3. Change directory to ~/django deploy

$ ```cd djangodeploy```

3. Run the setup file

$ ```./setup.py```


# Dont forget to place 'SERVERIPADDRESS' as a string in your django project settings.py file for CORS and ALLOWED_HOSTS to be set correctly.


# Running Tests
To run tests call setup.py within the djangodeploy/ folder.

$ ```./setup.py```

# DjangoDeploy's Future
In the future I'd like to see this repo used to deploy django applications remotely, integrating into Amazon Web Services, DigitalOcean and Microsoft Azure open APIs.
I'd also like to add more support for nodejs applications. This is my first public repository.
