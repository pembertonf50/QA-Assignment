from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
def home():
  template = loader.get_template("testAccountExperience/homePage.html")
  return HttpResponse(template.render())


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
#
# def home(request):
#   context = {"name": "Spot"}
#   return HttpResponse(template.render(context))
#   return render(request, "vetoffice/home.html", con