from core.nodes.veo.veo2_nodes import VEO2_NODES
from core.nodes.veo.veo3_nodes import VEO3_NODES

TEXT_TO_VIDEO_NODES = VEO2_NODES | VEO3_NODES
IMAGE_TO_VIDEO_NODES = VEO2_NODES | VEO3_NODES

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