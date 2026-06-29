from fastapi import APIRouter, WebSocket
import asyncio
from app.services.ecu_manager import ECUManager

router = APIRouter()
ecu = ECUManager()

@router.websocket("/ws/multi-ecu")
async def multi_ecu_stream(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = {
            "engine": ecu.get_engine_data(),
            "brake": ecu.get_brake_data(),
            "battery": ecu.get_battery_data(),
            "transmission": ecu.get_transmission_data()
        }

        await websocket.send_json(data)
        await asyncio.sleep(1)