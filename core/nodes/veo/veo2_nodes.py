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

VEO2_NODES = {
    "veo-2.0-generate-001": {
        "label": "Veo2",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo2_overrides)
    },
    "veo-2.0-generate-exp": {
        "label": "Veo2 Experiment",
        "inputs": generate_smart_inputs(VeoRequestParameters, overrides=veo2_overrides),
    }
}