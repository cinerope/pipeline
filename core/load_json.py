import json
from pathlib import Path

class Schema:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir/"data"/"schema.json"

        with open(path, "r", encoding="utf-8") as f:
            self.schema = json.load(f)

    # focus, shot, lens, camera
    def get_categories(self):
        return list(self.schema.get("categories", {}).keys())

    def get_properties(self, categories):
        return list(self.schema["camera"][categories]["properties"].keys())

    def get_enum(self, categories, properties):
        return list(self.schema["camera"][categories]["properties"][properties]["enum"].keys())

class UserPick:
    @property
    def get_user_pick(self):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir / "data" / "test.json"

        with open(path, "r", encoding="utf-8") as f:
            test_json = json.load(f)
        return test_json