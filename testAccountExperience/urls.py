from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# Todo: This is where you add the paths pattens to access the different view functions