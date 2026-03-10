# Google Veo
from core.nodes.veo.veo2_nodes import (
    VEO2,
    VEO2_EXPERIMENT,
    VEO2_I2V,
)
from core.nodes.veo.veo3_nodes import (
    VEO3,
    VEO3_FAST,
    VEO3_PREVIEW,
    VEO3_PREVIEW_FAST,
    VEO3_1,
    VEO3_1_FAST,
    VEO3_I2V,
    VEO3_1_I2V,
    VEO3_1_FAST_I2V,
)

TEXT_TO_VIDEO_NODES = (
        VEO2 |
        VEO2_EXPERIMENT |
        VEO3 |
        VEO3_FAST |
        VEO3_PREVIEW |
        VEO3_PREVIEW_FAST |
        VEO3_1 |
        VEO3_1_FAST
)

IMAGE_TO_VIDEO_NODES = (
        VEO2_I2V |
        VEO3_I2V |
        VEO3_1_I2V |
        VEO3_1_FAST_I2V
)

NODE_MANIFEST = {
    "text_to_video": {
        "label": "Text to Video",
        "models": TEXT_TO_VIDEO_NODES
    },

    "image_to_video": {
        "label": "Image to Video",
        "models": IMAGE_TO_VIDEO_NODES
    }
}
