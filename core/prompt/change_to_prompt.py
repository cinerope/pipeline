from core.prompt.load_json import UserPick

class Prompt:
    def __init__(self):
        user_pick = UserPick()
        self.json_data = user_pick.get_user_pick

    # 자연어로 프롬프트를 작성 (테스트 후 사용여부 결정)
    def json_to_cinematic_prompt(self):
        lines = []

        subject = self.json_data['subject']
        people = subject.get("people", {})
        location = subject.get("location", {})
        action = subject.get("action", {})

        camera = self.json_data.get("camera", {})
        lens = self.json_data.get("lens", {})
        focus = self.json_data.get("focus", {})

        if subject:
            lines.append(f"{people} {action} in {location}.")
        if camera:
            lines.append(
                f"The scene is framed as a {camera['shot size']} shot positioned {camera['position']} the subject."
            )
            lines.append(
                f"The camera performs a {camera['speed']} {camera['movement']} and the camera-to-subject distance is approximately {camera['distance']}."
            )
        if lens:
            lines.append(
                f"The shot is captured with an {lens['focal_length']} lens,"
            )
        if focus:
            lines.append(
                f"with a {focus['depth']} and {focus['type']}."
            )
        return "\n".join(lines)

prompt = Prompt()
print(prompt.json_to_cinematic_prompt())