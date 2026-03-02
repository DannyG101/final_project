import datetime
from pathlib import Path
import json
import logging
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)


logger.info("Beginning metadata extraction process")
data = []
p = Path('/army_podcasts')
for file in p.iterdir():
    metadata = {"file_path": str(file),
                "file_name": file.stem,
                "file_type": file.suffix,
                "file_size": file.stat().st_size,
                "file_creation_date": datetime.datetime.fromtimestamp(file.stat().st_ctime).isoformat()}
    data.append(metadata)

logger.info("Inserting into json")
with open("data/files.json", "w") as f:
    json.dump(data, f, indent=4)
logger.info("Inserted all metadata into json")

