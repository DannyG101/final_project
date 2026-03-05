from confluent_kafka import Consumer
import json

class KafkaConsumer:
    def __init__(self, kafka_bootstrap_servers, kafka_topic, _kafka_group_id, logger):
        self.kafka_bootstrap_servers= kafka_bootstrap_servers
        self.kafka_topic = kafka_topic
        self.kafka_group_id = _kafka_group_id
        self.logger = logger
        self.consumer = None

    def consume(self):
        if self.consumer is None:
            consumer_config = {
                "bootstrap.servers": self.kafka_bootstrap_servers,
                "group.id": self.kafka_group_id,
                "auto.offset.reset": "earliest"
            }

            self.consumer = Consumer(consumer_config)

            self.consumer.subscribe([self.kafka_topic])

        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("❌ Error:", msg.error())
                continue

            else:
                value = msg.value().decode("utf-8")
                data = json.loads(value)
                return data