"""Handles saving and loading data to and from JSON files."""
import json
import os

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "songs.json")

def save_data(data):
    """Saves a list of dictionaries to the JSON file."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    """Loads data from the JSON file. Returns an empty list if not found."""
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
