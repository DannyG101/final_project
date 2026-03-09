from encoded_text import bad_list, less_bad_list

class Orchestrator:
    def __init__(self, consumer, text_analyzer, elastic_search, logger):
        self.consumer = consumer
        self.text_analyzer = text_analyzer
        self.elastic_search = elastic_search
        self.logger = logger

    def handle_event(self, data):
        item_id = data["item_id"]
        text = data["text"]
        analysis_dict = self.text_analyzer.analyze(text, bad_list, less_bad_list)
        self.elastic_search.save_to_elasticsearch(item_id, analysis_dict)

    def run(self):
        self.logger.info("Beginning text analysis")
        while True:
            data = self.consumer.consume()
            self.handle_event(data)




