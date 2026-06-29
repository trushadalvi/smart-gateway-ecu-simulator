from fastapi import APIRouter
from app.services.ecu_manager import ecu_manager
from app.services.gateway_rule_engine import evaluate_rules


router = APIRouter(
    prefix="/ecu",
    tags=["ECU"]
)

# =====================
# DOOR ECU
# =====================

@router.post("/door/open")
def open_door():

    ecu_manager.door_state = "OPEN"

    ecu_manager.add_can_message(
        "0x100",
        "Door ECU",
        "DOOR_OPEN"
    )

    evaluate_rules()

    return {
        "message": "Door Opened",
        "door_state": ecu_manager.door_state
    }


@router.post("/door/close")
def close_door():

    ecu_manager.door_state = "CLOSED"

    ecu_manager.add_can_message(
        "0x100",
        "Door ECU",
        "DOOR_CLOSED"
    )

    evaluate_rules()

    return {
        "message": "Door Closed",
        "door_state": ecu_manager.door_state
    }


@router.get("/door/status")
def door_status():

    return {
        "door_state": ecu_manager.door_state
    }


# =====================
# BRAKE ECU
# =====================

@router.post("/brake/press")
def press_brake():

    ecu_manager.brake_state = "PRESSED"
    evaluate_rules()
    
    ecu_manager.add_can_message(
    "0x101",
    "Brake ECU",
    "BRAKE_PRESSED"
)

    return {
        "message": "Brake Pressed",
        "brake_state": ecu_manager.brake_state
    }


@router.post("/brake/release")
def release_brake():

    ecu_manager.brake_state = "RELEASED"
    evaluate_rules()
    
    ecu_manager.add_can_message(
    "0x101",
    "Brake ECU",
    "BRAKE_RELEASED"
)

    return {
        "message": "Brake Released",
        "brake_state": ecu_manager.brake_state
    }


@router.get("/brake/status")
def brake_status():

    return {
        "brake_state": ecu_manager.brake_state
    }


# =====================
# ENGINE ECU
# =====================

@router.post("/engine/start")
def start_engine():

    ecu_manager.engine_state = "RUNNING"

    return {
        "message": "Engine Started",
        "engine_state": ecu_manager.engine_state
    }


@router.post("/engine/stop")
def stop_engine():

    ecu_manager.engine_state = "STOPPED"

    return {
        "message": "Engine Stopped",
        "engine_state": ecu_manager.engine_state
    }


@router.get("/engine/status")
def engine_status():

    return {
        "engine_state": ecu_manager.engine_state
    }


# =====================
# HEADLAMP ECU
# =====================

@router.post("/headlamp/on")
def headlamp_on():

    ecu_manager.headlamp_state = "ON"

    return {
        "headlamp_state": ecu_manager.headlamp_state
    }


@router.post("/headlamp/off")
def headlamp_off():

    ecu_manager.headlamp_state = "OFF"

    return {
        "headlamp_state": ecu_manager.headlamp_state
    }


@router.get("/headlamp/status")
def headlamp_status():

    return {
        "headlamp_state": ecu_manager.headlamp_state
    }


# =====================
# SPEED ECU
# =====================

@router.post("/speed/{value}")
def set_speed(value: int):

    ecu_manager.speed = value
    
    ecu_manager.add_can_message(
    "0x104",
    "Speed ECU",
    f"SPEED_{value}"
)

    evaluate_rules()

    return {
        "speed": ecu_manager.speed
    }


@router.get("/speed/status")
def speed_status():

    return {
        "speed": ecu_manager.speed
    }


# =====================
# BATTERY ECU
# =====================

@router.post("/battery/healthy")
def battery_healthy():

    ecu_manager.battery_state = "HEALTHY"
    
    ecu_manager.add_can_message(
    "0x105",
    "Battery ECU",
    "BATTERY_HEALTHY"
)

    evaluate_rules()

    return {
        "battery_state": ecu_manager.battery_state
    }


@router.post("/battery/fault")
def battery_fault():

    ecu_manager.battery_state = "FAULT"
    
    ecu_manager.add_can_message(
    "0x105",
    "Battery ECU",
    "BATTERY_FAULT"
)

    evaluate_rules()

    return {
        "battery_state": ecu_manager.battery_state
    }


@router.get("/battery/status")
def battery_status():

    return {
        "battery_state": ecu_manager.battery_state
    }


# =====================
# TELEMATICS ECU
# =====================

@router.get("/telematics/status")
def telematics_status():

    return {
        "telematics_state": ecu_manager.telematics_state
    }


# =====================
# COMPLETE VEHICLE STATUS
# =====================

@router.get("/all-status")
def all_status():

    return {
        "door_state": ecu_manager.door_state,
        "brake_state": ecu_manager.brake_state,
        "engine_state": ecu_manager.engine_state,
        "headlamp_state": ecu_manager.headlamp_state,
        "speed": ecu_manager.speed,
        "battery_state": ecu_manager.battery_state,
        "telematics_state": ecu_manager.telematics_state,
        "speed_ecu_active": ecu_manager.speed_ecu_active,
        "system_ready": ecu_manager.system_ready
    }
    
@router.get("/can-messages")
def get_can_messages():

    return [
        {
            "timestamp": str(msg.timestamp),
            "can_id": msg.can_id,
            "source": msg.source,
            "data": msg.data
        }
        for msg in ecu_manager.can_messages
    ]