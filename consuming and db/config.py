import os
from dotenv import load_dotenv

load_dotenv()


class S2Config:
    def __init__(self):
        self.kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.mongo_uri = os.getenv("MONGO_URI")
        self.es_uri = os.getenv("ES_URI")

