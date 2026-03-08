from elasticsearch import Elasticsearch


class ElasticSearch:
    def __init__(self, es_uri, logger):
        self.es = Elasticsearch(es_uri)
        self.logger = logger

    def save_to_elasticsearch(self, item_id, text):
        self.logger.info("Updating Elastic Search with the text")
        self.es.update(index='podcasts_index', id=item_id, body={'doc': { 'text': text}})
        self.logger.info("Updated to Elastic Search")

