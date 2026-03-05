import os
from dotenv import load_dotenv

load_dotenv()


class S1Config:
    def __init__(self):
        self.kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

