import os
import json
import shutil
import logging
from json.decoder import JSONDecodeError

logging.basicConfig(level=logging.INFO, format="%(message)s")

source_dir = "./source"
output_dir = "./NEED_CHANGE"

os.makedirs(output_dir) if not os.path.exists(output_dir) else None

logging.info("Starting...")
moved_files_count = 0

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir,filename)
    with open(file_path) as file:
        try:
            data = json.load(file)
            date = data.get("date")
            if date != filename[:10]:
                file.close()
                output_path = os.path.join(output_dir,filename)
                shutil.move(file_path, output_path)
                moved_files_count+=1
        except JSONDecodeError as e:
            error_message = f"Error: {file_path}\n{e}"
            logging.error(error_message)
            continue

logging.info(f"moved {moved_files_count} ")
     