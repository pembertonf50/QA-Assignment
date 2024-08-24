from django.http import HttpResponse
from django.template import loader

""" Example syntax
def home(request):
  context = {"name": "Junior"}
  template = loader.get_template("app/home.html")
  return HttpResponse(template.render(context))
"""

# Create your views here.

def home(request):
  template = loader.get_template("testAccountExperience/homePage.html")
  context = {"answer": "yes"}
  return HttpResponse(template.render(context))


