import asyncio

from core.services.contracts import GenerationJob, JobStatus
from core.services.veo_service.veo_rest import VeoRequestService


def _service() -> VeoRequestService:
    return VeoRequestService(
        models="veo-3.1-fast-generate-001",
        headers={
            "Authorization": "Bearer fake-token",
            "Content-Type": "application/json",
            "X-Goog-User-Project": "test-project",
        },
    )


def test_result_uses_outputs_uri():
    service = _service()

    async def fake_fetch_operation(_):
        return {
            "done": True,
            "response": {"outputs": [{"uri": "gs://cinerope-veo-outputs/veo/a.mp4"}]},
        }

    service._fetch_operation = fake_fetch_operation
    job = GenerationJob(
        provider="veo",
        model_id="veo-3.1-fast-generate-001",
        operation_name="op-1",
        status=JobStatus.SUCCEEDED,
    )

    result = asyncio.run(service.result(job))

    assert result.status == JobStatus.SUCCEEDED
    assert result.output_uri == "gs://cinerope-veo-outputs/veo/a.mp4"


def test_result_uses_videos_gcs_uri():
    service = _service()

    async def fake_fetch_operation(_):
        return {
            "done": True,
            "response": {"videos": [{"gcsUri": "gs://cinerope-veo-outputs/veo/b.mp4"}]},
        }

    service._fetch_operation = fake_fetch_operation
    job = GenerationJob(
        provider="veo",
        model_id="veo-3.1-fast-generate-001",
        operation_name="op-2",
        status=JobStatus.SUCCEEDED,
    )

    result = asyncio.run(service.result(job))

    assert result.status == JobStatus.SUCCEEDED
    assert result.output_uri == "gs://cinerope-veo-outputs/veo/b.mp4"


def test_result_fails_when_uri_missing():
    service = _service()

    async def fake_fetch_operation(_):
        return {
            "done": True,
            "response": {"videos": [{"bytesBase64Encoded": "ZmFrZQ=="}]},
        }

    service._fetch_operation = fake_fetch_operation
    job = GenerationJob(
        provider="veo",
        model_id="veo-3.1-fast-generate-001",
        operation_name="op-3",
        status=JobStatus.SUCCEEDED,
    )

    result = asyncio.run(service.result(job))

    assert result.status == JobStatus.FAILED
    assert result.output_uri is None
    assert result.error is not None
    assert "without output URI" in result.error.message
