"""Script for creating a virtual environment with pip."""
import logging
import os
import subprocess
import sys

logging.basicConfig(level=logging.INFO)

# Get the current script directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the path for the virtual environment
venv_path = os.path.join(script_directory, "venv")

# Check if requirements.txt file exists
requirements_file = os.path.join(script_directory, "requirements.txt")

# Create virtual environment
subprocess.run(["python", "-m", "venv", venv_path], check=True)

if not os.path.exists(requirements_file):
    logging.info("requirements.txt file not found.")
    sys.exit(0)

# Activate virtual environment
activate_script = os.path.join(
    venv_path, "Scripts" if os.name == "nt" else "bin", "activate"
)
subprocess.run([activate_script], check=True)

# Install dependencies from requirements.txt
subprocess.run(["pip", "install", "-r", requirements_file], check=True)

logging.info("Virtual environment created and dependencies installed.")


