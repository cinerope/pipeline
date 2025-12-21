from core.mapping_schema import MappingSchema

class Prompt:
    def __init__(self):
        self.mapping_data = MappingSchema().mapping

    def build_prompt(self):
        prompt = []

        shot = self.mapping_data.get("shot", [])
        lens = self.mapping_data.get("lens", [])
        camera = self.mapping_data.get("camera", [])
        focus = self.mapping_data.get("focus", [])

        if shot or lens:
            prompt.append("A cinematic " + ", ".join(shot + lens) + ".")
        if camera:
            prompt.append("The camera " + ", ".join(camera)+ ".")
        if focus:
            prompt.append("The focus " + ", ".join(focus)+ ".")

        return "\n".join(prompt)