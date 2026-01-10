import os
from dotenv import load_dotenv

from google import genai
from google.genai.types import HttpOptions, GenerateImagesConfig

load_dotenv()

class ImagenApi:
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
        config: GenerateImagesConfig
    ):
        return self.client.models.generate_images(
            model=model,
            prompt=prompt,
            config=config
        )

    def get_operation(self, operation):
        return self.client.operations.get(operation)