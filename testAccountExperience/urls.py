# Todo: This file is where you add the paths pattens to access the different view functions

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logIn, name='login'),
    path('signup/', views.signUp, name='signup'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    path('logout/', views.logOut, name="logout"),
    path('deleteTestAccount/<str:templateEmail>', views.deleteTestAccount, name='deleteTestAccount'),
]
