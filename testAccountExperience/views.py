from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from .models import TestAccount


def stringifySubscriptions(subscriptionsList):
  return ', '.join(subscriptionsList)

def listifySubscriptions(querySet):
  for obj in querySet:
    obj.subscriptions = obj.subscriptions.split(', ')

  return querySet

# Create your views here.
def home(request):
  # template used "testAccountExperience/homePage.html"
  user = request.user

  accounts = [{"email": "faker1@gmail.com",
               "password": "123456",
               "location": "united kingdom",
               "language": "english",
               "subscriptions": [],
               "card": "yes",
               "address": "yes",
               "experiences": "http://www.faker1.com"}]

  if request.method == 'POST' and user.is_authenticated:
    testAccountLocation = request.POST['location']
    testAccountLanguage = request.POST['language']
    testAccountSubscriptions = request.POST['subscriptions']
    testAccountCardSaved = request.POST['card'] == "yes"
    testAccountAddressSaved = request.POST['address'] == "yes"

    TestAccount.objects.create(
      email="thisemailneedssort@gmail.com",
      password="password",
      location=testAccountLocation,
      language=testAccountLanguage,
      subscriptions=stringifySubscriptions(testAccountSubscriptions),
      cardSaved=testAccountCardSaved,
      addressSaved=testAccountAddressSaved,
      experienceLink="www.fakerfromdatabase.com",
      testAccountOwner=user
    ).save()

  if user.is_authenticated:
    userEmail = User.objects.get(email=user.email)
    testAccounts = TestAccount.objects.filter(testAccountOwner=user)
    print(testAccounts)
    print(type(testAccounts))
    print("print something afterwards")
    if testAccounts:
      accounts = listifySubscriptions(testAccounts)
    context = {"accounts": accounts, "userEmail": userEmail, "loggedIn": user.is_authenticated}
    return render(request, "testAccountExperience/homePage.html", context)


  context = {"accounts": accounts}
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
  return render(request, "testAccountExperience/logIn.html")

def signUp(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(email=email).exists():
        print("email already exists")
        return render(request, "testAccountExperience/signUp.html")
    User.objects.create_user(username=email, email=email, password=password).save()
    userAuthenticated = authenticate(request, username=email, password=password)
    if userAuthenticated is not None:
      login(request, userAuthenticated)
      return redirect("home")
  return render(request, "testAccountExperience/signUp.html")

def forgotPassword(request):
  template = loader.get_template("testAccountExperience/forgotPassword.html")
  return HttpResponse(template.render())

def newPassword(request):
  template = loader.get_template("testAccountExperience/newPassword.html")
  return HttpResponse(template.render())

def deleteAccount(request):
    if request.user.is_authenticated and request.method == "POST":
        User.objects.filter(email=request.user.email).delete()
        return redirect("home")
    context = {"userEmail": request.user.email}
    return render(request, "testAccountExperience/deleteAccount.html", context)

def logOut(request):
    logout(request)
    return redirect("home")
