import json

import falcon

from constant import PROJECT_ID, TOPIC_NAME
from events import Event


class PublishResource:

    def __init__(self, publisher):
        self.publisher = publisher

    def on_post(self, req, resp):

        if req.content_length:
            doc = json.load(req.stream)
            event = Event(doc["name"])
            topic_path = self.publisher.topic_path(PROJECT_ID, TOPIC_NAME)
            response_future = self.publisher.publish(topic_path,
                                                    data=event.body)
            resp.body = json.dumps({"published": "true",
                                    "result": response_future.result()},
                                    ensure_ascii=False)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
