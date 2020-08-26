import factory
from navers.models import Naver


class NaverFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Naver

    name = factory.Faker('first_name')
    birthdate = factory.Faker('date', end_datetime='-20y')
    admission_date = factory.Faker('date_between', start_date='-30y', end_date='today')
    job_role = factory.Faker('job')
