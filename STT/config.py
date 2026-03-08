import os
from dotenv import load_dotenv

load_dotenv()


class S3Config:
    def __init__(self):
        self.kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.es_uri = os.getenv("ES_URI")

