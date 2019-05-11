# Description
A simple project to play with GCP pubsub.

## Install
```
mkdir my-dir
cd my-dir
git pull
virtualenv .venv
cd pubsub-publisher
pip install -r requirements.txt
```



## Run locally (Windows)
To run this app locally on windows waitress is needed (gunicorn does not run on windows).
```
pip install waitress
```
And then run the app with:
```
waitress-serve --port=8000 app:api
```

# Build & Deploy container
## For local deployment
Building container locally for testing:
```
docker build --tag image-name:version .
```
Running docker locally with:
```
docker run --publish 8000:8000 --name container-name image-name:version
```

## For GCP deployment
Before pushing the container to **GCP**, we must tag our image with the necessary information that **GCP** needs, that is [REGISTRY-NAME]/[PROJECT-ID]/[IMAGE-NAME].

REGISTRY-NAME could be:
* **gcr.io** for hosting images in US
* **us.gcr.io** for hosting images in US
* **eu.gcr.io** for hosting images in EU
* **asia.gcr.io** for hosting images in Asia

For instance:
```
docker tag image-name:version eu.gcr.io/<PROJECT ID>/image-name:version
```
Authenticate to Container Registry to be able to push (details of authentication here: *https://cloud.google.com/container-registry/docs/advanced-authentication*):
```
gcloud auth configure-docker
```
We can now push the image to **GCP** Container Registry using the gcloud command:
```
docker --push gcr.io/<PROJECT NAME>/image-name:version
```
# Run container
## Run container locally
```
docker run --publish 8000:8000 -name pip install waitress
```
And then run it with:
```
waitress-serve --port=8000 app:api
```