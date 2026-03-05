from pymongo import MongoClient
import gridfs


class GridFSStorage:
    def __init__(self, mongo_uri, logger):
        self.logger = logger
        self.client = MongoClient(mongo_uri)
        self.db = self.client["tweets_db"]
        self.fs = gridfs.GridFS(self.db)

    def save_to_mongo(self, data):
        self.logger.info("Saving to mongo")
        for item in data:
            file_path = item['file_path']

            item_id = f"{item['metadata']['file_name']}-{item['metadata']['file_size']}"
            item["id"] = item_id
            with open(file_path, 'rb') as file_data:
                self.fs.put(file_data, _id=item_id)
        self.logger.info("Saved to Mongo")