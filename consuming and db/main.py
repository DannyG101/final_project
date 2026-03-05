from config import S2Config
from consumer import KafkaConsumer
from mongo_db import GridFSStorage
from elastic_search_db import ElasticSearch
from orchestrator import S2Orchestrator

import logging
logging.basicConfig(level="INFO")

config = S2Config()
consumer = KafkaConsumer(config.kafka_bootstrap_servers, "podcasts", "podcasts", logging.getLogger(KafkaConsumer.__module__))
mongo_db = GridFSStorage(config.mongo_uri, logging.getLogger(GridFSStorage.__module__))
elastic_search = ElasticSearch(config.es_uri, logging.getLogger(ElasticSearch.__module__))
orchestrator = S2Orchestrator(consumer, mongo_db, elastic_search, logging.getLogger(S2Orchestrator.__module__))

orchestrator.run()









