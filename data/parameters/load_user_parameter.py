import json
from pathlib import Path

class UserParameter:
    @property
    def get_user_parameter(self):
        base_dir = Path(__file__).resolve().parent.parent.parent
        path = base_dir/"data"/"user_parameters.json"
        with open(path, "r", encoding="utf-8") as f:
            user_parameters = json.load(f)

        return user_parameters