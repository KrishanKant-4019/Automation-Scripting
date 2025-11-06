# Day 3 – Shell Scripting for ML Automation

## Overview
In **Day 3** of my Automation & Scripting journey, I learned how to orchestrate multiple Python scripts into a single **automated ML pipeline** using **Shell Scripting (Bash)**.  
This day was about teaching my system to *coordinate tasks automatically* — turning independent scripts into a seamless workflow that runs from start to finish with a single command.

By combining Python and Bash, I built the foundation of true **workflow automation**, similar to what happens in real **MLOps pipelines**.

---

## What I Learned

- Created and executed **`.sh` (Bash)** shell scripts for automation.
- Combined multiple Python scripts (`folder_creator.py`, `file_cleaner.py`, `arg_logger.py`) into a single workflow.
- Used **`mkdir -p`** to automatically create missing directories.
- Implemented **`set -e`** to make the script stop immediately on any error.
- Understood **relative path management** (`../`) between projects.
- Debugged real-world environment issues between **PowerShell**, **Git Bash**, and **Anaconda**.
- Built a **self-healing, fault-tolerant pipeline** capable of running end-to-end.

---

## Key Takeaways

- **Shell scripting** ties together your Python automation scripts into complete pipelines.
- **Error handling (`set -e`)** ensures the pipeline halts safely when something fails.
- **Directory creation (`mkdir -p`)** prevents path-related crashes.
- **Relative paths** improve portability and reusability.
- This marks the transition from **script-level automation** to **workflow orchestration**, a key MLOps concept.

---

## Project: ML Automation Pipeline

### Objective
To create a **Shell Script (`automate_ml.sh`)** that automates an ML workflow by chaining together scripts from previous days.

### Features
- Executes multiple Python scripts in sequence:
  - **Day 1:** Folder creation (`folder_creator.py`)
  - **Day 1:** File cleanup (`file_cleaner.py`)
  - **Day 2:** Dataset copying and logging (`arg_logger.py`)
- Automatically creates required directories before execution.
- Uses **structured progress messages** for better readability.
- Stops the process if any command fails using `set -e`.
- Provides a clean, professional-style ML automation pipeline.

### Purpose
To build a working example of **workflow orchestration**, where multiple tasks — data setup, cleaning, and logging — are chained together under one command.

---

## Real-World Application

In real **Machine Learning** and **Data Engineering** environments:
- Shell scripts serve as the **entry point** to data pipelines.
- They can trigger:
  - Data fetching
  - Preprocessing
  - Model training
  - Evaluation and reporting
- The same principles used here scale up in tools like **Apache Airflow**, **Prefect**, and **Dagster**.

This project mirrors how production pipelines automate and coordinate data workflows.

---

## How I Run the Script

### Step 1 — Open Terminal and Navigate
```bash
cd "C:\Users\krish\OneDrive\Desktop\Automation & Scripting\day_03_shell_scripting"
````

### Step 2 — Run the Automation Script

```bash
bash shell_scripts/automate_ml.sh
```

### Step 3 — Observe the Output

Each stage (folder creation, cleanup, dataset copy) runs in sequence with clear terminal messages.

---

## Script Used

**File:** `automate_ml.sh`

```bash
#!/bin/bash
set -e

echo "Starting ML automation pipeline..."
echo "----------------------------------"

echo "Creating folder structure..."
python ../day_01_file_automation/scripts/folder_creator.py

mkdir -p logs
mkdir -p ../day_01_file_automation/datasets
mkdir -p ../day_01_file_automation/datasets/processed

echo "Cleaning temporary files..."
python ../day_01_file_automation/scripts/file_cleaner.py

echo "Copying dataset..."
python ../day_02_logging_arguments/scripts/arg_logger.py \
  --input ../day_01_file_automation/datasets/data.csv \
  --output ../day_01_file_automation/datasets/processed/

echo "All tasks completed successfully!"
echo "--------------------------------------"
```

---

## Mini-Project: `data_preprocess_run.sh`

### Objective

To build a **custom shell pipeline** that automates a simple data preprocessing workflow with timestamps and logging.

### Steps

1. **Create a dated folder** (e.g., `2025-11-04_run/`) using a Python script.
2. **Copy the dataset** into this new folder automatically.
3. **Log all operations** using your **Day 2 logger script (`arg_logger.py`)**.
4. **Print timestamps** before and after each operation to measure duration.

### Example Implementation

**File:** `data_preprocess_run.sh`

```bash
#!/bin/bash
set -e

start_time=$(date)
echo "Process started at: $start_time"
echo "----------------------------------"

run_folder=$(date +%Y-%m-%d_run)
mkdir -p runs/$run_folder/raw
mkdir -p runs/$run_folder/processed

echo "Created run folder: runs/$run_folder"

echo "Copying dataset..."
python ../day_02_logging_arguments/scripts/arg_logger.py \
  --input ../day_01_file_automation/datasets/data.csv \
  --output runs/$run_folder/raw/

echo "Data copied successfully!"

end_time=$(date)
echo "----------------------------------"
echo "Process completed at: $end_time"
```

### Purpose

This exercise builds your **first end-to-end ML workflow**, where:

* Every run creates a fresh timestamped folder.
* Data is processed, copied, and logged automatically.
* The entire sequence executes from one command — a prototype of a pipeline orchestrator.

---

## Sample Output

```
Starting ML automation pipeline...
----------------------------------
Creating folder structure...
Created: project_automation_demo\data\raw
Created: project_automation_demo\data\processed
Created: project_automation_demo\models
Created: project_automation_demo\logs
Created: project_automation_demo\reports
Folder structure ready!
Cleaning temporary files...
Folder not found.
Copying dataset...
File copied successfully to ..\day_01_file_automation\datasets\processed\data.csv
All tasks completed successfully!
--------------------------------------
```

---

## Complete Folder Structure

```
day_03_shell_scripting/
│
├── README.md
│
├── shell_scripts/
│   ├── automate_ml.sh
│   └── data_preprocess_run.sh
│
├── project_automation_demo/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── logs/
│   ├── models/
│   └── reports/
│
└── logs/
    └── arg_logger.log
```

---

## Outcome

By the end of Day 3, I successfully:

* Built a complete **automation pipeline** connecting all previous projects.
* Created a **custom shell pipeline (`data_preprocess_run.sh`)** with timestamps and logs.
* Automated folder creation, file cleaning, and dataset processing.
* Learned **error handling**, **path control**, and **cross-script execution**.
* Created a workflow that mirrors real-world **ML pipeline orchestration**.

---

