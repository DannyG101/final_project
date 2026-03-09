class Orchestrator:
    def __init__(self, consumer, speech_to_text, elastic_search, producer, logger):
        self.consumer = consumer
        self.speech_to_text = speech_to_text
        self.elastic_search = elastic_search
        self.producer = producer
        self.logger = logger


    def handle_event(self, data):
        path = data["file_path"]
        item_id = data["item_id"]
        text = self.speech_to_text.convert_to_text(path)
        data["text"] = text
        self.elastic_search.save_to_elasticsearch(item_id, text)
        self.producer.publish_to_kafka(data)

    def run(self):
        self.logger.info("Beginning text extraction process")
        while True:
            data = self.consumer.consume()
            self.handle_event(data)



