import os
import json
import shutil
import logging
from json.decoder import JSONDecodeError

logging.basicConfig(level=logging.INFO, format="%(message)s")

source_dir = "./NEED_CHANGE"

logging.info("Starting...")
changed_files_count = 0

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir,filename)
    with open(file_path, "r+") as file:
        try:
            data = json.load(file)
            date = data.get("date")
            if date != filename[:10]:
                new_date= filename[:10]
                data["date"] = new_date
                file.seek(0)
                json.dump(data,file, indent=4)
                changed_files_count+=1
        except JSONDecodeError as e:
            error_message = f"Error: {file_path}\n{e}"
            logging.error(error_message)
            continue

logging.info(f"changed {changed_files_count} files")
     