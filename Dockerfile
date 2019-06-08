# Image from which we inherit Dockerfile
FROM python:3.7-alpine

MAINTAINER Vojtech Janousek

# Disallows python from buffering outputs, just prints them directly
# Can avoid complications
ENV PYTHONUNBUFFERED 1

# Creates an empty folder on the Docker image, called /code
RUN mkdir /code

# Switches to that folder as the default directory
WORKDIR /code

# Copies the /setup_project folder from our local machine to the
# /code folder created on our image. This allows us to take
# the project code and copy it into our Docker image.
COPY . /code/

RUN pip install --upgrade pip

# RUN apk --update add jpeg-dev  \\
# RUN apk --update add --virtual gcc zlib zlib-dev

# Installs Pillow dependencies
RUN apk --update add jpeg-dev
RUN apk --update add --virtual .tmp-build-deps \
    gcc libc-dev linux-headers zlib zlib-dev

# Installs the requirements onto the Docker image
RUN pip install -r requirements.txt

# Created a user made only to run the application
# RUN adduser -D user
# Switches Docker to that user, otherwise it would use our root account
# which is not desirable
# USER user
