set -e

echo "Starting ML automation pipeline..."
echo "----------------------------------"

echo "Creating folder structure..."
python ../day_01_file_automation/scripts/folder_creator.py

mkdir -p logs
mkdir -p ../day_01_file_automation/datasets/processed

echo "Cleaning temporary files..."
python ../day_01_file_automation/scripts/file_cleaner.py

echo "Copying dataset..."
python ../day_02_logging_arguments/scripts/arg_logger.py \
  --input ../day_01_file_automation/datasets/data.csv \
  --output ../day_01_file_automation/datasets/processed/

echo "All tasks completed successfully!"
echo "--------------------------------------"
