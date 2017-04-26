import pika
import uuid
import json

class ParseJapaneseRpc(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("rabbit-server"))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, queue=self.callback_queue)

    def on_response(self, ch, method, properties, body):
        if self.correlation_id == properties.correlation_id:
            self.response = body

    def __call__(self, text):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange="",
                                   routing_key="rpc_queue",
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.correlation_id),
                                   body=text)
        while self.response is None:
            self.connection.process_data_events()

        return json.loads(self.response.decode("utf-8"))

