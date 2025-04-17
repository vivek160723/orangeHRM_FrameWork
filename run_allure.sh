#!/bin/bash
echo "Running All Tests with Allure Reporting..."
pytest tests/ --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
