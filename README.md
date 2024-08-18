### Django Web Application ###
## Overview ##
Project is a visual tabular project to store, modify and create test environments which can be easily accessed.
The purpose of this is to easily test different countries and customer types experience under set conditions as it can be hard to identify/reproduce existing experiences.
The project has been on Django Python web framework.


## Table of Contents ##
Prerequisites
Installation
Usage
Configuration
Testing
Deployment
Contributing
License
Acknowledgements

## Prerequisites ##
Before you begin, ensure you have met the following requirements:

Python 3.x
Django 3.x or later

## Installation ##
To set up the project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/pembertonf50/QA-Assignment.git
cd your-repository
Create a Virtual Environment:

bash
Copy code
python -m venv env


Activate the Virtual Environment:

On Windows:
bash
Copy code
.\env\Scripts\activate

On macOS/Linux:
bash
Copy code
source env/bin/activate

Installed Dependencies should be saved to requirements.txt

bash
Copy code

windows: pip install -r requirements.txt

mac: pip3 install -r requirements.txt

## Setup the project ##
Commands:

django-admin startproject djangoProject // this will start a project setting up structure and adding necessary files. Also names the project djangoProject

python3 manage.py runserver // this setups up a development server running on http://localhost:8000

python3 manage.py migrate // used to configure the django database if migrations errors occur.

python3 manage.py startapp <app name> // creates an app folder containing files related 


## Usage ##
Provide instructions on how to use the application. This might include:

How to access the web application
Basic navigation and functionality
How to perform common tasks
Configuration
List any environment variables or configuration settings that need to be configured. For example:


## Testing ##
Instructions for running tests:

