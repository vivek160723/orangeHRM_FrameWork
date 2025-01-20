#!/bin/bash

# Set the virtual environment path
VENV_PATH="./venv/bin/activate"

# Activate the virtual environment
if [ -f "$VENV_PATH" ]; then
    echo "Activating virtual environment..."
    source "$VENV_PATH"
else
    echo "Virtual environment not found. Please create it first."
    exit 1
fi

# Navigate to the project directory (ensure script is run from the project root)
cd "$(dirname "$0")"

# Clear previous reports (optional)
echo "Clearing old reports..."
rm -rf reports/allure_reports
rm -rf reports/html_reports

# Run tests with Pytest and generate HTML and Allure reports
echo "Running tests and generating reports..."
pytest --html=reports/html_reports/test_report.html --self-contained-html --alluredir=reports/allure_reports

# Generate Allure report (requires Allure to be installed)
echo "Generating Allure report..."
allure generate reports/allure_reports -o reports/allure_reports/html --clean

# Open the Allure report in browser (optional)
echo "Opening Allure report in browser..."
allure open reports/allure_reports/html

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Test execution completed."
