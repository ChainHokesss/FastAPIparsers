from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

from src.config.config import Config


class Kafka:
    def __init__(self, config: Config):
        self._producer = KafkaProducer(
            bootstrap_servers=[f'{config.kafka.host}:{config.kafka.port}'],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
        self._consumer = KafkaConsumer(
            'topic_test',
            bootstrap_servers=[f'{config.kafka.host}:{config.kafka.port}'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group-id',
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            consumer_timeout_ms=1000
        )

    @property
    def producer(self):
        return self._producer

    @property
    def consumer(self):
        return self._consumer

    def send_message(self, message):
        self.producer.send('topic_test', value={'message': message})

    def get_message(self):
        return self.consumer
