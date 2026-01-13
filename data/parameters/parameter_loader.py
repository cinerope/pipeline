from data.parameters.load_user_parameter import UserParameter

class UserParameterAccessor:
    def __init__(self):
        self.user_parameter = UserParameter().get_user_parameter

    @property
    def cinerope_parameters(self):
        return self.user_parameter.get("cinerope_parameters", {})

    @property
    def model_parameters(self):
        return self.user_parameter.get("model_parameters", {})

class Model:
    def __init__(self, parameters: dict):
        self._parameters = parameters

    @property
    def id(self):
        return self._parameters.get("model_id")

    # veo model
    # veo-2.0-generate-001
    # veo-3.0-generate-001
    # veo-3.0-fast-generate-001
    # veo-3.0-generate-preview(프리뷰)
    # veo-3.0-fast-generate-preview(프리뷰)
    # veo-3.1-generate-001
    # veo-3.1-fast-generate-001

    # imagen model
    # imagen-4.0-generate-001
    # imagen-4.0-fast-generate-001
    # imagen-4.0-ultra-generate-001
    # imagen-3.0-generate-002