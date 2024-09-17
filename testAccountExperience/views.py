from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import loader
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
  # Todo: refresh creates duplicate accounts and this should be happening
  # Todo: make sure to log errors
  # template used "testAccountExperience/homePage.html"
  user = request.user
  accounts = dummyAccounts

  if request.method == 'POST' and user.is_authenticated:
    testAccountLocation = request.POST['location'] # Todo: need to make sure this calm from list
    testAccountLanguage = request.POST['language'] # Todo: need to make sure this calm from list
    testAccountSubscriptions = request.POST.getlist('subscriptions')
    testAccountCardSaved = request.POST['card'] == "yes"
    testAccountAddressSaved = request.POST['address'] == "yes"

    # This supplies middle end validation
    if country_iso_codes.get(testAccountLocation) and testAccountLanguage in languages:

      planType = urlPlanType(testAccountSubscriptions)

      TestAccount.objects.create(
        email=generateUniqueEmail(TestAccount),
        password=Faker().password(),
        location=testAccountLocation,
        language=testAccountLanguage,
        subscriptions=stringifySubscriptions(testAccountSubscriptions),
        cardSaved=testAccountCardSaved,
        addressSaved=testAccountAddressSaved,
        experienceLink=f"www.virtualmachine-{planType}{country_iso_codes[testAccountLocation].lower()}.com",
        testAccountOwner=user
      ).save()

    else:
      print("need select a value from the lists")

  if user.is_authenticated:
    userEmail = User.objects.get(email=user.email)
    testAccounts = TestAccount.objects.filter(testAccountOwner=user)
    if testAccounts:
      accounts = listifySubscriptions(testAccounts)
    context = {"accounts": accounts, "subscriptions": subscriptions, "locations": locations, "languages": languages, "userEmail": userEmail, "loggedIn": user.is_authenticated}
    return render(request, "testAccountExperience/homePage.html", context)
  context = {"accounts": accounts, "subscriptions": subscriptions, "locations": locations, "languages": languages}
  return render(request, "testAccountExperience/homePage.html", context)

def logIn(request):
  if request.method == 'POST':
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    # Check if a user is verified and authenticated
    if user is not None:
      # Use the returned user object in login()
      login(request, user)
      # Redirect to home page after logging in
      return redirect("home")
    else:
      print("The credentials entered are incorrect")
  return render(request, "testAccountExperience/logIn.html")

def signUp(request):
  if request.method == 'POST':
    issues = False
    email = request.POST['email']
    password = request.POST['password']
    # if and try blocks below makes sure that our form submission
    # was valid with proper email and passwords
    if User.objects.filter(email=email).exists():
        issues = True
        print("email already exists")
    try:
      validate_email(email)
    except ValidationError as e:
      issues = True
      print("bad email, details:", e)

    try:
      validate_password(password)
    except ValidationError as e:
      issues = True
      print("bad email, details:", e)

    if not issues:
      User.objects.create_user(username=email, email=email, password=password).save()
      userAuthenticated = authenticate(request, username=email, password=password)
      if userAuthenticated is not None:
        login(request, userAuthenticated)
        return redirect("home")
      else:
        return redirect("login")
  return render(request, "testAccountExperience/signUp.html")

def deleteAccount(request):
    if request.user.is_authenticated and request.method == "POST":
        User.objects.filter(email=request.user.email).delete()
        return redirect("home")
    context = {"userEmail": request.user.email}
    return render(request, "testAccountExperience/deleteAccount.html", context)

def logOut(request):
    logout(request)
    return redirect("home")

def deleteTestAccount(request, templateEmail):
  if request.user.is_authenticated:
    # Q allows use to filter based on 2 or more conditions
    testAccountToDelete = TestAccount.objects.filter(Q(email=templateEmail) & Q(testAccountOwner=request.user))
    testAccountToDelete.delete()
  return redirect("home")


# Todo: consider deleting
def forgotPassword(request):
  template = loader.get_template("testAccountExperience/forgotPassword.html")
  return HttpResponse(template.render())

def newPassword(request):
  template = loader.get_template("testAccountExperience/newPassword.html")
  return HttpResponse(template.render())