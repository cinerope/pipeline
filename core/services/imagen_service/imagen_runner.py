import asyncio

class ImagenRunner:
    def __init__(self, client):
        self.client = client

    async def wait(self, operation, interval=10):
        while not operation.done:
            print("Generating video ...")
            await asyncio.sleep(interval)
            operation = self.client.get_operation(operation)

        if not operation.response:
            raise RuntimeError("Veo generation failed")

        return operation.response.generated_videos[0].video.uri

    image.generated_images[0].image.save(output_file)

    print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
    # Example response = "
    # Created output image using 1234567 bytes