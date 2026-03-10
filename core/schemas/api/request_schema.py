from pydantic import BaseModel, Field

from core.services.contracts import GenerationRequest, TaskType


class GenerationApiRequest(BaseModel):
    provider: str = Field(..., description="Provider key. e.g. veo, kling")
    model_id: str
    task_type: TaskType
    prompt: str | None = None
    image_base64: str | None = None
    image_uri: str | None = None
    image_id: str | None = None
    options: dict = Field(default_factory=dict)

    def to_generation_request(self) -> GenerationRequest:
        return GenerationRequest(
            provider=self.provider,
            model_id=self.model_id,
            task_type=self.task_type,
            prompt=self.prompt,
            image_base64=self.image_base64,
            image_uri=self.image_uri,
            image_id=self.image_id,
            options=self.options,
        )
