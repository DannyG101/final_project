
class S2Orchestrator:
    def __init__(self, consumer, mongo_db, elastic_search, logger):
        self.consumer = consumer
        self.mongo_db = mongo_db
        self.elastic_search = elastic_search
        self.logger = logger

    def run(self):
        self.logger.info("Beginning to consume and save data")
        data = self.consumer.consume()
        self.mongo_db.save_to_mongo(data)
        self.elastic_search.save_to_elasticsearch(data)
        self.logger.info("Completed to consume and save data")



