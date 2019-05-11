# From Debian slim-stretch
# Alpine distribution not working with the required pachages
# An error happen while installing package grpcio which is 
# a dependency for google-cloud-pubsub
FROM python:3.7-slim-stretch

# Make a working DIR for our app
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Install all required python packages
COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all of our app files
# (Except the one in .dockerignore)
COPY . /usr/src/app

# Set environment variable for the service account key
# (contained in the file referenced by the env variable)
ENV GOOGLE_APPLICATION_CREDENTIALS proj-gcp-playground-673e89080276.json

# Expose our service on port 8000
EXPOSE 8000

# Start gunicorn
CMD ["gunicorn" , "-b", "0.0.0.0:8000", "app"]