from core.schemas.video.veo_schema import VeoRequestParameters
from core.nodes.generate_inputs import generate_smart_inputs

veo2_overrides = {
    "duration": {
        "type": "SLIDER",
        "min": 5,
        "max": 8,
        "default": 8,
        "label": "Duration (5-8s)"
        }
    }

IMAGE_INPUT = {
    "name": "image_base64",
    "label": "Source Image",
    "type": "IMAGE_UPLOAD",
    "default": None
}

base_inputs_veo2 = generate_smart_inputs(VeoRequestParameters, overrides=veo2_overrides)

VEO2 = {
    "veo-2.0-generate-001": {
        "label": "Veo2",
        "inputs": base_inputs_veo2
    },
}

VEO2_EXPERIMENT = {
    "veo-2.0-generate-exp": {
        "label": "Veo2 Experiment",
        "inputs": base_inputs_veo2,
    }
}

VEO2_I2V = {
    "veo-2.0-generate-001": {
        "label": "Veo2 (Image to Video)",
        "inputs": [IMAGE_INPUT] + base_inputs_veo2
    },
}
