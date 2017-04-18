from rest_framework import status
from rest_framework.test import APITestCase
# from myproject.apps.core.models import Account

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account and login
        """
        url = '/rest-auth/registration/'
        data = {
            'username': 'tim',
            'password1': 'q1w2e3r4',
            'password2': 'q1w2e3r4',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = '/rest-auth/login/'
        data = {
            'username': 'tim',
            'password': 'q1w2e3r4'
        }
        response = self.client.post(url, data, format='json')
        self.assertIn('key', response.data)
