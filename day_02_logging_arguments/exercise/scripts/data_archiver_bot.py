import argparse
import logging
from pathlib import Path
import shutil
from datetime import datetime


def create_folder(path):
    folder = Path(path)
    folder.mkdir(parents=True, exist_ok=True)
    print(f"Folder exists: {folder}")
    return folder


def setup_logger():
    logs_dir = create_folder("exercise/logs")
    log_filename = logs_dir / f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("----- Data Archiver Bot Started -----")
    return log_filename


def source_folder(base_path="exercise/source_data"):
    """Create the standard source folder structure for data projects."""
    base = Path(base_path)
    subfolders = ["data/raw", "data/processed", "models", "reports"]

    for sub in subfolders:
        path = base / sub
        create_folder(path)

    print("Source folder structure ensured.")


def archive_files(src, dest, ext, mode="copy"):
    """Copy or move files with the given extension from src to dest."""
    source_path = Path(src)
    dest_path = create_folder(dest)

    if not source_path.exists():
        logging.error(f"Source folder not found: {source_path}")
        print("Source folder not found.")
        return

    files = list(source_path.glob(f"*{ext}"))

    if not files:
        logging.warning(f"No files with extension {ext} found in {source_path}.")
        print(f"No files with extension {ext} found.")
        return

    archived_count = 0
    for file in files:
        try:
            if mode == "move":
                shutil.move(file, dest_path / file.name)
                logging.info(f"Moved: {file.name}")
            else:
                shutil.copy(file, dest_path / file.name)
                logging.info(f"Copied: {file.name}")
            archived_count += 1
        except PermissionError:
            logging.error(f"Permission denied for file: {file}")
        except Exception as e:
            logging.error(f"Error archiving file {file}: {e}")

    logging.info(f"Total files processed ({mode}): {archived_count}")
    print(f"{archived_count} file(s) {mode}d successfully.")
    return archived_count


def main():
    parser = argparse.ArgumentParser(
        description="Data Archiver Bot - Automatically archives files by extensions."
    )
    parser.add_argument("--source", type=str, required=True, help="Folder containing files to archive.")
    parser.add_argument("--dest", type=str, required=True, help="Destination folder for archived files.")
    parser.add_argument("--ext", type=str, required=True, help="File extension to target (e.g., .csv, .txt)")
    parser.add_argument("--mode", type=str, choices=["copy", "move"],default="copy", help="Operation mode: 'copy' (default) or 'move' to transfer files."
    )

    args = parser.parse_args()

    log_file = setup_logger()
    print(f"Logging to: {log_file}")

    source_folder()  # ensure base folders exist
    archive_files(args.source, args.dest, args.ext, args.mode)

    logging.info("----- Data Archiver Bot Finished -----")


if __name__ == "__main__":
    main()
