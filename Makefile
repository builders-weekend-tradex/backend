# Makefile for setting up a virtual environment, installing dependencies, and running the FastAPI server

## If on windows to activate run this
# VENV_ACTIVATE= source venv/Scripts/activate
## If on mac or linux run this command
# VENV_ACTIVATE= source venv/bin/activate

# Virtual environment name
PY=python3
VENV=venv
BIN= source $(VENV)/bin/activate

# Make it work on Windows
ifeq ($(OS), Windows_NT)
	# For Windows, activate the virtual environment differently
	BIN= $(VENV)\\Scripts\\activate
	PY=py
endif

# Create virtual environment
venv:
	$(PY) -m venv $(VENV)

# Install dependencies from requirements.txt
install: venv
	$(BIN) && pip install -r requirements.txt

# Run the FastAPI server
runserver:
	$(BIN) && fastapi dev main.py

# Run tests using pytest
test: venv
	$(BIN) && pytest

# Clean up virtual environment and any other generated files
clean:
	rm -rf $(VENV)

# Generate requirements.txt from installed packages
freeze: venv
	$(BIN) && pip freeze > requirements.txt

# Define default target
.DEFAULT_GOAL := help

# Display help message
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  venv        to create a virtual environment"
	@echo "  install     to install dependencies"
	@echo "  run         to run the FastAPI server"
	@echo "  clean       to clean up the virtual environment"
	@echo "  freeze      to update requirements.txt"
	@echo "  test        to run all tests using pytest"