import asyncio
import json

from core.api.generation_api import generate_from_api_request
from core.nodes.all_nodes import NODE_MANIFEST


async def main() -> None:
    with open("data/veo_request_mock.json", "r", encoding="utf-8") as fh:
        payload = json.load(fh)

    result = await generate_from_api_request(payload)
    print(result)
    print("available_tasks:", list(NODE_MANIFEST.keys()))


if __name__ == "__main__":
    asyncio.run(main())
