from elasticsearch import Elasticsearch


class ElasticSearch:
    def __init__(self, es_uri, logger):
        self.es = Elasticsearch(es_uri)
        self.logger = logger

    def save_to_elasticsearch(self, data):
        self.logger.info("Saving to Elastic Search")
        for item in data:
            item_id = f"{item['metadata']['file_name']}-{item['metadata']['file_size']}"
            metadata = item['metadata']
            self.es.index(index='test_index', id=item_id, document=metadata)
        self.logger.info("Saved to Elastic Search")

