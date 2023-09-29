#!/usr/bin/env bash

# This script is used to ensure that the local virtualenv exactly matches the requirements.txt file.
# To generate the requirements.txt file, run `pip freeze > requirements.txt` from the root of the project.

# cd to the directory one higher than this script
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Ensure we are running in a virtual environment
if [ -z "${VIRTUAL_ENV}" ]; then
    echo "Please run this script from within a virtual environment." >&2
    echo "To create a virtual environment, run:" >&2
    echo "    python -m venv venv" >&2
    exit 1
fi

# If pip-sync is not installed, install it
if ! command -v pip-sync &> /dev/null; then
    pip install pip-tools
fi

# Run pip-sync to ensure the virtualenv exactly matches the requirements.txt file
pip-sync requirements.txt
