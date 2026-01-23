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

VEO3_NODES = {
    "veo-3.0-generate-001": {
        "label": "Veo3",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)
    },
    "veo-3.0-fast-generate-001": {
        "label": "Veo3 Fast",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)
    },
    "veo-3.0-generate-preview": {
        "label": "Veo3 Preview",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)
    },
    "veo-3.0-fast-generate-preview": {
        "label": "Veo3 Preview Fast",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)
    },
    "veo-3.1-generate-001": {
        "label": "Veo3.1",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)
    },
    "veo-3.1-fast-generate-001": {
        "label": "Veo3.1 Fast",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo3_overrides)
    }
}