import os

import requests
from dotenv import load_dotenv
from core.services.base import VideoProvider

load_dotenv()

class VeoRequestService(VideoProvider):
    def __init__(self, models, headers):
        project_id = os.getenv("PROJECT_ID")
        self.location = "us-central1"
        self.base_url = (
            f"https://{self.location}-aiplatform.googleapis.com/v1/"
            f"projects/{project_id}/locations/{self.location}/"
            f"publishers/google/models/{models}"
        )
        self.headers = headers

    def submit(self, veo_payload):
        res = requests.post(
            f"{self.base_url}:predictLongRunning",
            headers=self.headers,
            json=veo_payload,
            timeout=30,
        )
        res.raise_for_status()
        return res.json()["name"]

    def poll(self, operation_name):
        res = requests.post(
            f"{self.base_url}:fetchPredictOperation",
            headers=self.headers,
            json={"operationName": operation_name},
            timeout=30,
        )
        res.raise_for_status()
        return res.json()

    def result(self, poll_response):
        if not poll_response.get("done"):
            return None

        if "error" in poll_response:
            raise Exception(f"Video generation failed: {poll_response['error']}")

            # Veo의 응답 구조에 따라 response > outputs > 0 > uri 순으로 접근합니다.
        try:
            response_data = poll_response.get("response", {})
            outputs = response_data.get("outputs", [])

            if outputs:
                video_uri = outputs[0].get("uri")
                return video_uri
            return None

        except (KeyError, IndexError):
            return None