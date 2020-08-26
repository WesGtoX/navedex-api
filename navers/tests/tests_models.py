from django.test import TestCase
from django.contrib.auth import get_user_model

from navers.models import Naver
from projects.models import Project

User = get_user_model()


class PostModelTestCase(TestCase):

    def setUp(self):
        self.jane = User.objects.create_user(
            email='jane@user.com', password='foo123'
        )
        self.project1 = Project.objects.create(name='Projeto 1', user=self.jane)
        self.project2 = Project.objects.create(name='Projeto 2', user=self.jane)

    def test_create_naver(self):
        naver = Naver.objects.create(
            name='Fulano',
            birthdate='1999-05-15',
            admission_date='2020-06-12',
            job_role='Desenvolvedor',
            user=self.jane,
        )
        naver.projects.add(self.project1)
        naver.projects.add(self.project2)
        self.assertEqual(naver.name, 'Fulano')
        self.assertEqual(naver.birthdate, '1999-05-15')
        self.assertEqual(naver.admission_date, '2020-06-12')
        self.assertEqual(naver.job_role, 'Desenvolvedor')
        self.assertEqual(naver.__str__(), 'Fulano')
