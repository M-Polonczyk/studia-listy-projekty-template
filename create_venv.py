"""Script for creating a virtual environment with pip."""
import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)

# Get the current script directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the path for the virtual environment
venv_path = os.path.join(script_directory, "python_venv")

# Check if requirements.txt file exists
requirements_file = os.path.join(script_directory, "requirements.txt")

logging.info("creating virtual environment...")
# Create virtual environment
subprocess.run(["python", "-m", "venv", venv_path], check=True)

if os.path.exists(requirements_file):
    logging.info('run "pip install -r requirements.txt" to install required packages.')

logging.info("Creating projects directory in virtual environment.")
os.mkdir(os.path.join(venv_path, "projects"))

logging.info(
    'Virtual environment created and dependencies installed. Store .py files in "projects" directory.'
)
