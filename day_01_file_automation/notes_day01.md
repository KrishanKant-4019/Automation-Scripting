# Day 1 – Python File & Folder Automation

## Overview
In **Day 1** of my Automation & Scripting journey, I learned how to make Python directly interact with the file system — creating, organizing, and cleaning folders automatically.  
This day focused on the **foundation of all ML automation workflows**: managing datasets, models, and logs without manual effort.

Every ML pipeline depends on efficient file and folder organization, and automating that process saves both time and reduces human error.  
By the end of this day, I built scripts that can create, clean, and prepare workspace folders programmatically.

---

## What I Learned

- How to use **`os`**, **`pathlib`**, and **`shutil`** for real-world file automation.  
- How to generate complex folder structures using Python scripts.  
- How to delete or clean unwanted files (like `.tmp`, `.bak`, `.log`).
- How to move and copy files across folders efficiently.
- How to initialize data project environments programmatically.

---

## Key Takeaways

- **File automation** is the foundation for reproducible ML and data workflows.  
- **Path handling** with `pathlib` is cleaner, safer, and more readable than legacy `os.path`.  
- Automating folder creation ensures consistency across projects.  
- Scripts can replace repetitive manual setup steps, enabling true workflow automation.

---

## Project Completed: Data Setup Bot (Exercise)

### Objective
To build a **Data Setup Bot** that initializes a daily ML workspace automatically by:
- Creating a new folder named with the current date (e.g., `2025-11-05_run/`)
- Generating subfolders:
  - `raw`
  - `processed`
  - `models`
  - `logs`
- Copying `.csv` files from the `datasets/` folder into `raw/` automatically

This simulates how machine learning pipelines prepare fresh workspaces before data processing or training.

### Features Implemented
- Automatic folder creation using `pathlib`
- File copying automation with `shutil`
- Dynamic naming based on date/time
- Safe folder handling (no overwrite errors)
- Logging of all clean-up actions in a log file

---

## Real-World Relevance

In real-world **MLOps** and **data engineering** systems:
- Each pipeline run creates its own timestamped directory.
- Raw data, logs, and model outputs are stored separately for reproducibility.
- Temporary or redundant files are cleaned up automatically after processing.

This exercise built the foundation of those automation mechanics manually — the same logic that tools like **Airflow**, **Prefect**, or **Luigi** implement at scale.


## How I Run the Script

1. **Navigate to the main directory:**
   ```bash
   cd "C:\Users\krish\OneDrive\Desktop\Automation & Scripting\day_01_file_automation"
````

2. **Run the folder creator:**

   ```bash
   python scripts/folder_creator.py
   ```

3. **Clean temporary files:**

   ```bash
   python scripts/file_cleaner.py
   ```

4. **Run the Data Setup Bot (exercise):**

   ```bash
   python exercise/data_setup_bot.py
   ```

5. **Check output:**

   * A new timestamped folder appears inside `exercise/runs/`.
   * All `.csv` files from `datasets/` are copied into `raw/`.
   * Cleanup logs are stored in `exercise/logs/`.

---

## Complete Folder Structure

day_01_file_automation/
│
├── notes_day01.md
│
├── datasets/
│   ├── data.csv
│   ├── notes.txt
│   └── sales.csv
│
├── exercise/
│   ├── data_setup_bot.py
│   │
│   └── 2025-11-05_run/
│       ├── raw/
│       │   ├── data.csv
│       │   ├── sales.csv
│       │   
│       │
│       ├── processed/
│       ├── models/
│       └── logs/
│
└── scripts/
    ├── folder_creator.py
    ├── file_cleaner.py
    └── project_automation_demo/
        ├── data/
        │   ├── raw/
        │   ├── processed/
        │   
        │
        ├── models/
        ├── logs/
        └── reports/

By completing Day 1, I achieved:

* Full control of file and folder automation using Python.
* Reusable scripts for directory creation and cleanup.
* A working **Data Setup Bot** that automates daily project initialization.
* A structured and professional folder hierarchy ready for future days.

---

