from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthTokenTests(APITestCase):

    def setUp(self):
        self.data = {'email': 'normal@user.com', 'password': 'foo'}
        self.user = User.objects.create_user(
            email=self.data['email'],
            password=self.data['password']
        )

    def test_token_login(self):
        # post to get token
        response = self.client.post(
            reverse('token_obtain_pair'),
            data=self.data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access', response.data)
        self.assertTrue('refresh', response.data)

    def test_token_refresh(self):
        # post to get token
        response = self.client.post(
            reverse('token_obtain_pair'),
            data=self.data,
            format='json'
        )
        # post to get refresh token
        response = self.client.post(
            reverse('token_refresh'),
            data={'refresh': response.data['refresh']},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access', response.data)
