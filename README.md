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

5) Create an empty folder called app

Finish with: "docker build ."

6) Create a Docker compose configuration

Tool that allows us to run our Docker image from our project location

"docker-compose build"

7) Create a Django project

''' docker-compose run setup_project sh -c "django-admin startproject setup_project ." '''

8) Travis CI

Automation tool for builds. Can run linting tools, unit tests etc.

https://travis-ci.org/

- Login with GitHub and activate Travis on the repository
- Create file .travis.yml in root directory and file .flake8 in project directory
- In .flake8, exclude all files that should not be linted
