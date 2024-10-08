### Django Web Application ###
## Overview ##
Project is a visual tabular tool to store, modify and create test environments which can be easily accessed.
The purpose of this is to easily test different countries and customer types experience under set conditions as it can be hard to identify/reproduce existing experiences.
The purposes of this project is not to create the virtual environment required to enter experience but to enable new accounts to be created which would be used in these environments.
The is the scope of the project.
The project has been build with Django Python web framework.


## Table of Contents ##
Prerequisites

Installation

Setup the project

Models

Usage

Testing

Admin

Deployment


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

python3 manage.py migrate // used to sync/cleanup the conflicts between memory stored values in models and database saved values. Used if migrations errors occur.

python3 manage.py startapp <app name> // creates an app folder containing files related 

## Models ##
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
User are first taken to home screen where they can then navigate to login/signup.
Home screen by default shows the overall feel of the tool to effectively explain how it is use.
After login, user will be redirected to home where they can begin making test accounts.

when using admin account you can login using credential below like a regular user. You can also make use of the admin functionality by going to /admin endpoint. By login here you have access to all the users and there associated test accounts with the privilege to delete them.

## Testing ##
Test are all stored in testAccountExperience/tests.py
This is the native and intended way to create and store tests for simplicity.

All view functions have been tested and 100% coverage has been achieved for this application.
Test can be run using python3 manage.py test or by running the testAccountExperience/tests.py in PyCharm.

The reason why full coverage when only testing 1 files, is due to the following:

During a test, Django has to load the classes and other modules into the memory, and hence the program (your class and settings and many other parts) get executed.

So what’s happening here, is that CBVs are classes, when you run the tests Django will load them into memory, which means that they will be executed. When running the coverage, it will look for “executed” code and they will appear as tested.




## Admin ##
to create an admin account use the following command:

python3 manage.py createsuperuser


current stored account detail:

username: admin

email: admin@dummyemail.com

password: admin


## Deployment ##
Deployment has been done on Render.

In order to deploy on render environment variables have been used to differiente the experience between prod and development such the use of DEBUG and SECRET_KEY for security reasons.

In Django, there are has built-in support for creating a superuser through environment variables.

The following can be used to create superuser for site:

DJANGO_SUPERUSER_USERNAME

DJANGO_SUPERUSER_EMAIL

DJANGO_SUPERUSER_PASSWORD