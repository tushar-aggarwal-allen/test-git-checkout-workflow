#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate the virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Run the Python script using the venv's Python
"$SCRIPT_DIR/venv/bin/python" "$SCRIPT_DIR/test.py" "$@"
