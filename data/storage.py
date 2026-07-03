"""
Module: data.storage
Purpose: Handles saving and loading the athlete's data using JSON.
"""

import json

class DataStorage:
    """Manages reading and writing user data to a JSON file."""

    def __init__(self, filename="user_profile.json"):
        self.filename = filename

    def load_data(self):
        """
        Loads data from the JSON file. Returns an empty dict if the file is missing or corrupted.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self, data):
        """
        Overwrites the JSON file with the updated data dictionary.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)