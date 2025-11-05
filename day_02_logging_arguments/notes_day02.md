# Day 2 – Command-Line Arguments & Logging

## Overview
In **Day 2** of my Automation & Scripting journey, I focused on transforming my Python scripts into **dynamic**, **reusable**, and **traceable automation tools**.  
I learned how to use **command-line arguments** to make my scripts flexible and **logging** to record each operation automatically.  

This day was about teaching my scripts not just to *act*, but also to *listen* and *remember* — making them truly production-ready.

---

## What I Learned

- Implemented **`argparse`** to pass runtime arguments like file paths, file extensions, and modes of operation.
- Used **`logging`** to generate clean, timestamped logs instead of relying on print statements.
- Designed a modular automation script that adapts dynamically to user inputs.
- Understood how folder structures support maintainable automation workflows.
- Gained experience in handling missing folders, permissions, and dynamic file creation.

---

## Key Takeaways

- **Command-line arguments** make automation scripts flexible and reusable without editing code.
- **Logging** enables monitoring, debugging, and auditability in real-world workflows.
- **Folder organization** is critical for scaling projects across different stages (data, models, logs, etc.).
- Combining both techniques leads to robust, production-style Python scripts.

---

## Project: Data Archiver Bot

### Objective
To build a **Data Archiver Bot** that automatically copies or moves files based on their extensions while logging each operation.

### Features
- Takes user-defined arguments:
  - `--source`: Source folder containing files.
  - `--dest`: Destination folder for processed files.
  - `--ext`: File extension to target (e.g., `.csv`).
  - `--mode`: Operation type (`copy` or `move`).
- Automatically creates missing folders before processing.
- Generates log files with detailed status and timestamps.
- Handles missing paths and permission errors gracefully.
- Supports both **copying** and **moving** file operations.

### Purpose
This bot represents a real-world automation pattern found in data pipelines —  
taking input, processing it, and logging all actions — ensuring both scalability and traceability.

---

## Real-World Application

In production workflows, especially in **Machine Learning** and **Data Engineering**:
- **Logging** provides transparency and debugging insights.
- **Argument parsing** allows the same script to process different datasets or projects.
- These practices are the foundation of reproducible, modular, and auditable systems.

Example ML use cases:
- Data preprocessing with different datasets.
- Logging model training and evaluation metrics.
- Managing data file movements across environments.

---


## How I Run the Script

### Step 1 — Open Terminal and Navigate
```bash
cd "C:\Users\krish\OneDrive\Desktop\Automation & Scripting\day_02_logging_automation"
````

### Step 2 — Run the Bot

```bash
python exercise/scripts/data_archiver_bot.py --source exercise/source_data/data/raw --dest exercise/source_data/data/processed --ext .csv --mode copy
```

### Step 3 — View Logs

Each run creates a log file inside:

```
exercise/logs/archive_YYYYMMDD_HHMMSS.log
```

### Step 4 — Check Archived Files

Processed or moved files appear inside:

```
exercise/source_data/data/processed/
```

---

## Logs Example

A sample log file (`archive_20251106_143030.log`) contains:

```
2025-11-06 14:30:30,042 - INFO - ----- Data Archiver Bot Started -----
2025-11-06 14:30:30,045 - INFO - Copied: sample1.csv
2025-11-06 14:30:30,046 - INFO - Copied: sample2.csv
2025-11-06 14:30:30,048 - INFO - Total files processed (copy): 2
2025-11-06 14:30:30,050 - INFO - ----- Data Archiver Bot Finished -----
```

---

## Complete Folder Structure

day_02_logging_automation/
│
├── README.md                                
│
├── datasets/                                
│
├── logs/
│   └── arg_logger.log                       
│
├── scripts/
│   └── arg_logger.py                         
│
└── exercise/
    ├── README.md                            
    │
    ├── logs/
    │   ├── archive_YYYYMMDD_HHMMSS.log      
    │   └── ...
    │
    ├── scripts/
    │   └── data_archiver_bot.py           
    │
    ├── source_data/
    │   ├── data/
    │   │   ├── raw/                         
    │   │   │   ├── sample1.csv
    │   │   │   ├── sample2.csv
    │   │   │   └── ...
    │   │   └── processed/                 
    │   │       ├── sample1.csv
    │   │       ├── sample2.csv
    │   │       └── ...
    │   │
    │   ├── models/                         
    │   └── reports/                         
```

---

## Outcome

By the end of Day 2, I successfully:

* Created a fully functional **Data Archiver Bot** with both copy and move modes.
* Implemented command-line arguments using `argparse`.
* Set up logging to record detailed execution data.
* Organized a clean, scalable project folder structure.
* Learned the fundamentals of making scripts modular, reusable, and production-ready.

---

