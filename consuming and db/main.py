from config import S2Config
from consumer import KafkaConsumer
from mongo_db import GridFSStorage
from elastic_search_db import ElasticSearch
from producer import KafkaPublisher
from orchestrator import S2Orchestrator

from logging_class import Logger


config = S2Config()

logger = Logger.get_logger("S2_Logger", config.es_uri)

consumer = KafkaConsumer(config.kafka_bootstrap_servers, "podcasts", "podcasts", logger)
mongo_db = GridFSStorage(config.mongo_uri, logger)
elastic_search = ElasticSearch(config.es_uri, logger)
producer = KafkaPublisher(config.kafka_bootstrap_servers, "STT", logger)
orchestrator = S2Orchestrator(consumer, mongo_db, elastic_search, producer, logger)

orchestrator.run()









