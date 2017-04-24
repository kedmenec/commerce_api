from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):

    def _create_account_and_login(self):
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
        return response

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

    def _create_product(self):
        url = '/products/'
        data = {
            "title": "Tuna",
            "price": 302.0,
            "colour": "violet",
            "category": "Tools",
            "image": "http://lorempixel.com/640/480/nature",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['id']

    def test_add_review(self):
        resp = self._create_account_and_login()
        token = resp.data['key']
        self.client.credentials(HTTP_AUTHORIZATION='Token {token}'.format(token=token))
        product_id = self._create_product()
        url = '/reviews/'
        data = {
            'product': product_id,
            'text': 'very good',
            'rating': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the review is on the product
        url = '/products/'
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data['results'][0]['reviews']), 1)

        url = '/reviews/{review_id}/'.format(review_id=response.data['results'][0]['reviews'][0])

        response = self.client.get(url, format='json')
        self.assertEqual(response.data['text'], data['text'])




