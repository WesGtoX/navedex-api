import random
import requests

from faker import Faker
from time import sleep

BASE_URL = 'http://127.0.0.1:8000'
DEV_PASSWD = 'dev@pass123'
faker = Faker(['pt_BR'])


def get_headers():
    return {'content-type': 'application/json'}


def signup():
    headers = get_headers()
    email_list = get_email_list()
    for user_email in email_list:
        response = requests.post(
            url=f'{BASE_URL}/signup/',
            headers=headers,
            json={'email': user_email, 'password': DEV_PASSWD}
        )
        print({'status_code': response.status_code, 'email': user_email, 'message': response.json().get('email')})
        sleep(1)


def token_refresh(refresh, user_email):
    headers = get_headers()
    response = requests.post(
        url=f'{BASE_URL}/token/refresh/',
        headers=headers,
        json={'refresh': refresh}
    )
    if response.ok:
        return response.json()['access']


def login(user_email):
    headers = get_headers()
    response = requests.post(
        url=f'{BASE_URL}/login/',
        headers=headers,
        json={
            'email': user_email,
            'password': DEV_PASSWD
        }
    )
    if response.ok:
        return token_refresh(response.json()['refresh'], user_email)


def get_token(email):
    return login(email)


def get_email_list():
    name_list = ['dev', 'jane', 'bruce', 'max', 'jonh', 'mary']
    return [f'{email}@navedex.com' for email in name_list]


def get_random_email():
    name_list = ['dev', 'jane', 'bruce', 'max', 'jonh', 'mary']
    return f'{random.choice(name_list)}@navedex.com'


def get_projects_list_id(user_email):
    token_jwt = get_token(user_email)

    headers = get_headers()
    headers['authorization'] = f'Bearer {token_jwt}'

    response = requests.get(
        url=f'{BASE_URL}/projects/index/',
        headers=headers
    )
    if response.ok:
        return [r.get('id') for r in response.json()]


def create_projects(user_email):
    token_jwt = get_token(user_email)

    headers = get_headers()
    headers['authorization'] = f'Bearer {token_jwt}'

    response = requests.post(
        url=f'{BASE_URL}/projects/store/',
        headers=headers,
        json={
            'name': faker.company(),
            "navers": []
        }
    )
    if not response.ok:
        print({'status_code': response.status_code, 'message': response.json()})

    print(response.json())


def create_navers(user_email, projects_ids=None):
    token_jwt = get_token(user_email)

    headers = get_headers()
    headers['authorization'] = f'Bearer {token_jwt}'

    job_role = [
        'Back-end',
        'Cientista de Dados',
        'Desenvolvedor',
        'Dev Fullstack',
        'DevOps',
        'Engenheiro',
        'Ethical Hacking',
        'Front-end',
        'Scrum Master',
        'UX Designer'
    ]

    data = {
        'name': faker.first_name(),
        'birthdate': str(faker.date_between(start_date='-40y', end_date='-20y')),
        'admission_date': str(faker.date_between(start_date='-20y', end_date='today')),
        'job_role': random.choice(job_role)
    }

    if projects_ids:
        data['projects'] = projects_ids

    response = requests.post(
        url=f'{BASE_URL}/navers/store/',
        headers=headers,
        json=data
    )
    if not response.ok:
        print({'status_code': response.status_code, 'message': response.json()}, '\n')

    print(response.json())


def get_projects_size(projects_ids):
    if projects_ids:
        n = len(projects_ids)
        if n == 0:
            return n
        else:
            size = n - 1 if n > 1 else 1
            return random.choice(range(size)) + 1
    return 0


def quantity_insert(number):
    try:
        return int(number)
    except ValueError:
        return 0


def navers_process(qtd=0):
    for i in range(qtd):
        email = get_random_email()
        print('=' * 20)
        print({'user': email})
        projects_ids = get_projects_list_id(email)
        k = get_projects_size(projects_ids)
        id_list = random.sample(projects_ids, k=k)
        create_navers(email, id_list)


def projects_process(qtd=0):
    for i in range(qtd):
        email = get_random_email()
        print('=' * 10)
        print({'user': email})
        create_projects(email)
    return True


def populate_process():
    print('=' * 20)
    register = input('DO YOU WANT TO REGISTER USER? [Y/n]: ')

    if register.lower() == 'y':
        signup()

    print('=' * 20)
    quantity = input('NUMBER OF PROJECTS TO CREATE [default = 0]: ')
    result = projects_process(quantity_insert(quantity))

    if result:
        print('=' * 20)
        quantity = input('NUMBER OF NAVERS TO CREATE [default = 0]: ')
        navers_process(quantity_insert(quantity))


if __name__ == '__main__':
    populate_process()
