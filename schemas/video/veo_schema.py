from pydantic import BaseModel, Field

class VeoImageInstance(BaseModel):
    bytesBase64Encoded : str | None = Field(None)
    gcsUri : str | None = Field(None)
    mimeType : str | None = Field(None)             # jpeg or png

class VeoVideoInstance(BaseModel):
    gcsUri : str | None = Field(None)
    mimeType : str | None = Field(None)

class VeoFirstLastFrameImageInstance(BaseModel):
    image : VeoImageInstance | None = Field(None)
    lastFrame : VeoImageInstance | None = Field(None)

class VeoReferenceImageInstance(BaseModel):         # veo-2.0-generate-exp 및 veo-3.1-generate-preview에서만 지원
    image : VeoImageInstance | None = Field(None)
    referenceType : str | None = Field(None)        # asset

class VeoVideoInsertObjectInstance(BaseModel):
    mask : VeoImageInstance | None = Field(None)
    maskMode : str | None = Field(None)             # insert
    video : VeoVideoInstance | None = Field(None)

class VeoRequestParameters(BaseModel):
    sampleCount: int | None = Field(1)  # 한 번에 만들 영상 개수
    aspectRatio: str | None = Field(
        None, examples=["16:9", "9:16"]
    )                                               # 해상도
    compressionQuality: str | None = Field(
        None, examples=["optimized","lossless"])    # 영상 품질
    durationSeconds: int | None = Field(None,le=8)  # 생성할 영상 시간 | Veo2 5~8, Veo3 4,6,8
    enhancePrompt: bool | None = Field(None)        # gemini 사용 프롬프트 개선 | Veo2 전용
    generateAudio: bool | None = Field(None)        # 오디오 생성 여부 | Veo3 전용
    negativePrompt: str | None = Field(None)        # 영상 내부 제외사항
    personGeneration: str | None = Field(
        None,examples=["allow_adult" , "dont_allow", "allow_all"]
    )                                               # 얼굴 생성 허용 여부
    resizeMode: str | None = Field(
        None, examples= ["pad", "crop"]
    )                                               # 이미지의 크기와 영상 사이즈의 설정 | Veo3 image-to-video 전용
    resolution: str | None = Field(
        None, examples=["720p", "1080p"]
    )                                               # 해상도 | Veo3 전용
    seed: int | None = Field(
        None, ge=0, le=4294967295
    )                                               # 일관성을 위한 seed
    storageUri: str | None = Field(
        None,
        description="GCS bucket uri"
    )                                               #GCS 버킷 주소