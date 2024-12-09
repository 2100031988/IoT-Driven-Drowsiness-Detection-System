#!/bin/bash
# Install Python dependencies
python3 -m pip install --user -r requirements.txt

# Download the shape predictor model
python3 download_model.py