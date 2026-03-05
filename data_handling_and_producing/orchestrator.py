class S1Orchestrator:
    def __init__(self, data_handler, producer, logger):
        self.data_handler = data_handler
        self.producer = producer
        self. logger = logger

    def run(self, path):
        self.logger.info("Beginning data handling")
        data = self.data_handler.extract_metadata(path)
        self.data_handler.write_to_json(data)
        self.producer.publish_to_kafka(data)
        self.logger.info("Completed data handling")
