import json

class Options():
    def __init__(self, path=r"data/prompts.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.state = json.load(f)

    @property
    def focus(self):
        return self.state.get("focus", {})