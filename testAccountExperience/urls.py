from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logIn, name='login'),
    path('signup/', views.signUp, name='signup'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('newPassword/', views.newPassword, name='newPassword'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),

]

# Todo: This is where you add the paths pattens to access the different view functions