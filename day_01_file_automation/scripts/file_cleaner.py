import os
import shutil
from pathlib import Path

def clean_temp_files(folder = "datasets", extensions = (".tmp", ".log", ".bak")):
    folder_path = Path(folder)
    if not folder_path.exists():
        print("Folder not found.")
        return
    
    removed = 0
    for file in folder_path.glob("*"):
        if file.suffix in extensions:
            file.unlink()
            removed += 1
        elif file.isdir() and file.name.lower() == "temp":
            shutil.rmtree(file)
            removed += 1

    print(f"🧹 Cleaned {removed} unwanted files/folders from {folder_path}")

if __name__ == "__main__":
    clean_temp_files()