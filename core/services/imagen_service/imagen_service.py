import os

from data.parameters.parameter_loader import UserParameterAccessor, Model
from core.schemas.Image.imagen_schema import ImagenRequestParameters

from google import genai
from google.genai.types import GenerateImagesConfig


class ImagenService:
    def __init__(self):
        accessor = UserParameterAccessor()

        self.model_parameters = accessor.model_parameters
        self.model_id = Model(self.model_parameters).id

    def _merge_parameters(self, user_params: ImagenRequestParameters | None):
        base = self.model_parameters.copy()
        if user_params:
            base.update(user_params.model_dump(exclude_unset=True))

        base["storageUri"] = os.getenv("GCS_OUTPUT_URI")
        return ImagenRequestParameters(**base)

    async def create_imagen(self, user_parms:ImagenRequestParameters):
        client = genai.Client()
        output_file = "output-image.png"
        parms = self._merge_parameters(user_parms)

        operation = await client.models.generate_images(
            model=self.model_id,
            prompt="A dog reading a newspaper",
            config=GenerateImagesConfig(
                add_watermark = parms.addWatermark,
                aspect_ratio = parms.aspectRatio,
                enhance_prompt = parms.enhancePrompt,
                guidance_scale = parms.guidanceScale,
                image_size = parms.imageSize,
                include_rai_reason = parms.includeRaiReason,
                include_safety_attributes = parms.includeSafetyAttributes,
                labels = parms.labels,
                language = parms.language,
                negative_prompt = parms.negativePrompt,
                number_of_images = parms.numberOfImages,
                output_compression_quality = parms.outputCompressionQuality,
                output_gcs_uri = parms.outputGcsUri,
                output_mime_type = parms.outputMimeType,
                person_generation = parms.personGeneration,
                safety_filter_level = parms.safetyFilterLevel,
                seed = parms.seed
            )
        )
        return operation
