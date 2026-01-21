import os
from dotenv import load_dotenv

load_dotenv()
VEO_KEY_PATH = os.getenv("veo-auth-key.json")


class ModelRegistry:
    def __init__(self):
        # 모델 ID와 해당 클래스(혹은 생성 함수)를 매핑합니다.
        self._models = {
            "Veo2" : "veo-2.0-generate-001",
            "Veo3" : "veo-3.0-generate-001",
            "Veo3 fast" : "veo-3.0-fast-generate-001",
            "Veo3 preview" : "veo-3.0-generate-preview",
            "Veo3 fast preview" : "veo-3.0-fast-generate-preview",
            "Veo3.1" : "veo-3.1-generate-001",
            "Veo3.1 fast": "veo-3.1-fast-generate-001"
        }