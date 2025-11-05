"""A smart script that reads command-line arguments, processes files, and logs everything."""

import argparse
from pathlib import Path
import shutil
import logging

# Setup logging
logging.basicConfig(
    filename = "logs/arg_logger.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def copy_file(input_path, output_folder):
    input_path = Path(input_path)
    output_folder = Path(output_folder)

    if not input_path.exists():
        logging.error(f"Input file not found: {input_path}")
        print("Input file not found.")
        return
    
    output_folder.mkdir(parents = True, exist_ok = True)
    dest = output_folder / input_path.name
    shutil.copy(input_path, dest)
    logging.info(f"Copied {input_path} to {dest}")
    print(f"File copied successfully to {dest}")

def main():
    parser = argparse.ArgumentParser(description = "Copy a file and log the operation.")
    parser.add_argument("--input", type = str, required = True, help = "Path to input file")
    parser.add_argument("--output", type = str, required = True, help = "Destination folder")
    args = parser.parse_args()

    copy_file(args.input, args.output)

if __name__ == "__main__":
    main()

