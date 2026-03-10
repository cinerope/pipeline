import os

from dotenv import load_dotenv
from core.services.contracts import GenerationRequest, TaskType
from core.schemas.video.veo_schema import (
    VeoRequestParameters,
    VeoImageInstance,
)

load_dotenv()


TEXT_TO_VIDEO_MODELS = {
    "veo-2.0-generate-001",
    "veo-2.0-generate-exp",
    "veo-3.0-generate-001",
    "veo-3.0-fast-generate-001",
    "veo-3.0-generate-preview",
    "veo-3.0-fast-generate-preview",
    "veo-3.1-generate-001",
    "veo-3.1-fast-generate-001",
}

IMAGE_TO_VIDEO_MODELS = {
    "veo-2.0-generate-001",
    "veo-3.0-generate-001",
    "veo-3.1-generate-001",
    "veo-3.1-fast-generate-001",
}


def _resolve_image_gcs_uri(request: GenerationRequest, ui_params: dict) -> str | None:
    if request.image_uri:
        return request.image_uri

    if request.image_id:
        mapping = ui_params.get("image_id_to_uri")
        if isinstance(mapping, dict):
            resolved = mapping.get(request.image_id)
            if isinstance(resolved, str) and resolved:
                return resolved

    raw_uri = ui_params.get("image_uri")
    if isinstance(raw_uri, str) and raw_uri:
        return raw_uri

    raw_id = ui_params.get("image_id")
    mapping = ui_params.get("image_id_to_uri")
    if isinstance(raw_id, str) and isinstance(mapping, dict):
        resolved = mapping.get(raw_id)
        if isinstance(resolved, str) and resolved:
            return resolved

    return None


def _validate_model_task_support(model_id: str, task_type: TaskType) -> None:
    if task_type == TaskType.TEXT_TO_VIDEO:
        if model_id not in TEXT_TO_VIDEO_MODELS:
            raise ValueError(
                f"Model '{model_id}' does not support task_type '{task_type.value}'"
            )
        return

    if task_type == TaskType.IMAGE_TO_VIDEO:
        if model_id not in IMAGE_TO_VIDEO_MODELS:
            raise ValueError(
                f"Model '{model_id}' does not support task_type '{task_type.value}'"
            )
        return

    raise ValueError(f"Unsupported task_type: {task_type.value}")


def build_veo_payload(request: GenerationRequest) -> dict:
    _validate_model_task_support(request.model_id, request.task_type)
    ui_params = request.options.copy()
    if "storage_uri" not in ui_params and "storageUri" not in ui_params:
        env_storage_uri = os.getenv("GCS_OUTPUT_URI")
        if env_storage_uri:
            ui_params["storage_uri"] = env_storage_uri

    param_model = VeoRequestParameters(**ui_params)
    instance_model = {"prompt": request.prompt}

    if request.task_type == TaskType.IMAGE_TO_VIDEO:
        image_uri = _resolve_image_gcs_uri(request, ui_params)
        if not request.image_base64 and not image_uri:
            raise ValueError(
                "image_to_video requires one of image_base64, image_uri, or image_id"
            )
        img_obj = VeoImageInstance(
            bytesBase64Encoded=request.image_base64,
            gcsUri=image_uri or ui_params.get("gcsUri"),
            mimeType=ui_params.get("mimeType"),
        )
        instance_model["image"] = img_obj.model_dump(exclude_none=True, by_alias=False)

    parameters = param_model.model_dump(exclude_none=True, by_alias=False)
    if not parameters.get("storageUri"):
        raise ValueError("storageUri is required for Veo output delivery")

    if request.model_id.startswith("veo-3."):
        # Veo 3 rejects explicit enhancePrompt=false.
        parameters.pop("enhancePrompt", None)

    return {
        "instances": [instance_model],
        "parameters": parameters,
    }


def build_pydantic_payload(task_type, ui_params):
    # Backward compatibility wrapper for existing callers.
    request = GenerationRequest(
        provider="veo",
        model_id=ui_params.get("model_id", ""),
        task_type=TaskType(task_type),
        prompt=ui_params.get("prompt"),
        image_base64=ui_params.get("image_base64"),
        options=ui_params,
    )
    return build_veo_payload(request)
