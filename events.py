import json
import base64


class Event:

    def __init__(self, name):
        self.name = name
        self.create_body()

    def create_body(self):
        """
        Initialse the body of the event to be published.
        Body is different per event name.
        Body is stored ready to be published on pub/sub,
        i.e. base64 encoded.
        """

        # PROVISIONED event
        if self.name == "PROVISIONED":
            self.body = {
                "name": "PROVISIONED",
                "service": "SECURENET_CONVERGED",
                "line_ids": [
                    {
                        "account": "245TU786",
                        "mobile_line": "447123456789"
                    }
                ],
                "security_platform_id": "0e03a9f3-c47e-41fc-9c96-c744fbbdb6f8"
            }

        # base64 encoding
        self.body = base64.b64encode(json.dumps(self.body,
                                                ensure_ascii=False).encode())

        return()

    def publish_pubsub():
        """
        Publish the event in GCP pubsub
        """
