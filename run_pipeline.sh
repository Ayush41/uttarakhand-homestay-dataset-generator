#!/bin/bash

set -e

echo "Setting up environment..."
python -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating dataset..."
python generate_dataset.py

echo "Done ✔ Dataset created"
echo "Flexing my bash skills "