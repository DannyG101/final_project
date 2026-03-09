from config import S4Config
from logging_class import Logger
from consumer import KafkaConsumer
from text_analyzer import TextAnalyzer
from elastic_search_db import ElasticSearch
from orchestrator import Orchestrator

config = S4Config()

logger = Logger.get_logger("S4_logger", config.es_uri)

consumer = KafkaConsumer(config.kafka_bootstrap_servers, "text_analyzer", "text_analyzer", logger)

text_analyzer = TextAnalyzer()

elastic_search = ElasticSearch(config.es_uri, logger)

orchestrator = Orchestrator(consumer, text_analyzer, elastic_search, logger)

orchestrator.run()

