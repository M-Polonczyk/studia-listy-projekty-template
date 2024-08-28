"""Script for creating a virtual environment with pip."""

import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)
PYTHON_PROJECT_PATH = "python_projects"

# Get the current script directory
script_directory = os.path.dirname(os.path.realpath(__file__))
proj_path = os.path.join(script_directory, PYTHON_PROJECT_PATH)

if not os.path.exists(proj_path):
    logging.info("Creating projects directory with virtual environment.")
    os.mkdir(proj_path)

# Set the path for the virtual environment
venv_path = os.path.join(proj_path, ".venv")

# Check if requirements.txt file exists
requirements_file = (
    os.path.join(script_directory, "requirements.txt")
    if os.path.exists("requirements.txt")
    else os.path.join(proj_path, "requirements.txt")
)

logging.info("creating virtual environment...")

# Create virtual environment
# If error occurs, replace 'python' with 'python3'
subprocess.run(["python3", "-m", "venv", venv_path], check=True)

if os.path.exists(requirements_file):
    logging.info('run "pip install -r requirements.txt" to install required packages.')
else:
    with open(requirements_file, "w", encoding="utf-8") as file:
        file.write("# Write to this file with 'pip freeze > requirements.txt'")
    logging.info("Created requirements.txt file in %s.", proj_path)

logging.info(
    "Virtual environment created and dependencies installed. Store .py files in '%s' directory.",
    PYTHON_PROJECT_PATH,
)
