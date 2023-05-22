import asyncio
import logging
import websockets
import websocket
from nostr_node import Client
logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger("PRODUCER CLIENT")


HOST = "ws://localhost:8080"
PRIVATE_KEY = "f89711963b361cf24e798fb527d78ef703613bd33815bb691f705ca4f4c92102"
PUBLIC_KEY = "1f5733a0b9b844a2d66c4a855c689459d3dcb759895fd7087b5542fde306bb30"

async def demo() -> None:
    async with websockets.connect(HOST) as websocket:
        client = Client(websocket, private_key=PRIVATE_KEY, public_key=PUBLIC_KEY)
        message = await client.publish_event(content="hello")
        logger.info(f"Message sent | event: {message}")
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(demo())