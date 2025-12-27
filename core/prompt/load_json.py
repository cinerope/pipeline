import json
from pathlib import Path

class Schema:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir/"data"/"schema.json"

        with open(path, "r", encoding="utf-8") as f:
            self.schema = json.load(f)

    # 파라미터의 상위 값들 subject, shot, lens, focus, movement, video
    def get_categories(self):
        return list(self.schema.get("categories", {}).keys())

    # 선택 한 파라미터들의 속성값들 ex) shot: [size: close-up]
    def get_properties(self, categories):
        return list(self.schema["categories"].get(categories).items())

class UserPick:
    #유저가 선택한 파라미터
    @property
    def get_user_pick(self):
        base_dir = Path(__file__).resolve().parent.parent.parent
        path = base_dir / "data" / "test.json"

        with open(path, "r", encoding="utf-8") as f:
            test_json = json.load(f)
        return test_json