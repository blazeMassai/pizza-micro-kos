import os
from unittest import result

import pika
from pika import channel


class Consumer:
    def __init__(self, host, username, password):
        self.host=host
        self.username=username
        self.password=password

    def _init_channels(self):
        connection = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{self.username}:{self.password}@{self.host}:5672')
        )
        return connection.channel()

    def _init_queue(exchange, queue_name, routing_key):
        queue = channel.queue_delcare(queue=queue_name)
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        return result.method.queue

    def consume(self, exchange, queue_name, routing_key,
                callback):
        channel = self._init_channels()

        queue_name = self._init_queue()
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
        )


consumer = Consumer(
host=os.environ.get('RABBITMQ_HOST'),
username=os.environ.get('RABBITMQ_USERNAME'),
password=os.environ.get('RABBITMQ_PASSWORD'),
)