# Django project

This project is a rest api provide register, login, and list stock trade detail methods.
It also integrate django-rest-knox, django-rest-framework.

## Installation


This is an installation example in MacOS, and python version is 3.6.8 .


Install python depedency(remember to use virtualenv is better)
```sh
pip install -r requirements.txt
```
Configure you database setting in settings.py, then migrate it.
`(If you want to base it on production , remember change security key prevent security issue.)`
```sh
python manage.py migrate
```

## Run Demo
```sh
gunicorn stock_rest_api.wsgi
```