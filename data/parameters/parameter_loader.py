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