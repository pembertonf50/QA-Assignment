from django.db import models
from django.contrib.auth.models import User

'''class Patient(models.Model):
  breed = models.CharField(max_length=200)
  pet_name = models.CharField(max_length=200)
  age = models.IntegerField(default=0)
  # Add your code below:
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
  
  class Flower(models.Model):
  COLOR_CHOICES = [
     ("R", "Red"),
     ("Y", "Yellow"),
     ("P", "Purple"),
     ("O", "Other"),
  ]
  
  color = models.CharField(max_length=1, choices=COLOR_CHOICES)
  
'''
# Create your models here.
'''
User Model This is a built in model which can be used to generate users
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
    locationChoices = [(), ()]
    languageChoices = [(), ()]
    subscriptionsChoices = [("prime", "Prime"), ()]
    # these choices are used to autogen a dropdown in django forms
    # Todo: Look into how to do this with Django forms
    #       location = models.CharField(max_length=200, choices=locationChoices)
    # Todo: Consider how you can arrange subscriptions list so that there's not
    #    many options using sort for example

    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    subscriptions = models.CharField(max_length=200)
    cardSaved = models.BooleanField(default=False)
    addressSaved = models.BooleanField(default=False)
    experienceLink = models.URLField(max_length=200)
    testAccountOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    # 'on_delete=models.CASCADE' ensures that TestAccount is/are deleted
    # when User is deleted

    # Todo: methods below maybe redundant is Postgres is used as it has
    #       in built list handling
