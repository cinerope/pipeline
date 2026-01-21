import os
from dotenv import load_dotenv

from google import genai
from google.genai.types import HttpOptions, GenerateContentConfig

load_dotenv()

class GeminiApi:
    def __init__(self):
        self.client = genai.Client(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location=os.getenv("GOOGLE_LOCATION"),
            http_options=HttpOptions(api_version="v1")
        )

    async def generate(
        self,
        model: str,
        contents: str,
        config: GenerateContentConfig
    ):
        return self.client.models.generate_content(
            model=model,
            contents=contents,
            config=config
        )

    def get_operation(self, operation):
        return self.client.operations.get(operation)