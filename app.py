import falcon

from publish_resource import PublishResource
from google.cloud import pubsub_v1


api = application = falcon.API()

publisher = pubsub_v1.PublisherClient()
publish_resource = PublishResource(publisher)

api.add_route("/publish", publish_resource)
