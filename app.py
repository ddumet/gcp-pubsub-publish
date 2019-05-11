import falcon

from publish_resource import PublishResource


api = application = falcon.API()

publish_resource = PublishResource()
api.add_route("/publish", publish_resource)
