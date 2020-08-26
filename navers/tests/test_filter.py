from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .fixture import NaverFactory

User = get_user_model()


class NaverFilterTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='bruce@user.com', password='foo')

        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_filter(self):
        NaverFactory.create_batch(2, user=self.user)
        NaverFactory.create_batch(3, name='Jane', job_role='Back-end', user=self.user)
        NaverFactory.create_batch(2, name='Bruce', admission_date='2008-07-02', job_role='Dev', user=self.user)
        NaverFactory.create_batch(4, name='Bruce', admission_date='2018-05-01', job_role='Dev', user=self.user)
        NaverFactory.create_batch(1, job_role='Front-end', user=self.user)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Bruce&admission_date_gte=2018-05-01&job_role=Dev"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Jane&job_role=Back-end"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Jan&job_role=Front-end"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_name(self):
        NaverFactory.create_batch(2, user=self.user)
        NaverFactory.create_batch(3, name='Jane', user=self.user)
        NaverFactory.create_batch(1, name='Bruce', user=self.user)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Jonh"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Jane"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Bruce Wayne"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get(f'{reverse("naver-list")}{"?name=Bruce"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_admission_date(self):
        NaverFactory.create_batch(2, admission_date='2020-01-02', user=self.user)
        NaverFactory.create_batch(3, admission_date='2001-03-21', user=self.user)
        NaverFactory.create_batch(1, admission_date='2017-05-04', user=self.user)

        response = self.client.get(f'{reverse("naver-list")}{"?admission_date_gte=2018-01-01"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        response = self.client.get(f'{reverse("naver-list")}{"?admission_date_lte=2016-05-20"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        response = self.client.get(f'{reverse("naver-list")}{"?admission_date_gte=2000-12-05"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

        response = self.client.get(f'{reverse("naver-list")}{"?admission_date_lte=1900-01-01"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_job_role(self):
        NaverFactory.create_batch(2, user=self.user)
        NaverFactory.create_batch(3, job_role='Back-end', user=self.user)
        NaverFactory.create_batch(1, job_role='Front-end', user=self.user)

        response = self.client.get(f'{reverse("naver-list")}{"?job_role=Back Front"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get(f'{reverse("naver-list")}{"?job_role=Back-end"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        response = self.client.get(f'{reverse("naver-list")}{"?job_role=Front-end"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
