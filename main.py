import asyncio
from services.veo_service.veo_service import VeoService


async def main():
    generator = VeoService()
    operation = await generator.text_to_video()
    print(operation)


if __name__ == "__main__":
    asyncio.run(main())