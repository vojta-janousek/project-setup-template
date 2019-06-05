# Image from which we inherit Dockerfile
FROM python:3.7-alpine

MAINTAINER Vojtech Janousek

# Disallows python from buffering outputs, just prints them directly
# Can avoid complications
ENV PYTHONUNBUFFERED 1

# Copies requirements filled with dependencies onto the Docker image
COPY ./requirements.txt /requirements.txt
# Installs the requirements onto the Docker image
RUN pip install -r /requirements.txt

# Creates an empty folder on the Docker image, called /app
RUN mkdir /app
# Switches to that folder as the default directory
WORKDIR /app
# Copies the /app folder from our local machine to the /app folder
# created on our image. This allows us to take the project code
# and copy it into our Docker image.
COPY ./app /app

# Created a user made only to run the application
RUN adduser -D user
# Switches Docker to that user, othewise it would use our root account
# which is not desirable
USER user
