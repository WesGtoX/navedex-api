from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .fixture import NaverFactory
from projects.models import Project

User = get_user_model()


class NaversViewSetTests(APITestCase):

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

        self.project1 = Project.objects.create(name='Projeto 1', user=self.user)
        self.project2 = Project.objects.create(name='Projeto 2', user=self.user)

    def test_perform_create(self):
        data = {
            "name": "Joe",
            "birthdate": "1999-05-15",
            "admission_date": "2020-06-12",
            "job_role": "Back-end",
            "projects": [self.project1.id, self.project2.id]
        }
        response = self.unath_client.post(reverse('naver-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(reverse('naver-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertTrue(len(response.data['projects']), 2)

    def test_list(self):
        NaverFactory.create_batch(5, user=self.user)

        response = self.unath_client.get(reverse('naver-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.get(reverse('naver-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get(reverse('naver-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 5)

    def test_retrieve(self):
        naver = NaverFactory.create(id=10, user=self.user)
        naver.projects.add(self.project1)
        naver.projects.add(self.project2)

        response = self.unath_client.get(reverse('naver-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.get(reverse('naver-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('naver-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], naver.name)
        self.assertEqual(response.data['birthdate'], str(naver.birthdate))
        self.assertEqual(response.data['admission_date'], str(naver.admission_date))
        self.assertEqual(response.data['job_role'], naver.job_role)
        self.assertTrue(len(response.data['projects']), 2)

    def test_update(self):
        naver = NaverFactory.create(id=21, user=self.user)
        data = {
            "name": "Joe",
            "birthdate": "1999-05-15",
            "admission_date": "2020-06-12",
            "job_role": "Back-end",
            "projects": [self.project1.id]
        }
        self.assertNotEqual(naver.name, data['name'])
        self.assertNotEqual(naver.job_role, data['job_role'])

        response = self.unath_client.put(reverse('naver-update', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.put(reverse('naver-update', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('naver-update', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertTrue(len(response.data['projects']), 1)

    def test_partial_update(self):
        naver = NaverFactory.create(id=22, user=self.user)
        data = {
            "name": "Joe",
            "job_role": "Back-end",
        }
        self.assertNotEqual(naver.name, data['name'])
        self.assertNotEqual(naver.job_role, data['job_role'])

        response = self.unath_client.patch(reverse('naver-update', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anon_client.patch(reverse('naver-update', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.patch(reverse('naver-update', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['job_role'], data['job_role'])

    def test_destroy(self):
        NaverFactory.create(id=15, user=self.user)
        response = self.unath_client.get(reverse('naver-delete', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('naver-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

        response = self.anon_client.delete(reverse('naver-delete', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('naver-delete', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('naver-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
