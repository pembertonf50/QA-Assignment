from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from unittest.mock import patch
from .models import TestAccount


# Create your tests here.
class TestViews(TestCase):
  def setUp(self):
    # Todo: Client object simulates a web browser and allows you to make requests to your Django application.
    self.client = Client()
    # Todo: reverse('home') function resolves the URL based on the named URL pattern defined in your urls.py file.
    self.home_url = reverse('home')
    self.login_url = reverse('login')
    self.signup_url = reverse('signup')
    self.deleteAccount_url = reverse('deleteAccount')
    self.logout_url = reverse('logout')
    self.deleteTestAccount_url = reverse('deleteTestAccount', args=["<EMAIL>"])
    # Todo: Omitting the save() to not dirty database with test data
    self.user = User.objects.create_user(username='testuser', email='testuser', password='password')

  'home view tests'

  def test_home_GET_user_not_authenticated(self):
    client = Client()
    response = client.get(reverse('home')) # Todo: simulates a GET request on home endpoint

    self.assertEqual(response.status_code, 200) # Todo: GET was ok
    # Todo: Checks correct template
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

  def test_home_GET_user_authenticated_with_accounts(self):
    self.client.login(username='testuser', password='password') # Todo: login to authenticate user
    testAccount = TestAccount.objects.create( # Todo: Creates a test account
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

  def test_home_GET_user_authenticated_no_accounts(self):
    self.client.login(username='testuser', password='password')
    response = self.client.get(self.home_url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/homePage.html')

  def test_home_POST_user_authenticated_invalid_data(self):
    self.client.login(username='testuser', password='password')
    # Todo: nope is not a valid location or language
    data = {'location': 'nope', 'language': 'nope', 'subscriptions': ['cool'], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)

    self.assertRaises(ObjectDoesNotExist, TestAccount.objects.get, location='nope')
    self.assertEqual(response.status_code, 302) # Todo: Checks redirect response worked
    self.assertRedirects(response, '/') # Todo: Checks redirect to home endpoint

  def test_home_POST_user_authenticated_valid_data(self):
    self.client.login(username='testuser', password='password')
    # Todo: subscriptions with 1 input
    data = {'location': 'Turkey', 'language': 'Turkish', 'subscriptions': ['cool'], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)

    self.assertEqual(TestAccount.objects.get(location='Turkey').location, "Turkey")
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

    # Todo: subscriptions with no input
    data = {'location': 'Canada', 'language': 'English', 'subscriptions': [], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)

    self.assertEqual(TestAccount.objects.get(location='Canada').location, "Canada")
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

    # Todo: subscriptions with multiple input
    data = {'location': 'United Arab Emirates', 'language': 'Arabic',
            'subscriptions': ['cool', 'dead'], 'card': 'no', 'address': 'no'}
    response = self.client.post(self.home_url, data)

    self.assertEqual(TestAccount.objects.get(location='United Arab Emirates').location, "United Arab Emirates")
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  'login view tests'

  def test_login_GET(self):
    response = self.client.get(self.login_url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/logIn.html')

  def test_login_POST_invalid_data(self):
    data = {'email': 'noEmail', 'password': 'noPassword'}
    response = self.client.post(self.login_url, data)

    self.assertRaises(ObjectDoesNotExist, User.objects.get, email='noEmail')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/logIn.html')

  def test_login_POST_valid_data(self):
    data = {'email': 'testuser', 'password': 'password'}
    response = self.client.post(self.login_url, data)

    self.assertEqual(User.objects.get(email='testuser').email, 'testuser')
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  'signup view tests'

  def test_signup_GET(self):
    response = self.client.get(self.signup_url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/signUp.html')

  def test_signup_POST_invalid_data(self):
    data = {'email': 'testuser', 'password': 'password'} # Todo: Already exists data
    response = self.client.post(self.signup_url, data)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/signUp.html')

  def test_signup_POST_valid_data(self):
    data = {'email': 'testuser@gmail.com', 'password': 'somethingproper12'}
    response = self.client.post(self.signup_url, data)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  @patch('testAccountExperience.views.authenticate')  # Todo: patch changes outcome of authenticate()
  def test_signup_POST_valid_data_authentication_fails(self, mock_authenticate):
    mock_authenticate.return_value = None
    data = {'email': 'testuser@gmail.com', 'password': 'somethingproper12'}
    response = self.client.post(self.signup_url, data)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/login/')

  'delete account view tests'

  def test_deleteAccount_GET(self):
    self.client.login(username='testuser', password='password')
    response = self.client.get(self.deleteAccount_url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'testAccountExperience/deleteAccount.html')

  def test_deleteAccount_GET_user_not_authenticated(self):
    response = self.client.get(self.deleteAccount_url)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  def test_deleteAccount_POST(self):
    self.client.login(username='testuser', password='password')
    response = self.client.post(self.deleteAccount_url)

    self.assertRaises(ObjectDoesNotExist, User.objects.get, email='testuser')
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  'logout view tests'

  def test_logout_GET(self):
    self.client.login(username='testuser', password='password')
    response = self.client.get(self.logout_url)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  'delete test account view tests'

  def test_deleteTestAccount_GET(self):
    self.client.login(username='testuser', password='password')
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
    response = self.client.get(self.deleteTestAccount_url)

    self.assertEqual(TestAccount.objects.filter(testAccountOwner=self.user).count(), 0)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')

  @patch('testAccountExperience.views.TestAccount.objects.exists')
  def test_deleteTestAccount_no_account_found(self, mock_authenticate):
    mock_authenticate.return_value = False
    self.client.login(username='testuser', password='password')
    response = self.client.get(self.deleteTestAccount_url)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')