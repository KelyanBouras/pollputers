from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from views import SignUpView


class SignUpViewTestCase(TestCase):
    def test_SignUpView(self):
        # Define the test user's credentials
        username = 'testuser'
        password = 'testpassword'
        email = 'testuser@example.com'

        # Send a POST request to the SignUpView view with the test user's credentials
        response = self.client.post(reverse('SignUpView'), {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email,
        })

        # Check that the SignUpView was successful
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertTrue(User.objects.filter(username=username).exists())  # User should exist in the database

        # Attempt to log in with the test user's credentials
        login_response = self.client.post(reverse('login'), {
            'username': username,
            'password': password,
        })

        # Check that the login was successful
        self.assertEqual(login_response.status_code, 302)  # Should redirect to the home page
        self.assertTrue(login_response.wsgi_request.user.is_authenticated)  # User should be authenticated
