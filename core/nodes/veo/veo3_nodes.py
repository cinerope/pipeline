from core.schemas.video.veo_schema import VeoRequestParameters
from core.nodes.generate_inputs import generate_smart_inputs

veo3_overrides = {
    "duration": {
        "type": "COMBO",
        "options": [4, 6, 8], # 슬라이더는 5, 7을 선택할 위험이 있으니 콤보로 변경
        "default": 8,
        "label": "Duration (4, 6, 8s)"
    }
}

IMAGE_INPUT = {
    "name": "image_base64",
    "label": "Source Image",
    "type": "IMAGE_UPLOAD",
    "default": None
}

base_inputs_veo3 = generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)

VEO3 = {
    "veo-3.0-generate-001": {
        "label": "Veo3",
        "inputs": base_inputs_veo3
    }
}

VEO3_FAST = {
    "veo-3.0-fast-generate-001": {
        "label": "Veo3 Fast",
        "inputs": base_inputs_veo3
        }
}

VEO3_PREVIEW = {
    "veo-3.0-generate-preview": {
        "label": "Veo3 Preview",
        "inputs": base_inputs_veo3
    }
}

VEO3_PREVIEW_FAST = {
    "veo-3.0-fast-generate-preview": {
        "label": "Veo3 Preview Fast",
        "inputs": base_inputs_veo3
    }
}

VEO3_1 = {
    "veo-3.1-generate-001": {
        "label": "Veo3.1",
        "inputs": base_inputs_veo3
    }
}

VEO3_1_FAST = {
    "veo-3.1-fast-generate-001": {
        "label": "Veo3.1 Fast",
        "inputs": base_inputs_veo3
    }
}

VEO3_I2V = {
    "veo-3.0-generate-001": {
        "label": "Veo3 (Image to Video)",
        "inputs": [IMAGE_INPUT] + base_inputs_veo3
    }
}

VEO3_1_I2V = {
    "veo-3.1-generate-001": {
        "label": "Veo3.1 (Image to Video)",
        "inputs": [IMAGE_INPUT] + base_inputs_veo3
    }
}

VEO3_1_FAST_I2V = {
    "veo-3.1-fast-generate-001": {
        "label": "Veo3.1 (Image to Video)",
        "inputs": [IMAGE_INPUT] + base_inputs_veo3
    }
}