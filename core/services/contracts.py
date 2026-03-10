from enum import Enum
from pydantic import BaseModel, Field


class TaskType(str, Enum):
    TEXT_TO_VIDEO = "text_to_video"
    IMAGE_TO_VIDEO = "image_to_video"


class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class ErrorCode(str, Enum):
    AUTH_ERROR = "auth_error"
    RATE_LIMITED = "rate_limited"
    INVALID_INPUT = "invalid_input"
    PROVIDER_ERROR = "provider_error"
    TIMEOUT = "timeout"


class ProviderError(BaseModel):
    code: ErrorCode
    message: str
    provider: str
    raw: dict | None = None


class GenerationRequest(BaseModel):
    provider: str = Field(..., description="Provider key. e.g. veo, kling")
    model_id: str
    task_type: TaskType
    prompt: str | None = None
    image_base64: str | None = None
    image_uri: str | None = None
    image_id: str | None = None
    options: dict = Field(default_factory=dict)


class GenerationJob(BaseModel):
    provider: str
    model_id: str
    operation_name: str
    status: JobStatus = JobStatus.QUEUED


class GenerationResult(BaseModel):
    provider: str
    model_id: str
    status: JobStatus
    output_uri: str | None = None
    error: ProviderError | None = None
