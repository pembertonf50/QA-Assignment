from django.db import models

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
class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    loggedIn = models.BooleanField(default=False)

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
    def setSubscriptions(self, subscriptionsList):
        self.subscriptions = ','.join(subscriptionsList)

    def getSubscriptions(self):
        return self.subscriptions.split(',')