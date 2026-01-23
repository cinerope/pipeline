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
                add_watermark = parms.add_watermark,
                aspect_ratio = parms.aspect_ratio,
                enhance_prompt = parms.enhance_prompt,
                guidance_scale = parms.guidance_scale,
                image_size = parms.image_size,
                include_rai_reason = parms.include_rai_reason,
                include_safety_attributes = parms.include_safety_attributes,
                labels = parms.labels,
                language = parms.language,
                negative_prompt = parms.negative_prompt,
                number_of_images = parms.number_of_images,
                output_compression_quality = parms.output_compression_quality,
                output_gcs_uri = parms.output_gcs_uri,
                output_mime_type = parms.output_mime_type,
                person_generation = parms.person_generation,
                safety_filter_level = parms.safety_filter_level,
                seed = parms.seed
            )
        )
        return operation