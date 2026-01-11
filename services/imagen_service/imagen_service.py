from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

output_file = "output-image.png"

image = client.models.generate_images(
    model="imagen-4.0-generate-001",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        add_watermark = "",
        aspect_ratio = "",
        enhance_prompt = "",
        guidance_scale = "",
        image_size = "",
        include_rai_reason = "",
        include_safety_attributes = "",
        labels = "",
        language = "",
        negative_prompt = "",
        number_of_images = "",
        output_compression_quality = "",
        output_gcs_uri = "",
        output_mime_type = "",
        person_generation = "",
        safety_filter_level = "",
        seed = ""
    )
)

image.generated_images[0].image.save(output_file)

print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
# Example response = "
# Created output image using 1234567 bytes