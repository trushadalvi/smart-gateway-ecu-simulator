
from fastapi import APIRouter, WebSocket
from app.services.ecu_manager import ecu_manager
import asyncio

router = APIRouter()


@router.get("/ws-test")
def ws_test():
    return {"message": "WebSocket Router Loaded"}


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    print("CLIENT CONNECTED")

    while True:

        messages = []

        for msg in ecu_manager.can_messages:

            messages.append({
                "timestamp": str(msg.timestamp),
                "can_id": msg.can_id,
                "source": msg.source,
                "data": msg.data
            })

        await websocket.send_json(messages)

        await asyncio.sleep(1)