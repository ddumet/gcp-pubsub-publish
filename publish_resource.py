import json

import falcon

from constant import PROJECT_ID, TOPIC_NAME
from events import Event

from google.cloud import pubsub_v1


class PublishResource:

    def on_post(self, req, resp):

        if req.content_length:
            doc = json.load(req.stream)
            event = Event(doc["name"])
            pubsub_client = pubsub_v1.PublisherClient()
            topic_path = pubsub_client.topic_path(PROJECT_ID, TOPIC_NAME)
            response_future = pubsub_client.publish(topic_path,
                                                    data=event.body)
            resp.body = json.dumps({"published": "true",
                                    "result": response_future.result()},
                                    ensure_ascii=False)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
