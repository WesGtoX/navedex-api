<h1 align="center">
  <a href="https://github.com/WesGtoX/navedex-api">
    <img src=".github/logo.png" alt="Navedex API" title="Navedex API" width="200px">
  </a>
  <br />
  <img alt="Navedex-API CI" src="https://github.com/WesGtoX/navedex-api/workflows/Navedex-API%20CI/badge.svg" />
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#usage">Usage</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/navedex-api?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/navedex-api?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/navedex-api?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/navedex-api?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/navedex-api?style=plastic" />
</p>


# Navedex API

...


## About the Project

Navedex is an API to register navedex’s and projects in which they participated.

The project was developed using the Django REST Framework which is Django's toolkit, powerful and flexible to build API’s Web.


## Technology 

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)


## Getting Started

### Prerequisites

- [Python](https://www.python.org/)


### Install and Run

1. Clone the repository:
```bash
git clone https://github.com/WesGtoX/navedex-api.git
```
2. Create and activate a virtual enviroment:
```bash
python -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```bash
pip install -r requirements-dev.txt
```
4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Create a superuser:
```bash
python manage.py createsuperuser
```
6. Run:
```bash
python manage.py runserver
```
7. To run tests:
```bash
pytest
# or
python manage.py test
```


## Usage

### Insomnia

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Navedex&uri=https%3A%2F%2Fraw.githubusercontent.com%2FWesGtoX%2Fnavedex-api%2Fmaster%2Fnavedex_insomnia.json)

<p align="center">
  <img src="misc/images/img01.gif" alt="Insomnia Example" width="450px" />
  <img src="misc/images/img02.gif" alt="Insomnia Example" width="450px" />
</p>

<p align="center">
  <img src="misc/images/img03.gif" alt="Insomnia Example" width="450px" />
  <img src="misc/images/img04.gif" alt="Insomnia Example" width="450px" />
</p>


_For more examples, please refer to the [Documentation](https://github.com/WesGtoX/navedex-api/wiki)_


## License

Distributed under the MIT License. See [LICENSE](LICENSE.md) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com.br/) :wave:
