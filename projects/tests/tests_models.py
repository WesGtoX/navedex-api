from django.test import TestCase
from django.contrib.auth import get_user_model

from projects.models import Project
from navers.models import Naver

User = get_user_model()


class PostModelTestCase(TestCase):

    def setUp(self):
        self.bruce = User.objects.create_user(
            email='bruce@user.com', password='bar123'
        )
        self.naver1 = Naver.objects.create(
            name='Jane',
            birthdate='1999-05-15',
            admission_date='2020-06-12',
            job_role='Back-end',
            user=self.bruce,
        )
        self.naver2 = Naver.objects.create(
            name='Fulano',
            birthdate='1999-05-15',
            admission_date='2020-06-12',
            job_role='Desenvolvedor',
            user=self.bruce,
        )

    def test_create_project(self):
        project = Project.objects.create(name='Projeto Realmente Bom', user=self.bruce)
        project.navers.add(self.naver1)
        project.navers.add(self.naver2)
        self.assertEqual(project.name, 'Projeto Realmente Bom')
        self.assertEqual(project.__str__(), 'Projeto Realmente Bom')
