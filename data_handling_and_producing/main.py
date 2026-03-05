from config import S1Config
from data_handler import DataHandler
from producer import KafkaPublisher
from orchestrator import S1Orchestrator

import logging
logging.basicConfig(level="INFO")

config = S1Config()
data_handler = DataHandler(logging.getLogger(DataHandler.__module__))
producer = KafkaPublisher(config.kafka_bootstrap_servers, "podcasts", logging.getLogger(KafkaPublisher.__module__))
orchestrator = S1Orchestrator(data_handler, producer, logging.getLogger(S1Orchestrator.__module__))

orchestrator.run("/army_podcasts")