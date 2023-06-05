import argparse
import datetime
import json
import logging
import os
import shutil
import time
from json.decoder import JSONDecodeError

logging.basicConfig(level=logging.INFO, format="%(message)s")


def prepare_data(source_dir, output_dir, dry_run=True):
    if not dry_run:
        os.makedirs(output_dir, exist_ok=True)

    moved_files_count = 0

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        with open(file_path) as file:
            try:
                data = json.load(file)
                date = data.get("date")
                if date != filename[:10]:
                    file.close()

                    if not dry_run:
                        output_path = os.path.join(output_dir, filename)
                        shutil.move(file_path, output_path)

                    moved_files_count += 1

            except JSONDecodeError as e:
                error_message = f"Error: {file_path}\n{e}"
                logging.error(error_message)
                continue

    return logging.info(f"Moved {moved_files_count} files due to json date not matching the filename they need to be changed manually using edit_prepared_data.py")


def sort_data(input_file, output_dir, dry_run=True):
    filename = os.path.basename(input_file)
    date = filename[:10]
    year, month, day = map(int, date.split("-"))
    no_week = datetime.date(year, month, day).isocalendar()[1]

    week_dir = os.path.join(output_dir, str(year), f"W{no_week:02}")

    output_file = os.path.join(week_dir, filename[5:])

    if not dry_run:
        os.makedirs(week_dir, exist_ok=True)
        shutil.move(input_file, output_file)

    return {"source": input_file, "target": output_file}


def arguments():
    source_dir = "./source"
    output_dir = "./target"

    parser = argparse.ArgumentParser(description="Data Sorting")
    parser.add_argument("-i", "--input", dest="input_dir",
                        default=source_dir, help="Input dir")
    parser.add_argument("-o", "--output", dest="output_dir",
                        default=output_dir, help="Target dir")
    parser.add_argument("-v", "--version", action="version",
                        version="1.0.0", help="Show version")
    parser.add_argument("-w", "--write", dest="write",
                        action="store_true", help="Write the changes")
    return parser.parse_args()


def main():
    args = arguments()
    source_dir = args.input_dir
    output_dir = args.output_dir
    dry_run = not args.write

    total_files = 0
    successful_files = 0
    errors = []

    prepare_data(source_dir, "./NEED_CHANGE", dry_run)
    input("Press any key to continue...")

    for file_count in os.listdir(source_dir):
        total_files += 1

    logging.info(f"Processing {total_files} files...")
    time.sleep(1)

    for root, _, files in os.walk(source_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                logging.info(sort_data(file_path, output_dir, dry_run))
                successful_files += 1
            except (JSONDecodeError, ValueError, OSError, Exception) as e:
                error_message = f"Error: {file_path}\n{e}"
                errors.append({"file path": file_path, "error": e})
                logging.error(error_message)
                continue

    if successful_files == file_count:
        logging.info(f"Success: processed {successful_files}/{total_files}")
    else:
        logging.info(f"Failure: processed {successful_files}/{total_files}")
        logging.info(f"Found Errors in: \n{errors}")


if __name__ == "__main__":
    main()
