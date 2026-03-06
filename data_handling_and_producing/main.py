from config import S1Config
from data_handler import DataHandler
from producer import KafkaPublisher
from orchestrator import S1Orchestrator

from logging_class import Logger

config = S1Config()

logger = Logger.get_logger("S1_Logger", config.es_uri)

data_handler = DataHandler(logger)
producer = KafkaPublisher(config.kafka_bootstrap_servers, "podcasts", logger)
orchestrator = S1Orchestrator(data_handler, producer, logger)

orchestrator.run("/army_podcasts")