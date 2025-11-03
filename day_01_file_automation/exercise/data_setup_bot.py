import shutil
from pathlib import Path
from datetime import date

def data_setup_bot():
    today = date.today().isoformat()
    base_path = Path("automation_learning/day_01_file_automation/exercise") / f"{today}_run"
    base = Path(base_path)
    subfolders = ["raw", "processed", "models", "logs"]

    # Create folder structure
    for sub in subfolders:
        path = base / sub
        path.mkdir(parents = True, exist_ok = True)
        print(f"Created: {path}")

    # Copy CSV files from parent datasets/ to new raw/ folder
    source_folder = Path("automation_learning/day_01_file_automation/datasets")
    target_folder = base / "raw"

    if not source_folder.exists():
        print("Source folder 'datasets/' not found.")
    else:
        csv_files = list(source_folder.glob("*.csv"))
        if not csv_files:
            print("No CSV files found in 'datasets/'")
        else:
            for file in csv_files:
                shutil.copy(file, target_folder)
                print(f"Copied: {file.name} -> {target_folder}")

    print(f"\nData Setup Bot completed! Folder ready at: {base_path}")

if __name__ == "__main__":
    data_setup_bot()





