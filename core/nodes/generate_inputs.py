# overrides: 특정 필드의 설정을 강제로 바꾸고 싶을 때 사용하는 딕셔너리
def generate_smart_inputs(pydantic_model, overrides=None):
    if overrides is None:
        overrides = {}

    inputs = []

    for field_name, field_info in pydantic_model.model_fields.items():
        name = field_info.alias or field_name

        ui_meta = field_info.json_schema_extra or {}
        input_def = {
            "name": name,
            "label": ui_meta.get("ui_label", name.replace("_", " ").title()),
            "type": "STRING",  # 임시
            "default": field_info.default,
            "options": field_info.examples
        }

        if "ui_widget" in ui_meta:
            input_def["type"] = ui_meta["ui_widget"]
            input_def["min"] = ui_meta.get("min")
            input_def["max"] = ui_meta.get("max")
        elif field_info.examples:
            input_def["type"] = "COMBO"
            # bool 또는 bool | None 둘 다 체크해야 함
        elif field_info.annotation == bool or field_info.annotation == (bool | None):
            input_def["type"] = "BOOLEAN"
        elif field_info.annotation == int:
            input_def["type"] = "INT"

        if name in overrides:
            input_def.update(overrides[name])

        inputs.append(input_def)

    return inputs