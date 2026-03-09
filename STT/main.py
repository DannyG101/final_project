from config import S3Config
from consumer import KafkaConsumer
from speech_to_text import SpeechToText
from elastic_search_db import ElasticSearch
from producer import KafkaPublisher
from orchestrator import Orchestrator

from logging_class import Logger

config = S3Config()

logger = Logger.get_logger("S3_Logger", config.es_uri)

consumer = KafkaConsumer(config.kafka_bootstrap_servers, "STT", "STT", logger)

speech_to_text = SpeechToText(logger)

elastic_search = ElasticSearch(config.es_uri, logger)

producer = KafkaPublisher(config.kafka_bootstrap_servers, "text_analyzer", logger)

orchestrator = Orchestrator(consumer, speech_to_text, elastic_search, producer, logger)

orchestrator.run()