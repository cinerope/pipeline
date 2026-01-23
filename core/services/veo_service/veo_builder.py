from typing import Dict, Any

from core.schemas.video.veo_schema import (
    VeoRequestParameters,
    VeoImageInstance,
    VeoFirstLastFrameImageInstance,
    VeoReferenceImageInstance,
    VeoVideoInsertObjectInstance
)

class VeoInstanceBuilder:
    @staticmethod
    def text(prompt) -> Dict[str, Any]:
        return {"prompt": prompt}

    @staticmethod
    def image(prompt, image: VeoImageInstance) -> Dict[str, Any]:
        """
        veo-2.0-generate-001
        veo-3.0-generate-001
        veo-3.1-generate-001
        veo-3.1-fast-generate-001
        상기 모델만 사용 가능
        """
        return {
            "prompt": prompt,
            "image": image.model_dump(exclude_none=True),
        }

    @staticmethod
    def first_last_frame(
            prompt,
            first : VeoFirstLastFrameImageInstance,
            last : VeoFirstLastFrameImageInstance
    ) -> Dict[str, Any]:
        """
        veo-2.0-generate-001
        veo-3.1-generate-001
        veo-3.1-fast-generate-001
        상기 모델만 사용 가능
        """
        return {
            "prompt": prompt,
            "first": first.image.model_dump(exclude_none=True),
            "last": last.lastFrame.model_dump(exclude_none=True)
        }

    @staticmethod
    def reference_image(
            prompt,
            ref: VeoReferenceImageInstance
    ) -> Dict[str, Any]:
        """
        veo-2.0-generate-exp
        veo-3.1-generate-preview
        상기 모델만 사용 가능
        """
        return {
            "prompt": prompt,
            "referenceImage" : [
                {
                "image": ref.image.model_dump(exclude_none=True),
                "referenceType": ref.referenceType
                }
            ]
        }

    @staticmethod
    def insert_object(
            prompt,
            mask: VeoVideoInsertObjectInstance,
            video: VeoVideoInsertObjectInstance
    ) -> Dict[str, Any]:
        """
        아직 사용 불가
        사유 : veo 내부 테스트중
        """
        return {
            "prompt": prompt,
            "mask": mask.mask.model_dump(exclude_none=True),
            "maskMode": mask.maskMode,
            "video": video.video.model_dump(exclude_none=True),
        }

class VeoPayloadBuilder:
    @staticmethod
    def build(
            instance,
            params: VeoRequestParameters
    ) -> Dict[str, Any]:
        return {
            "instances": [instance],
            "parameters": params.model_dump(exclude_none=True),
        }