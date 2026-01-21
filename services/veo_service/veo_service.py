from services.get_headers import get_headers_from_key
from services.veo_service.veo_rest import VeoRequestService

class Veo2:
    def __init__(self, key_path):
        # Registry에서 넘겨준 환경변수 경로를 사용합니다.
        self.headers = get_headers_from_key(key_path)
        self.service = VeoRequestService("veo-001", self.headers)

class Veo3:
    def __init__(self, key_path):
        self.headers = get_headers_from_key(key_path)
        self.service = VeoRequestService("veo-3.1-fast-generate-001", self.headers)