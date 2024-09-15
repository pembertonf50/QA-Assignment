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

Models are used to setup database schema and commands can be used to run the necessary sql commands:
python3 manage.py makemigrations <app name> // this will create a script to be run in migrations folder

python3 manage.py migrate // this command is used to run the generated script to make changes to the database schema

python3 manage.py showmigrations <app name> // this is used to display the generated scripts from makemigrations such as:
0001_initial.py
0002_gardenmap.py
0003_gardenemployees.py

python3 manage.py migrate <app name> 0002 // this would remove 0003 and revert back to 0002



## Usage ##
Provide instructions on how to use the application. This might include:

How to access the web application
Basic navigation and functionality
How to perform common tasks
Configuration
List any environment variables or configuration settings that need to be configured. For example:


## Testing ##
Instructions for running tests:

## Admin ##
username admin
email admin@dummyemail.com
password admin
