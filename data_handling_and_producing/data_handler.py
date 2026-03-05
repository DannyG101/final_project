import datetime
from pathlib import Path
import json


class DataHandler:
    def __init__(self, logger):
        self.logger = logger


    def extract_metadata(self, path):
        self.logger.info("Beginning metadata extraction")
        data = []
        p = Path(path)
        for file in p.iterdir():
            metadata = {"file_path": str(file),
                        "metadata": {"file_name": file.stem,
                             "file_type": file.suffix,
                             "file_size": file.stat().st_size,
                             "file_creation_date": datetime.datetime.fromtimestamp(file.stat().st_ctime).isoformat()}}
            data.append(metadata)

        self.logger.info("Completed metadata extraction")
        return data


    def write_to_json(self, data):
        self.logger.info("Writing to JSON file")
        with open("data/files.json", "w") as f:
            json.dump(data, f, indent=4)


