# Django Web Application #
## Overview ##
Project is a visual tabular tool to store, modify and create test environments which can be easily accessed.
The purpose of this is to easily test different factors effecting customer experiences often hard to identify/reproduce.
This project does not create functioning links to the specific testing experiences as this is out of project scope. The project has been built with Django Python web framework.


## Table of Contents ##
1. Notes
2. Prerequisites
3. Installation
4. Commands for working with Django
5. Models
6. Testing
7. Admin
8. Deployment

## Notes ##
"Todo:" is used to mark non-native comments in the code and explains non-native Django project setup code.


## Prerequisites ##
Ensure the following are installed:

Python 3.x

git

## Installation ##
To set up the project locally, follow these steps:

1. Navigate to your desired project directory

2. Clone the Repository

`git clone https://github.com/pembertonf50/QA-Assignment.git`

3. Enter project folder and create virtual environment

`python -m venv env`

4. Activate the virtual environment

Windows: `.\env\Scripts\activate`

macOS/Linux: `source env/bin/activate`

5. Install dependencies from requirements.txt

`pip install -r requirements.txt`

## Commands for working with Django ##
`django-admin startproject myDjangoProject` **Not to be used and information only**. Was used to start the project setting up structure and adding Django native files. Also names the project mydjangoProject.

`python manage.py startapp <app name>` **Not to be used and information only**. Creates an app folder containing Django native files.

`python manage.py runserver` Used to check application locally. Command creates development server running on http://localhost:8000

`python manage.py migrate` Fixes common migration errors when attempting `python manage.py runserver`. Corrects the conflicts between memory stored values in models and database values.

## Models ##
Models are used to set up database schema and Django functions can make changes to the database.

`python manage.py makemigrations <app name>` Creates a script file in  *migrations* folder.

`python manage.py migrate` Runs the above generated script to make changes to the database.

`python manage.py showmigrations <app name>` Displays the generated scripts from makemigrations such as:

*0001_initial.py*

*0002_gardenmap.py*

*0003_gardenemployees.py*

`python manage.py migrate <app name> 0002` Example to remove 0003 and revert back to 0002.

## Testing ##
Tests are all stored in *testAccountExperience/tests.py*.

This is the native and intended location for unit tests.

`python manage.py test` To run tests.

## Admin ##
`python3 manage.py createsuperuser` Creates admin account. Email and username should match so authentication functions work with email.

Current stored account detail:

| Credential | POSTGRES local | Production and SQLite |
|:----------:|:--------------:|:---------------------:|
|  username  |  admin-local   |         admin         |
|   email    |  admin-local   |         admin         |
|  password  |  admin-local   |         admin         |


Admin account can login like a regular user. Admin has separate Django admin portal at /admin endpoint. From the admin portal, admin can access all the users and there associated test accounts and modify user data.

## Deployment ##
Deployment has been done on Render.

To deploy on render environment variables are used to differentiate the experience between prod and dev so debug information is only shown in development.

The following environment variables are used to create a superuser for Render:

DJANGO_SUPERUSER_USERNAME

DJANGO_SUPERUSER_EMAIL

DJANGO_SUPERUSER_PASSWORD

this shoudl not be pushed