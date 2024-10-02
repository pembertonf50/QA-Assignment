from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from faker import Faker
from .models import TestAccount
from .appCupboard import stringifySubscriptions, listifySubscriptions, subscriptions, locations, languages, \
  dummyAccounts, generateUniqueEmail, country_iso_codes, urlPlanType


# Create your views here.
def home(request):
  user = request.user
  accounts = dummyAccounts

  if request.method == 'POST' and user.is_authenticated:
    testAccountLocation = request.POST['location']
    testAccountLanguage = request.POST['language']
    testAccountSubscriptions = request.POST.getlist('subscriptions')
    testAccountCardSaved = request.POST['card'] == "yes"
    testAccountAddressSaved = request.POST['address'] == "yes"

    # Todo: This supplies middle-end validation
    if country_iso_codes.get(testAccountLocation) and testAccountLanguage in languages:
      planType = urlPlanType(testAccountSubscriptions)

      TestAccount.objects.create(
        email=generateUniqueEmail(TestAccount), # Todo: appCupboard.py has documentation
        password=Faker().password(), # Todo: Creates fake password
        location=testAccountLocation,
        language=testAccountLanguage,
        subscriptions=stringifySubscriptions(testAccountSubscriptions),  # Todo: appCupboard.py has documentation
        cardSaved=testAccountCardSaved,
        addressSaved=testAccountAddressSaved,
        experienceLink=f"www.virtualmachine-{planType}{country_iso_codes[testAccountLocation].lower()}.com",
        testAccountOwner=user
      ).save()

    else:
      messages.error(request, "Need to select a value from Account location and Account language")

    # Todo: the use of redirect stops multiple POST submission which duplicates account creation on refresh
    return redirect('home')

  if user.is_authenticated:
    userEmail = User.objects.get(email=user.email)
    testAccounts = TestAccount.objects.filter(testAccountOwner=user)
    if testAccounts:
      accounts = listifySubscriptions(testAccounts)  # Todo: appCupboard.py has documentation
    context = {"accounts": accounts, "subscriptions": subscriptions, "locations": locations, "languages": languages,
               "userEmail": userEmail, "loggedIn": user.is_authenticated}
    return render(request, "testAccountExperience/homePage.html", context)
  context = {"accounts": accounts, "subscriptions": subscriptions, "locations": locations, "languages": languages}
  return render(request, "testAccountExperience/homePage.html", context)
  # Todo: render() displays the chosen template such as homePage.html to the user. context is used to pass data to
  #   template

def logIn(request):
  if request.method == 'POST':
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    # Todo: Check if a user is verified and authenticated
    if user is not None:
      login(request, user)
      return redirect("home")
    else:
      messages.error(request, "Cannot find account with these login credentials")
  return render(request, "testAccountExperience/logIn.html")

def signUp(request):
  if request.method == 'POST':
    valid = True
    email = request.POST['email']
    password = request.POST['password']
    # Todo: if/try blocks below makes sure that our form submission
    #   has valid email and passwords
    if User.objects.filter(email=email).exists():
        valid = False
        messages.error(request, "Email already registered")
    try:
      validate_email(email)
    except ValidationError as e:
      valid = False
      messageString = "Bad email, details: " + str(e)
      messages.error(request, messageString)
    try:
      # Todo: validate_password() checks common passwords, similar to user properties, not completely numeric and
      #  minimum 9 characters long
      validate_password(password)
    except ValidationError as e:
      valid = False
      messageString = "Bad password, details: " + str(e)
      messages.error(request, messageString)

    if valid:
      User.objects.create_user(username=email, email=email, password=password).save()
      userAuthenticated = authenticate(request, username=email, password=password)
      if userAuthenticated is not None:
        login(request, userAuthenticated)
        return redirect("home")
      else:
        return redirect("login")
  return render(request, "testAccountExperience/signUp.html")

def deleteAccount(request):
    if not request.user.is_authenticated:
      return redirect("home")
    if request.user.is_authenticated and request.method == "POST":
        User.objects.filter(email=request.user.email).delete()
        return redirect("home")
    context = {"userEmail": request.user.email}
    return render(request, "testAccountExperience/deleteAccount.html", context)

def logOut(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect("home")

def deleteTestAccount(request, templateEmail):
  if request.user.is_authenticated:
    # Todo: Q allows filter based on 2 or more conditions
    testAccountToDelete = TestAccount.objects.filter(Q(email=templateEmail) & Q(testAccountOwner=request.user))
    if testAccountToDelete.exists():
      testAccountToDelete.delete()
  return redirect("home")
