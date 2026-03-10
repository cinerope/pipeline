import os
import asyncio

import requests
from dotenv import load_dotenv
from core.services.base import VideoProvider
from core.services.contracts import (
    ErrorCode,
    GenerationJob,
    GenerationRequest,
    GenerationResult,
    JobStatus,
    ProviderError,
)
from core.services.veo_service.veo_payload import build_veo_payload

load_dotenv()

class VeoRequestService(VideoProvider):
    def __init__(self, models: str, headers: dict):
        project_id = (
            os.getenv("PROJECT_ID")
            or os.getenv("GOOGLE_PROJECT_ID")
            or headers.get("X-Goog-User-Project")
        )
        if not project_id:
            raise ValueError(
                "Missing project id. Set PROJECT_ID or GOOGLE_PROJECT_ID, "
                "or provide X-Goog-User-Project in headers."
            )
        self.location = "us-central1"
        self.model_id = models
        self.base_url = (
            f"https://{self.location}-aiplatform.googleapis.com/v1/"
            f"projects/{project_id}/locations/{self.location}/"
            f"publishers/google/models/{models}"
        )
        self.headers = headers

    async def submit(self, request: GenerationRequest) -> GenerationJob:
        veo_payload = build_veo_payload(request)
        res = await asyncio.to_thread(
            requests.post,
            f"{self.base_url}:predictLongRunning",
            headers=self.headers,
            json=veo_payload,
            timeout=30,
        )
        res.raise_for_status()
        operation_name = res.json()["name"]
        return GenerationJob(
            provider=request.provider,
            model_id=request.model_id,
            operation_name=operation_name,
            status=JobStatus.QUEUED,
        )

    async def _fetch_operation(self, operation_name: str) -> dict:
        res = await asyncio.to_thread(
            requests.post,
            f"{self.base_url}:fetchPredictOperation",
            headers=self.headers,
            json={"operationName": operation_name},
            timeout=30,
        )
        res.raise_for_status()
        return res.json()

    async def poll(self, job: GenerationJob) -> GenerationJob:
        poll_response = await self._fetch_operation(job.operation_name)
        if poll_response.get("done"):
            if "error" in poll_response:
                return job.model_copy(update={"status": JobStatus.FAILED})
            return job.model_copy(update={"status": JobStatus.SUCCEEDED})
        return job.model_copy(update={"status": JobStatus.RUNNING})

    async def result(self, job: GenerationJob) -> GenerationResult:
        poll_response = await self._fetch_operation(job.operation_name)
        if not poll_response.get("done"):
            return GenerationResult(
                provider=job.provider,
                model_id=job.model_id,
                status=JobStatus.RUNNING,
            )

        if "error" in poll_response:
            return GenerationResult(
                provider=job.provider,
                model_id=job.model_id,
                status=JobStatus.FAILED,
                error=ProviderError(
                    code=ErrorCode.PROVIDER_ERROR,
                    message="Video generation failed",
                    provider=job.provider,
                    raw=poll_response.get("error"),
                ),
            )

        response_data = poll_response.get("response", {})
        outputs = response_data.get("outputs", [])
        output_uri = outputs[0].get("uri") if outputs else None
        if not output_uri:
            videos = response_data.get("videos", [])
            output_uri = videos[0].get("gcsUri") if videos else None

        if not output_uri:
            return GenerationResult(
                provider=job.provider,
                model_id=job.model_id,
                status=JobStatus.FAILED,
                error=ProviderError(
                    code=ErrorCode.PROVIDER_ERROR,
                    message="Video generation completed without output URI. Set storageUri to a valid gs:// path.",
                    provider=job.provider,
                    raw=response_data,
                ),
            )

        return GenerationResult(
            provider=job.provider,
            model_id=job.model_id,
            status=JobStatus.SUCCEEDED,
            output_uri=output_uri,
        )
