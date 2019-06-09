Setting up a Django project:

Basic setup:
1) Create a GitHub repository

- MIT License
- gitignore: Python

2) Clone the repository to a local file

"git clone git@github.com:vojta-janousek/project-name.git"

3) Create and configure a Dockerfile

Select the image you are going to inherit the Dockerfile from.
Images can be found at: https://hub.docker.com

4) Create requirements.txt

Check the newest versions of dependencies at
https://pypi.org

5) Create an empty folder called setup_project

Finish with: "docker build ."

6) Create a docker-compose.yml configuration

Tool that allows us to run our Docker image from our project location

"docker-compose build"
"docker-compose up"

7) Create a Django project

docker-compose run setup_project sh -c "django-admin startproject setup_project ."

8) Travis CI

Automation tool for builds. Can run linting tools, unit tests etc.

https://travis-ci.org/

- Login with GitHub and activate Travis on the repository
- Create files .travis.yml and .flake8 in in the root directory
- In .flake8, exclude all files that should not be linted

9) Docker commands

docker-compose run setup_project sh -c "python setup_project/manage.py test && flake8"
docker-compose run setup_project sh -c "python manage.py startapp appname"

docker-compose run setup_project sh -c "python manage.py migrate"
docker-compose run setup_project sh -c "python manage.py makemigrations appname"
docker-compose run setup_project sh -c "python manage.py createsuperuser"
