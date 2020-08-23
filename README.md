# PyBlog
The PyBlog is a blog app where users can register themselves to post articles and see each others posts. This project implements various important aspects of Django.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/ "PEP8 style guidelines").

## Features
* Users
	* Account creation
	* Update the profile
	* Create, Read, Update, and Delete own posts
	* Read posts of other users
* Admins
	* Read all models
	* Does have any access to sensitive data like passwords

## Frontend
Bootstrap 4.0 is used for the frontend.

## Backend
Django 2.1 with Python 3.7 is used for the backend.

## Getting Started
#### Installing Dependencies

##### MiniConda
Download and install MiniConda from [here](https://docs.conda.io/en/latest/miniconda.html).
> It is used to create and manage the virtual environment.
> pip freeze > requirements.txt is used to create the dependency list.

###### Create Virtual Environment and Install Dependencies
```bash
conda create --name env_pyblog python=3.7
conda activate env_pyblog
pip install -r requirements.txt
```

##### Python 3.7
It is installed while creating the venv.

#### PIP Dependencies

`pip install -r requirements.txt`

This will install all of the required packages we selected within the requirements.txt file.

#### Key Dependencies
* Django - A Python based web framework
* pillow - A library to manage images in Django Apps
* django-crispy-forms - A Library to integrate Django forms with Bootstrap
* flake8 - Used for mainting the linting with VSCode
* autopep8 - Used for few auto linting with VSCode

##### Installation
`pip install flake8, autopep8, pillow, django-crispy-forms`
> Included in requirements.txt - external installation not required.

#### Database Setup
##### Development
SQLite database is used for development. It is configured automatically by Django.

##### Production

With Postgres, create a database named **pyblogdb**

`createdb pyblogdb`

> Make sure to include the database credentials in **env_file.py**

#### Running the server
From the project directory to run the server, execute:
```bash
conda activate env_pyblog
python manage.py runserver
```

#### Tests
##### pytest
In order to run tests, navigate to the project folder and run the following commands:

`pytest test_app.py`

## Deployment
We are using Heroku for deployment.
* Install heroku in your machine.
* Login to heroku
```bash
heroku login
```
* Create an app
```bash
heroku create appname
```
* Create 2 databases by running the following command twice. One for application and other one to use during the test.
```bash
heroku addons:create heroku-postgresql:hobby-dev --app appname
```
* Check configuration variables in Heroku
```bash
heroku config --app appname
```
> Note down the db variables and include them in the setup.sh.

* Initialize git in the project directory
```bash
git init
git remote add heroku https://git.heroku.com/appname.git
```

* Push it to heroku
```bash
git add .
git commit -am "make it better"
git push heroku master
```

> If there is any issue, use `heroku restart` to restart the app.

## Author
* [Himel Das](https://www.linkedin.com/in/himeldas/)

## Acknowledgements
This project is created while studying Django Full-Featured Web App by Corey Schafer in YouTube. Special thanks to Corey Schafer for creating such a beautiful course demostrating each part so beautifully.

* [YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
* [GitHub Repository](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog)
