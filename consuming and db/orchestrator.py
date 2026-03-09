class S2Orchestrator:
    def __init__(self, consumer, mongo_db, elastic_search, producer, logger):
        self.consumer = consumer
        self.mongo_db = mongo_db
        self.elastic_search = elastic_search
        self.producer = producer
        self.logger = logger

    def run(self):
        self.logger.info("Beginning to consume and save data")
        while True:
            data = self.consumer.consume()
            self.mongo_db.save_to_mongo(data)

            self.elastic_search.save_to_elasticsearch(data)
            self.logger.info("Completed to consume and save data")

            self.logger.info("Publishing data to STT Service")
            for item in data:
                file_path = item['file_path']
                item_id = f"{item['metadata']['file_name']}-{item['metadata']['file_size']}"
                new_data = {"file_path": file_path, "item_id": item_id}
                self.producer.publish_to_kafka(new_data)
                self.logger.info("published data to STT Service")



