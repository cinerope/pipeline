import os

from google.genai.types import GenerateVideosConfig, Image

from test.python_sdk.apis.veo_api import VeoApi
from data.parameters.parameter_loader import UserParameterAccessor, Model
from schemas.video.veo_schema import *
from test.python_sdk.veo_service.veo_prompt import VeoPromptService
from test.python_sdk.veo_service.veo_runner import VeoRunner

class VeoService:
    def __init__(self):
        accessor = UserParameterAccessor()

        self.model_parameters = accessor.model_parameters
        self.model_id = Model(self.model_parameters).id


        self.prompt = VeoPromptService()
        self.client = VeoApi()
        self.runner = VeoRunner(self.client)

    def _merge_parameters(self, user_params: VeoRequestParameters | None):
        base = self.model_parameters.copy()
        if user_params:
            base.update(user_params.model_dump(exclude_unset=True))

        base["storageUri"] = os.getenv("GCS_OUTPUT_URI")
        return VeoRequestParameters(**base)

    async def text_to_video(self, user_params: VeoRequestParameters = None):
        params = self._merge_parameters(user_params)

        operation = await self.client.generate(
            model = self.model_id,
            prompt = self.prompt.build(),
            config = GenerateVideosConfig(
                aspect_ratio = params.aspectRatio,
                compression_quality = params.compressionQuality,
                duration_seconds = params.durationSeconds,
                enhance_prompt = params.enhancePrompt,
                generate_audio = params.generateAudio,
                negative_prompt = params.negativePrompt,
                person_generation = params.personGeneration,
                resolution = params.resolution,
                number_of_videos = params.sampleCount,
                seed = params.seed,
                output_gcs_uri = params.storageUri
            )
        )
        return await self.runner.wait(operation)

    async def image_to_video(
            self,
            image_parms: VeoImageInstance,
            user_params: VeoRequestParameters
    ):
        params = self._merge_parameters(user_params)

        operation = await self.client.generate(
            model = self.model_id,
            prompt = self.prompt.build(),
            image = Image(
            gcs_uri = image_parms.gcsUri,
            mime_type = image_parms.mimeType,
             ),
            config = GenerateVideosConfig(
                aspect_ratio = params.aspectRatio,
                compression_quality = params.compressionQuality,
                duration_seconds = params.durationSeconds,
                enhance_prompt = params.enhancePrompt,
                generate_audio = params.generateAudio,
                negative_prompt = params.negativePrompt,
                person_generation = params.personGeneration,
                resolution = params.resolution,
                number_of_videos = params.sampleCount,
                seed = params.seed,
                output_gcs_uri = params.storageUri
            )
        )
        return await self.runner.wait(operation)

    async def first_last_frame_video(
            self,
            image_parms: VeoImageInstance,
            last_frame: VeoFirstLastFrameImageInstance,
            user_params: VeoRequestParameters
    ):
        params = self._merge_parameters(user_params)

        operation =  self.client.generate(
            model = self.model_id,
            prompt = self.prompt.build(),
            image = Image(
                gcs_uri = image_parms.gcsUri,
                mime_type = image_parms.mimeType,
            ),
            config = GenerateVideosConfig(
                aspect_ratio = params.aspectRatio,
                last_frame = Image(
                gcs_uri = last_frame.gcsUri,
                mime_type = last_frame.mimeType,
                ),
                compression_quality = params.compressionQuality,
                duration_seconds = params.durationSeconds,
                enhance_prompt = params.enhancePrompt,
                generate_audio = params.generateAudio,
                negative_prompt = params.negativePrompt,
                person_generation = params.personGeneration,
                resolution = params.resolution,
                number_of_videos = params.sampleCount,
                seed = params.seed,
                output_gcs_uri = params.storageUri
            )
        )
        return await self.runner.wait(operation)