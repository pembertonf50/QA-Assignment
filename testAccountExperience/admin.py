from django.contrib import admin
from .models import TestAccount

# Register your models here.
# Todo: Code below is based off of admin.site.register(TestAccount)
#   list_display allows you to see all the fields more clearly in /admin endpoint
@admin.register(TestAccount)
class TestAccountAdmin(admin.ModelAdmin):
  list_display = (
    "id",
    "email",
    "password",
    "location",
    "language",
    "subscriptions",
    "cardSaved",
    "addressSaved",
    "experienceLink",
    "testAccountOwner"
  )
