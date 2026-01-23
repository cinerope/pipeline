# services/payloads.py
from core.schemas.video.veo_schema import (
    VeoRequestParameters,
    VeoImageInstance,
    VeoFirstLastFrameImageInstance,
    VeoReferenceImageInstance
)


def build_pydantic_payload(task_type, ui_params):
    """
    ui_params: {"aspect_ratio": "16:9", "seed": 123, "image_base64": "..."}
    """

    # 1. Parameters 처리 (Alias 덕분에 자동 매핑!)
    # UI에서 받은 dict를 그대로 unpack(**) 해서 넣습니다.
    # Pydantic이 알아서 alias("aspect_ratio")를 찾아 "aspectRatio" 필드에 넣습니다.
    param_model = VeoRequestParameters(**ui_params)

    # 2. Instance 처리
    instance_model = None

    if task_type == "text_to_video":
        instance_model = {"prompt": ui_params.get("prompt")}

    elif task_type == "image_to_video":
        # 이미지 객체 생성 (alias="image_base64" 덕분에 자동 매핑)
        img_obj = VeoImageInstance(**ui_params)
        instance_model = {
            "prompt": ui_params.get("prompt"),
            "image": img_obj.model_dump(exclude_none=True, by_alias=False)
        }

    elif task_type == "frame_interpolation":
        # first_frame, last_frame 키가 들어오면 알아서 내부 필드로 매핑됨
        fl_instance = VeoFirstLastFrameImageInstance(**ui_params)

        instance_dict = fl_instance.model_dump(exclude_none=True, by_alias=False)
        instance_dict["prompt"] = ui_params.get("prompt")
        instance_model = instance_dict

    elif task_type == "reference_image":
        reference_instance = VeoReferenceImageInstance(**ui_params)

        instance_dict = reference_instance.model_dump(exclude_none=True, by_alias=False)
        instance_dict["prompt"] = ui_params.get("prompt")
        instance_model = instance_dict

    # 3. 최종 결과 반환
    return {
        "instances": [instance_model],
        # by_alias=False: 나갈 때는 alias(snake_case)가 아니라 원래 이름(camelCase)으로 나감!
        "parameters": param_model.model_dump(exclude_none=True, by_alias=False)
    }