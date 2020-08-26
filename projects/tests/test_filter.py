from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .fixture import ProjectFactory

User = get_user_model()


class ProjectFilterTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='bruce@user.com', password='foo')

        self.client = APIClient()

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_filter_name(self):
        ProjectFactory.create_batch(2, user=self.user)
        ProjectFactory.create_batch(3, name='Projeto Bom', user=self.user)
        ProjectFactory.create_batch(1, name='Projeto Boom', user=self.user)

        response = self.client.get(f'{reverse("project-list")}{"?name=Projeto"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get(f'{reverse("project-list")}{"?name=Projeto Bom"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        response = self.client.get(f'{reverse("project-list")}{"?name=Projeto Boom"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(f'{reverse("project-list")}{"?name=P"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
