About
---------------
Editor: VS Code
Theme: Dainty Andromeda


Versions
--------
Python 3.7
Django 2.1
Bootstrap 4.0

Notes
-----
Make migration after installing new app or doing some major change in the settings.py file.


Initial
-------
prompt $g
conda activate env_pyblog
conda deactivate

conda activate env_pyblog
django-admin startproject django_project
django-admin startapp blog
django-admin startapp users
python manage.py runserver


Env Initialization
------------------
conda create --name env_pyblog python=3.7

Inside env:
conda install django=2.1
Check version: python -m django --version
conda remove --name env_pyblog --all

List all packages in the current environment:
conda list

Save packages for future use:
conda list --export > packages.txt

Reinstall packages from an export file:
conda create -n env_pyblog --file packages.txt


Installed Packages
------------------
Libary for linting:
pip install flake8

Style Django forms with Bootstrap:
pip install django-crispy-forms
conda install -c conda-forge django-crispy-forms

Libraries for user authentication:
pip install bcrypt
pip install django[argon2]

Library for pictures:
pip install pillow
If you get any error like jpeg support disabled:
pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"



Create the folders in the blog directory:
-----------------------------------------
templates/blog, static/blog


Edit the settings.py in the project directory:
----------------------------------------------

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    ...
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    ...
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':9}
    },
    ...
]

# User-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Select Boostrap version in crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login related URLs
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'blog-home'


Migration
---------
# 'makemigrations' initiates the migration and 'migrate' performs the migration.
python manage.py makemigrations
python manage.py migrate


python manage.py shell
from first_app.models import Topic
t = Topic(topic_name="Social Network")
t.save()
print(Topic.objects.all())
print(t)


Create Super User
-----------------
python manage.py createsuperuser


Users
-----
john
password@123

mike
password@123
