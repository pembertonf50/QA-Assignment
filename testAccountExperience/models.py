from django.db import models
from django.contrib.auth.models import User
from .appCupboard import locations, languages, proccessTuplesForModels

# Create your models here.
'''
User Model is a built in model which can be used to generate users
Fields:
username: A unique username for the user.
password: A hashed password for the user.
first_name: The user's first name.
last_name: The user's last name.
email: The user's email address.
is_active: A boolean indicating whether the user is active.
is_staff: A boolean indicating whether the user is a staff member.
is_superuser: A boolean indicating whether the user is a superuser.
date_joined: The date and time the user was created.

Methods:
check_password(raw_password): Verifies if the provided raw password matches the user's stored hashed password.
get_full_name(): Returns the user's full name.
get_short_name(): Returns the user's username.
has_perm(perm): Checks if the user has the specified permission.
has_perms(perm_list): Checks if the user has all of the specified permissions.
has_module_perms(app_label): Checks if the user has permissions for the specified app.
'''

class TestAccount(models.Model):
    # Todo: The use of unique and choices keyword parameters provides backend validation.
    #   choices enforces that location/languages is from tuple lists
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    location = models.CharField(max_length=200, choices=proccessTuplesForModels(locations))
    language = models.CharField(max_length=200, choices=proccessTuplesForModels(languages))
    subscriptions = models.CharField(max_length=200)
    cardSaved = models.BooleanField(default=False)
    addressSaved = models.BooleanField(default=False)
    experienceLink = models.URLField(max_length=200)
    testAccountOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Todo: 'on_delete=models.CASCADE' ensures that TestAccount is/are deleted when User is deleted
