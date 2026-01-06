import time, os
from dotenv import load_dotenv

from core.parameters.parameter_loader import *
from core.prompt.prompt_builder import Prompt
from core.models_video.types.veo_types import *

from google import genai
from google.genai.types import HttpOptions, GenerateVideosConfig, Image

class GenaiVideoGenerator:
    def __init__(self):
        load_dotenv()

        accessor = UserParameterAccessor()

        self.prompt = Prompt()
        self.model_parameters = accessor.model_parameters
        self.veo_params = VeoRequestParameters(
            **self.model_parameters,
            storageUri=os.getenv("GCS_OUTPUT_URI")
        )

        self.model_id = Model(self.model_parameters).id

        self.client = genai.Client(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location=os.getenv("GOOGLE_LOCATION"),
            http_options=HttpOptions(api_version="v1")
        )

        self.system_prompt = f"""
            You are a cinematic video generation model.

            Strictly follow the cinematic instructions below as the highest priority.

            Do not add, remove, or modify any camera angles, shot sizes, lens types,
            camera movements, framing, or focus behavior beyond what is explicitly specified.

            Do not apply any film-style overlays or analog effects.
            Do not add Vignetting, film grain, film borders, vignetting, letterboxing,
            dust, scratches, retro textures, or stylized frames.

            The final result must appear clean, modern, and digital,
            with no artificial framing or film emulation.
            """

    def text_to_video(self):
        return self.client.models.generate_videos(
            model= self.model_id,
            prompt= f"{self.system_prompt} \n#{self.prompt.text_to_video()}",
            config= GenerateVideosConfig(
                aspect_ratio=self.veo_params.aspectRatio,
                compression_quality=self.veo_params.compressionQuality,
                duration_seconds=self.veo_params.durationSeconds,
                enhance_prompt=self.veo_params.enhancePrompt,
                generate_audio=self.veo_params.generateAudio,
                negative_prompt=self.veo_params.negativePrompt,
                person_generation=self.veo_params.personGeneration,
                resolution=self.veo_params.resolution,
                number_of_videos=self.veo_params.sampleCount,
                seed=self.veo_params.seed,
                output_gcs_uri=self.veo_params.storageUri
            )
        )

    def image_to_video(self, image_parms:VeoImageInstance):
        return self.client.models.generate_videos(
            model= self.model_id,
            prompt= f"{self.system_prompt} \n#{self.prompt.text_to_video()}",
            image= Image(
            gcs_uri= image_parms.gcsUri,
            mime_type= image_parms.mimeType,
             ),
            config= GenerateVideosConfig(
                aspect_ratio=self.veo_params.aspectRatio,
                compression_quality=self.veo_params.compressionQuality,
                duration_seconds=self.veo_params.durationSeconds,
                enhance_prompt=self.veo_params.enhancePrompt,
                generate_audio=self.veo_params.generateAudio,
                negative_prompt=self.veo_params.negativePrompt,
                person_generation=self.veo_params.personGeneration,
                resolution=self.veo_params.resolution,
                number_of_videos=self.veo_params.sampleCount,
                seed=self.veo_params.seed,
                output_gcs_uri=self.veo_params.storageUri
            )
        )

    def first_last_frame_video(self, image_parms:VeoImageInstance, last_frame:VeoFristLastFrameImageInstance):
        return self.client.models.generate_videos(
            model=self.model_id,
            prompt=f"{self.system_prompt} \n#{self.prompt.text_to_video()}",
            image= Image(
                gcs_uri= image_parms.gcsUri,
                mime_type= image_parms.mimeType,
            ),
            config=GenerateVideosConfig(
                aspect_ratio=self.veo_params.aspectRatio,
                last_frame=Image(
                gcs_uri= last_frame.gcs_uri,
                mime_type= last_frame.mimeType,
                ),
                compression_quality=self.veo_params.compressionQuality,
                duration_seconds=self.veo_params.durationSeconds,
                enhance_prompt=self.veo_params.enhancePrompt,
                generate_audio=self.veo_params.generateAudio,
                negative_prompt=self.veo_params.negativePrompt,
                person_generation=self.veo_params.personGeneration,
                resolution=self.veo_params.resolution,
                number_of_videos=self.veo_params.sampleCount,
                seed=self.veo_params.seed,
                output_gcs_uri=self.veo_params.storageUri
            )
        )

    def create_video(self, operation):
        while not operation.done:
            print("Waiting for models_video generation to complete...")
            time.sleep(10)
            operation = self.client.operations.get(operation)

        if operation.response:
            return operation.result.generated_videos[0].video.uri