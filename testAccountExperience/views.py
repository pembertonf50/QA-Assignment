from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
  template = loader.get_template("testAccountExperience/homePage.html")
  accounts = [
    {"email": "faker1@gmail.com",
     "password": "123456",
     "location": "united kingdom",
     "language": "english",
     "subscriptions": [],
     "card": "yes",
     "address": "yes",
     "experiences": "http://www.faker1.com"},

    {"email": "faker2@gmail.com",
     "password": "123456",
     "location": "france",
     "language": "french",
     "subscriptions": ["prime"],
     "card": "no",
     "address": "no",
     "experiences": "http://www.faker2.com"}
  ]
  userInfo = {"loggedIn": True, "email": "randomEmail@outlook.com", "password": "<PASSWORD>" }
  context = {"accounts": accounts, "userInfo": userInfo}
  return HttpResponse(template.render(context))

def logIn(request):
  template = loader.get_template("testAccountExperience/logIn.html")
  return HttpResponse(template.render())

def signUp(request):
  template = loader.get_template("testAccountExperience/signUp.html")
  return HttpResponse(template.render())

def forgotPassword(request):
  template = loader.get_template("testAccountExperience/forgotPassword.html")
  return HttpResponse(template.render())

def newPassword(request):
  template = loader.get_template("testAccountExperience/newPassword.html")
  return HttpResponse(template.render())

def deleteAccount(request):
    template = loader.get_template("testAccountExperience/deleteAccount.html")
    userInfo = {"loggedIn": True, "email": "randomEmail@outlook.com", "password": "<PASSWORD>"}
    context = {"account": userInfo}
    return HttpResponse(template.render(context))