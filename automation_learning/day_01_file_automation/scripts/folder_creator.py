from pathlib import Path

def create_project_structure(base_path = "project_automation_demo"):
    base = Path(base_path)
    subfolders = ["data/raw", "data/processed", "models", "logs", "reports"]

    for sub in subfolders:
        path = base / sub
        path.mkdir(parents = True, exist_ok = True)
        print(f"Created: {path}")

    print("Folder structure ready!")

if __name__ == "__main__":
    create_project_structure()