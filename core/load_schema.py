import json
from pathlib import Path

class Schema:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir/"data"/"schema.json"

        with open(path, "r", encoding="utf-8") as f:
            self.schema = json.load(f)

    def get_categories(self):
        return list(self.schema["category"].keys())

    def get_properties(self, category):
        return list(self.schema["category"][category]["properties"].keys())

    def get_enum(self, category, properties):
        return self.schema["category"][category]["properties"][properties]["enum"]
