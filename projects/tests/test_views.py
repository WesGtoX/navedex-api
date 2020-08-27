from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .fixture import ProjectFactory
from navers.tests.fixture import NaverFactory

User = get_user_model()


class ProjectViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='bruce@user.com', password='foo')
        self.anon_user = User.objects.create_user(email='jane@user.com', password='bar')

        self.unath_client = APIClient()

        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        self.anon_client = APIClient()
        anon_refresh = RefreshToken.for_user(self.anon_user)
        self.anon_client.credentials(HTTP_AUTHORIZATION=f'Bearer {anon_refresh.access_token}')

        self.naver1 = NaverFactory.create(id=1, user=self.user)
        self.naver2 = NaverFactory.create(id=2, user=self.user)

    def test_perform_create(self):
        data = {
            "name": "Projeto Realmente Bom",
            "navers": [self.naver1.id, self.naver2.id]
        }
        response = self.unath_client.post(reverse('project-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(reverse('project-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertTrue(len(response.data['navers']), 2)

    def test_list(self):
        ProjectFactory.create_batch(5, user=self.user)

        response = self.unath_client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 5)

    def test_retrieve(self):
        project = ProjectFactory.create(id=10, user=self.user)
        project.navers.add(self.naver1)
        project.navers.add(self.naver2)

        response = self.unath_client.get(reverse('project-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.get(reverse('project-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('project-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], project.name)
        self.assertTrue(len(response.data['navers']), 2)

    def test_update(self):
        project = ProjectFactory.create(id=21, user=self.user)
        data = {
            "name": "Projeto muito Bom",
            "navers": [self.naver1.id]
        }
        self.assertNotEqual(project.name, data['name'])

        response = self.unath_client.put(reverse('project-update', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.put(reverse('project-update', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('project-update', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertTrue(len(response.data['navers']), 1)

    def test_partial_update(self):
        project = ProjectFactory.create(id=22, user=self.user)
        data = {
            "name": "Projeto Bom",
        }
        self.assertNotEqual(project.name, data['name'])

        response = self.unath_client.patch(reverse('project-update', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.patch(reverse('project-update', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.patch(reverse('project-update', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_destroy(self):
        ProjectFactory.create(id=15, user=self.user)
        response = self.unath_client.get(reverse('project-delete', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

        response = self.anon_client.delete(reverse('project-delete', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('project-delete', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
