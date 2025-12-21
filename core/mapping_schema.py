import json
from pathlib import Path
from core.load_json import Schema, UserPick

class MappingSchema:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir/"data"/"prompt_mapping.json"
        with open(path, "r", encoding="utf-8") as f:
            self.prompt_mapping = json.load(f)

        self.schema = Schema()
        self.user_pick = UserPick()

    @property
    def mapping(self):
        sentences = {}
        user_json = self.user_pick.get_user_pick

        for categories, properties in user_json.items():
            if categories not in self.schema.schema["categories"]:
                continue

            sentences.setdefault(categories, [])

            for property, value in properties.items():
                prompt_map = (
                    self.prompt_mapping.get(categories, {})
                    .get(property, {})
                    .get(value)
                )
                if prompt_map:
                    sentences[categories].append(prompt_map)
        return sentences