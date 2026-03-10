from pydantic import BaseModel, Field, ConfigDict

class ImagenRequestParameters(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    addWatermark: bool | None = Field(
        False, alias="add_watermark",
        json_schema_extra={"ui_label": "Add Watermark"}
    )

    aspectRatio: str | None = Field(
        "16:9",
        alias="aspect_ratio", examples=["16:9", "9:16", "4:3", "3:4", "1:1"],
        json_schema_extra={"ui_label": "Aspect Ratio"}

    )

    enhancePrompt: bool | None = Field(
        False, alias="enhance_prompt",
        json_schema_extra={"ui_label": "Enhance Prompt"}
    )


    guidanceScale: float | None = Field(None, alias="guidance_scale")
    imageSize: str | None = Field(None, alias="image_size")
    includeRaiReason: bool | None = Field(None, alias="include_rai_reason")
    includeSafetyAttributes: bool | None = Field(None, alias="include_safety_attributes")
    labels: dict[str, str] | None = Field(None)
    language: str | None = Field(None)
    negativePrompt: str | None = Field(None, alias="negative_prompt")
    numberOfImages: int | None = Field(None, alias="number_of_images")
    outputCompressionQuality: int | None = Field(None, alias="output_compression_quality")
    outputGcsUri: str | None = Field(None, alias="output_gcs_uri")
    outputMimeType: str | None = Field(None, alias="output_mime_type")
    personGeneration: str | None = Field(None, alias="person_generation")
    safetyFilterLevel: str | None = Field(None, alias="safety_filter_level")
    seed: int | None = Field(None)
