from core.prompt.prompt_builder import Prompt

class VeoPromptService:
    def __init__(self):
        self.prompt_builder = Prompt()

        self.system_prompt = f"""
            You are a cinematic video generation model.

            Strictly follow the cinematic instructions below as the highest priority.

            Do not add, remove, or modify any camera angles, shot sizes, lens types,
            camera movements, framing, or focus behavior beyond what is explicitly specified.

            Do not apply any film-style overlays or analog effects.
            Do not add Vignetting, film grain, film borders, vignetting, letterboxing,
            dust, scratches, retro textures, or stylized frames.

            The final result must appear clean, modern, and digital,
            with no artificial framing or film emulation.
            """

    def build(self) -> str:
        return f"{self.system_prompt}\n#{self.prompt_builder.text_to_video()}"
