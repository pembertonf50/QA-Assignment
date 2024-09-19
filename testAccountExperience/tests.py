from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TestAccount
from django.core.exceptions import ObjectDoesNotExist

# Todo: most of the application gets coverage automatically because ...

"""
Then the additional comment gives an extra flavor to it:

During the test, Django has to load the classes and other modules into the memory, and hence the program (your class and settings and many other parts) get executed.

So what’s happening here, is that CBVs are classes, when you run the tests Django will load them into memory, which means that they will be executed. When I ran the coverage, it will look for “executed” code and they will appear as tested.

The Class Based View method I have overridden is not run while loading Django and that’s why it isn’t considered as tested!

"""

# Create your tests here.
class TestViews(TestCase):
  def setUp(self):
    self.client = Client() # client object simulates a web browser and allows you to make requests to your Django application.
    self.home_url = reverse('home') # reverse('home') function resolves the URL based on the named URL pattern defined in your urls.py file.
    self.user = User.objects.create_user(username='testuser', email='testuser', password='testpassword') # omitting the save to not dirty database
    # self.delete_test_account_url = reverse('delete_test_account', args=[1])
    # self.project1 = Project.objects.create(name='Test Project 1', budget=1000)

  def test_home_get_user_not_authenticated(self):
    response = self.client.get(self.home_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

  def test_home_get_user_authenticated_with_accounts(self):
    self.client.login(username='testuser', password='testpassword')
    testAccount = TestAccount.objects.create(
      email="<EMAIL>",
      password="<PASSWORD>",
      location="here",
      language="foreign",
      subscriptions="",
      cardSaved=False,
      addressSaved=False,
      experienceLink="www.yeh.com",
      testAccountOwner=self.user
    )

    response = self.client.get(self.home_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

  def test_home_get_user_authenticated_no_accounts(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(self.home_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

  def test_home_post_user_authenticated_invalid_data(self):
    self.client.login(username='testuser', password='testpassword')
    data = {'location': 'nope', 'language': 'nope', 'subscriptions': ['cool'], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)

    self.assertRaises(ObjectDoesNotExist, TestAccount.objects.get, location='nope')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

  def test_home_post_user_authenticated_valid_data(self):
    self.client.login(username='testuser', password='testpassword')

    # subscriptions with 1 input
    data = {'location': 'Turkey', 'language': 'Turkish', 'subscriptions': ['cool'], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)
    self.assertEqual(TestAccount.objects.get(location='Turkey').location, "Turkey")
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

    # subscriptions with no input
    data = {'location': 'Canada', 'language': 'English', 'subscriptions': [], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)
    self.assertEqual(TestAccount.objects.get(location='Canada').location, "Canada")
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

    # subscriptions with multiple input
    data = {'location': 'United Arab Emirates', 'language': 'Arabic', 'subscriptions': ['cool', 'dead'], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)
    self.assertEqual(TestAccount.objects.get(location='United Arab Emirates').location, "United Arab Emirates")
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')


    '''!!!! The login view tests !!!!'''