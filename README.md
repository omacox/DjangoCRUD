# Django CRUD

- Start with

```python

mkdir /projecttodo

python -m venv .venv

```

- macOS/Linux

```bash

source .venv/bin/activate

pip install django

django-admin startproject todoproject
cd todoproject
python manage.py startapp todoapp

python manage.py makemigrations
python manage.py migrate


├── README.md                     # Outline 
├── db.sqlite3                    # Database
├── manage.py
├── templates
│   ├── layout.html
│   └── todoapp
│       ├── confirmation.html
│       ├── show.html
│       └── todo.html
├── todoapp
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── forms.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── todoproject
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

install these

```bash

pip install crispy-bootstrap5
pip install django-crispy-forms

```

test configuration

```bash

python manage.py runserver

```

if you need to kill the process you can use these

```bash
lsof -i :<port_number>

kill -9 <PID>

```

## Setting up Admin

```python

python manage.py createsuperuser


python manage.py makemigrations
python manage.py migrate


```
