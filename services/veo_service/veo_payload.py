from services.veo_service.veo_builder import VeoInstanceBuilder, VeoPayloadBuilder

class VeoPayload:
    @staticmethod
    def from_text(prompt, parms):
        instance = VeoInstanceBuilder.text(prompt)
        return VeoPayloadBuilder.build(instance, parms)

    @staticmethod
    def from_image(prompt, image, parms):
        instance = VeoInstanceBuilder.image(prompt, image)
        return VeoPayloadBuilder.build(instance, parms)

    @staticmethod
    def from_first_last_frame(prompt, first, last, parms):
        instance = VeoInstanceBuilder.first_last_frame(prompt, first, last)
        return VeoPayloadBuilder.build(instance, parms)

    @staticmethod
    def from_reference_image(prompt, ref, parms):
        instance = VeoInstanceBuilder.reference_image(prompt, ref)
        return VeoPayloadBuilder.build(instance, parms)

    @staticmethod
    def from_insert_object(prompt, mask, video, parms):
        instance = VeoInstanceBuilder.insert_object(prompt, mask, video)
        return VeoPayloadBuilder.build(instance, parms)