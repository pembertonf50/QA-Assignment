from django.contrib import admin
from .models import TestAccount

# Register your models here.
# code below is based off of admin.site.register(TestAccount)
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

