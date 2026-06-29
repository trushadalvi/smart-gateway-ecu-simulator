import asyncio
import websockets

async def test():
    url = "ws://127.0.0.1:8000/ecu/ws/multi-ecu"

    async with websockets.connect(url) as websocket:
        print("Connected to ECU stream 🚗⚡")

        while True:
            data = await websocket.recv()
            print(data)

asyncio.run(test())