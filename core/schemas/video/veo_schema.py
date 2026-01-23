from pydantic import BaseModel, Field, ConfigDict

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
    model_config = ConfigDict(populate_by_name=True)

    sampleCount: int | None = Field(
        1,
        ge=1, le=4, alias="sample_count",
        json_schema_extra = {"ui_label": "Sample Count"}
    )

    aspectRatio: str | None = Field(
        "16:9",
        alias="aspect_ratio", examples=["16:9", "9:16"],
        json_schema_extra={"ui_label": "Aspect Ratio"}

    )

    compressionQuality: str | None = Field(
        "optimized",
        alias="compression_quality", examples=["optimized", "lossless"],
        json_schema_extra={"ui_label": "Compression Quality",}
    )

    durationSeconds: int | None = Field( # 생성할 영상 시간 | Veo2 5~8, Veo3 4,6,8 | default : 8
        8,
        alias="duration", ge=4, le=8,
        json_schema_extra={
            "ui_label": "Duration",
            "ui_widget": "SLIDER",
            "min": 4,
            "max": 8
        }
    )

    enhancePrompt: bool | None = Field( # gemini 사용 프롬프트 개선 | Veo2 전용
        False, alias="enhance_prompt",
        json_schema_extra={"ui_label": "Enhance Prompt"}
    )

    generateAudio: bool | None = Field(
        True, alias="generate_audio",
        json_schema_extra={"ui_label": "Generate Audio"}
    )

    negativePrompt: str | None = Field(
        None, alias="negative_prompt",
        json_schema_extra={
            "ui_label": "Negative Prompt",
            "ui_widget": "TEXT_AREA"
        }
    )

    personGeneration: str | None = Field( # default : allow_adult
        "allow_adult",
        alias="person_generation",
        examples=["allow_adult", "dont_allow", "allow_all"],
        json_schema_extra={"ui_label": "Person Generation",}
    )

    resizeMode: str | None = Field( # 이미지의 크기와 영상 사이즈의 설정 | Veo3 image-to-video 전용
        "pad",
        alias="resize_mode",
        examples=["pad", "crop"],
        json_schema_extra={"ui_label": "Resize Mode",}
    )

    resolution: str | None = Field( # 해상도 | Veo3 전용 | default : 720p
        "720p",
        alias= "resolution",
        examples=["720p", "1080p"],
        json_schema_extra={"ui_label": "Resolution"}
    )

    seed: int | None = Field(
        None,
        ge=0, le=4294967295,
        json_schema_extra={
            "ui_label": "Seed"
        }
    )