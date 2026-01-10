from data.parameters.parameter_loader import UserParameterAccessor

class Prompt:
    def __init__(self):
        self.cinerope_parameters = UserParameterAccessor().cinerope_parameters

    # 자연어로 프롬프트를 작성 (테스트 후 사용여부 결정)
    def text_to_video(self):
        lines = []
        camera = self.cinerope_parameters.get("camera", {})
        if camera:
            lines.append(
                f"A {camera['shot_size']} shot, with the camera {camera['speed']} {camera['movement']} {camera['position']} the subject."
            )
            lines.append(
                f"And the camera-to-subject distance is approximately {camera['distance']}."
            )

        lens = self.cinerope_parameters.get("lens", {})
        if lens:
            lines.append(
                f"The shot is captured with an {lens['focal_length']} lens,"
            )

        focus = self.cinerope_parameters.get("focus", {})
        if focus:
            lines.append(
                f"with a {focus['depth']} and {focus['type']}."
            )

        subject = self.cinerope_parameters.get('subject', {})
        people = subject.get("people", {})
        location = subject.get("location", {})
        action = subject.get("action", {})
        if subject:
            lines.append(f"{people} {action} in {location}.")

        return "\n".join(lines)