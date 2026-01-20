import os

from core.prompt.video_prompt_builder import Prompt
from data.parameters.parameter_loader import Model, User, UserParameterAccessor
from services.get_headers import get_headers_from_key
from services.veo_service.veo_rest import VeoRequestService
from services.veo_service.veo_builder import VeoInstanceBuilder
from services.veo_service.veo_payload import VeoPayload

class Veo2:
    def __init__(self):
        key_file = "veo-auth-key.json"
        headers = get_headers_from_key(key_file)
        VeoRequestService("veo-3.1-fast-generate-001", headers)

    @staticmethod
    def text():
        assembly_prompt = Prompt()
        parameters = UserParameterAccessor().model_parameters
        veo_payload = VeoPayload.from_text(assembly_prompt, parameters)
        VeoRequestService.submit(veo_payload)


    @staticmethod
    def image():


class Veo3:
    key_file = "veo-auth-key.json"
    headers = get_headers_from_key(key_file)
    veo_service = VeoRequestService("veo-3.1-fast-generate-001", headers)