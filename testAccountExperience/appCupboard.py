# Todo: This file is used to remove complex logic from views and models

import faker

def stringifySubscriptions(subscriptionsList): # Todo: models can't take list objects so needs converting to string
  return ', '.join(subscriptionsList)

def listifySubscriptions(querySet): # Todo: Converts the model stored subscriptions back to list
  for obj in querySet:
    obj.subscriptions = obj.subscriptions.split(', ') # Todo: .save() not used so no changes are done in database
  return querySet

def urlPlanType(lst): # Todo: Creates plantype text in virtual environment link
  if len(lst) == 0:
    return ""
  elif len(lst) == 1:
    return lst[0].lower() + "-"
  else:
    return "multiplan-"

def proccessTuplesForModels(tup): # Todo: Example output (('Portuguese', 'Portuguese'), ('English', 'English'), ...)
  modelReadyTuple = ()            #  used in to make sure values stored in database come from tuple
  for s in tup:
    modelReadyTuple += ((s, s),)
  return modelReadyTuple

def createLocationsTuple(dic): # Todo: Used to create tuple from country_iso_codes from 1 source of truth
  locationsTuple = ()
  for s in dic.keys():
    locationsTuple += (s,)
  return locationsTuple

def generateUniqueEmail(model): # Todo: Generates a unique test email address for a given User model.
    fake = faker.Faker()
    while True:
        email = fake.email()
        if not model.objects.filter(email=email).exists():
            return email

dummyAccounts = [{"email": "example@gmail.com",
               "password": "123456",
               "location": "united kingdom",
               "language": "english",
               "subscriptions": ["something"],
               "cardSaved": True,
               "addressSaved": False,
               "experienceLink": "www.example.com"}]

country_iso_codes = {
    "Argentina": "AR",
    "Australia": "AU",
    "Austria": "AT",
    "Barbados": "BB",
    "Belgium": "BE",
    "Brazil": "BR",
    "Canada": "CA",
    "Chile": "CL",
    "Colombia": "CO",
    "Denmark": "DK",
    "France": "FR",
    "Germany": "DE",
    "Hungary": "HU",
    "India": "IN",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Italy": "IT",
    "Japan": "JP",
    "Kenya": "KE",
    "Luxembourg": "LU",
    "Malaysia": "MY",
    "Mexico": "MX",
    "Netherlands": "NL",
    "New Zealand": "NZ",
    "Nigeria": "NG",
    "Norway": "NO",
    "Peru": "PE",
    "Philippines": "PH",
    "Poland": "PL",
    "Paraguay": "PY",
    "Romania": "RO",
    "Saudi Arabia": "SA",
    "Singapore": "SG",
    "Spain": "ES",
    "Sweden": "SE",
    "Switzerland": "CH",
    "Taiwan": "TW",
    "Thailand": "TH",
    "Turkey": "TR",
    "United Arab Emirates": "AE",
    "United Kingdom": "GB",
    "United States": "US",
    "Vietnam": "VN",
    "South Africa": "ZA"
}

locations = createLocationsTuple(country_iso_codes)

languages = (
  'Portuguese', 'English', 'Swedish',
  'Vietnamese', 'Malay', 'Danish',
  'Arabic', 'Turkish', 'French',
  'Dutch', 'Mandarin Chinese', 'Luxembourgish',
  'Japanese', 'Indonesian', 'Guaraní',
  'Hindi', 'Hungarian', 'Polish',
  'German', 'Romanian', 'Italian',
  'Tagalog', 'Spanish', 'Thai',
  'Norwegian'
)

subscriptions = ("PrimeVideo", "Prime", "HBO", "Paramount+")
