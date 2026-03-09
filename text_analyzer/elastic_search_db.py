from elasticsearch import Elasticsearch


class ElasticSearch:
    def __init__(self, es_uri, logger):
        self.es = Elasticsearch(es_uri)
        self.logger = logger

    def save_to_elasticsearch(self, item_id, analysis_dict):
        self.logger.info("Updating Elastic Search with the text")
        self.es.update(index='podcasts_index', id=item_id, body={'doc': analysis_dict})
        self.logger.info("Updated to Elastic Search")

