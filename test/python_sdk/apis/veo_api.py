import os
from dotenv import load_dotenv

from google import genai
from google.genai.types import HttpOptions, GenerateVideosConfig, Image

load_dotenv()

class VeoApi:
    def __init__(self):
        self.client = genai.Client(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location=os.getenv("GOOGLE_LOCATION"),
            http_options=HttpOptions(api_version="v1")
        )

    async def generate(
        self,
        model: str,
        prompt: str,
        config: GenerateVideosConfig,
        image: Image | None = None
    ):
        return self.client.models.generate_videos(
            model=model,
            prompt=prompt,
            image=image,
            config=config
        )

    def get_operation(self, operation):
        return self.client.operations.get(operation)