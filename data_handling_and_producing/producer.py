import json
from confluent_kafka import Producer

class KafkaPublisher:
    def __init__(self, kafka_bootstrap_servers, kafka_topic, logger):
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.kafka_topic = kafka_topic
        self.logger = logger

    def publish_to_kafka(self, event):
        self.logger.info("Publishing to Kafka")
        producer_config = {
            "bootstrap.servers": self.kafka_bootstrap_servers
        }

        producer = Producer(producer_config)

        def delivery_report(err, msg):
            if err:
                self.logger.error(f"Error while trying to publish to Kafka: {err}")
            else:
                self.logger.info(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")


        value = json.dumps(event).encode("utf-8")

        producer.produce(
            topic=self.kafka_topic,
            value=value,
            callback=delivery_report
        )

        producer.flush()