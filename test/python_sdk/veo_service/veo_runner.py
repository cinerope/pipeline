import asyncio

class VeoRunner:
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