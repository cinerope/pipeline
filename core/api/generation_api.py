import os

from core.schemas.api.request_schema import GenerationApiRequest
from core.services.contracts import GenerationJob, JobStatus
from core.services.get_headers import get_headers_from_key
from core.services.veo_service.veo_rest import VeoRequestService


def _resolve_headers(options: dict) -> dict:
    direct_headers = options.get("headers")
    if isinstance(direct_headers, dict):
        return direct_headers

    key_path = options.get("key_path") or os.getenv("VEO_KEY_PATH") or os.getenv(
        "GOOGLE_APPLICATION_CREDENTIALS"
    )
    if not key_path:
        raise ValueError(
            "Missing auth headers. Provide options.headers or options.key_path/env key path."
        )
    return get_headers_from_key(key_path)


async def generate_from_api_request(payload: dict) -> dict:
    api_request = GenerationApiRequest(**payload)
    request = api_request.to_generation_request()

    if request.provider != "veo":
        raise ValueError(f"Unsupported provider: {request.provider}")

    options = request.options or {}
    service = VeoRequestService(models=request.model_id, headers=_resolve_headers(options))

    mock_poll_response = options.get("mock_poll_response")
    if isinstance(mock_poll_response, dict):
        operation_name = options.get("mock_operation_name", "mock-operation")
        job = GenerationJob(
            provider=request.provider,
            model_id=request.model_id,
            operation_name=operation_name,
            status=JobStatus.QUEUED,
        )
        if mock_poll_response.get("done"):
            if "error" in mock_poll_response:
                polled_job = job.model_copy(update={"status": JobStatus.FAILED})
                return {
                    "status": polled_job.status.value,
                    "operation_name": polled_job.operation_name,
                    "output_uri": None,
                    "error": mock_poll_response.get("error"),
                }
            outputs = mock_poll_response.get("response", {}).get("outputs", [])
            output_uri = outputs[0].get("uri") if outputs else None
            polled_job = job.model_copy(update={"status": JobStatus.SUCCEEDED})
            return {
                "status": polled_job.status.value,
                "operation_name": polled_job.operation_name,
                "output_uri": output_uri,
                "error": None,
            }

        polled_job = job.model_copy(update={"status": JobStatus.RUNNING})
        return {
            "status": polled_job.status.value,
            "operation_name": polled_job.operation_name,
            "output_uri": None,
            "error": None,
        }

    job = await service.submit(request)
    polled_job = await service.poll(job)
    result = await service.result(polled_job)
    return {
        "status": result.status.value,
        "operation_name": polled_job.operation_name,
        "output_uri": result.output_uri,
        "error": result.error.model_dump() if result.error else None,
    }
