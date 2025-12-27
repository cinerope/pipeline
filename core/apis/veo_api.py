from core.prompt.change_to_prompt import Prompt
from typing import Optional
from pydantic import BaseModel, Field

class VeoRequestInstanceImage(BaseModel):
    bytesBase64Encoded: str | None = Field(None)
    mimeType: str | None = Field(None)

class VeoRequestInstance(BaseModel):
    image: VeoRequestInstanceImage | None = Field(None)
    lastFrame: VeoRequestInstanceImage | None = Field(None)
    prompt: str

class VeoRequestParameters(BaseModel):
    aspectRatio: Optional[str] = Field(None, examples=['16:9'])
    durationSeconds: Optional[int] = None
    enhancePrompt: Optional[bool] = None
    generateAudio: Optional[bool] = Field(
        None,
        description='Generate audio for the video. Only supported by veo 3 models.',
    )
    negativePrompt: Optional[str] = None
    personGeneration: str | None = Field(None, description="ALLOW or BLOCK")
    sampleCount: Optional[int] = None
    seed: Optional[int] = None
    storageUri: Optional[str] = Field(
        None, description='Optional Cloud Storage URI to upload the video'
    )
    resolution: str | None = Field(None)

prompt_text = Prompt().json_to_cinematic_prompt()

q = VeoRequestInstance(prompt=prompt_text)
print(q.prompt)