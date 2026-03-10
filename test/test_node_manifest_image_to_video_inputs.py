from core.nodes.all_nodes import NODE_MANIFEST


def test_image_to_video_models_require_image_base64_input() -> None:
    models = NODE_MANIFEST["image_to_video"]["models"]
    expected_models = {
        "veo-2.0-generate-001",
        "veo-3.0-generate-001",
        "veo-3.1-generate-001",
        "veo-3.1-fast-generate-001",
    }

    assert expected_models.issubset(set(models.keys()))

    for model_id in expected_models:
        inputs = models[model_id]["inputs"]
        assert any(i.get("name") == "image_base64" for i in inputs), model_id
