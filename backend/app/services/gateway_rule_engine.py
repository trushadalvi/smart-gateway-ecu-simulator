from app.services.ecu_manager import ecu_manager


def evaluate_rules():

    # =====================
    # Rule 1
    # Door Closed + Brake Pressed
    # -> Start Engine
    # =====================

    if (
        ecu_manager.door_state == "CLOSED"
        and ecu_manager.brake_state == "PRESSED"
    ):

        ecu_manager.engine_state = "RUNNING"

        if ecu_manager.prev_engine_state != "RUNNING":

            ecu_manager.add_can_message(
                "0x200",
                "Gateway ECU",
                "START_ENGINE"
            )

    else:

        ecu_manager.engine_state = "STOPPED"

    ecu_manager.prev_engine_state = ecu_manager.engine_state

    # =====================
    # Rule 2
    # Engine Running
    # -> Headlamp ON
    # =====================

    if ecu_manager.engine_state == "RUNNING":

        ecu_manager.headlamp_state = "ON"

        if ecu_manager.prev_headlamp_state != "ON":

            ecu_manager.add_can_message(
                "0x200",
                "Gateway ECU",
                "HEADLAMP_ON"
            )

    else:

        ecu_manager.headlamp_state = "OFF"

    ecu_manager.prev_headlamp_state = ecu_manager.headlamp_state

    # =====================
    # Rule 3
    # Engine Running + Battery Healthy
    # -> Telematics ACTIVE
    # =====================

    if (
        ecu_manager.engine_state == "RUNNING"
        and ecu_manager.battery_state == "HEALTHY"
    ):

        ecu_manager.telematics_state = "ACTIVE"

        if ecu_manager.prev_telematics_state != "ACTIVE":

            ecu_manager.add_can_message(
                "0x200",
                "Gateway ECU",
                "TELEMATICS_ON"
            )

    else:

        ecu_manager.telematics_state = "INACTIVE"

    ecu_manager.prev_telematics_state = ecu_manager.telematics_state

    # =====================
    # Rule 4
    # Speed > 0
    # -> Speed ECU Active
    # =====================

    if ecu_manager.speed > 0:

        ecu_manager.speed_ecu_active = True

    else:

        ecu_manager.speed_ecu_active = False

    # =====================
    # Rule 5
    # Vehicle Ready
    # =====================

    if (
        ecu_manager.engine_state == "RUNNING"
        and ecu_manager.speed_ecu_active
        and ecu_manager.battery_state == "HEALTHY"
    ):

        ecu_manager.system_ready = True

        if ecu_manager.prev_system_ready is False:

            ecu_manager.add_can_message(
                "0x300",
                "Gateway ECU",
                "SYSTEM_READY"
            )

    else:

        ecu_manager.system_ready = False

    ecu_manager.prev_system_ready = ecu_manager.system_ready