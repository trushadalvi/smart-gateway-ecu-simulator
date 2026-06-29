from app.models.can_message import CANMessage


class ECUManager:

    def __init__(self):

        self.door_state = "CLOSED"
        self.brake_state = "RELEASED"
        self.engine_state = "STOPPED"

        self.headlamp_state = "OFF"
        self.speed = 0

        self.battery_state = "HEALTHY"

        self.telematics_state = "INACTIVE"

        self.speed_ecu_active = False
        self.system_ready = False
        
        self.prev_engine_state = "STOPPED"
        self.prev_headlamp_state = "OFF"
        self.prev_telematics_state = "INACTIVE"
        self.prev_system_ready = False

        self.can_messages = []

    def add_can_message(
        self,
        can_id,
        source,
        data
    ):
        message = CANMessage(
            can_id=can_id,
            source=source,
            data=data
        )

        self.can_messages.append(message)


ecu_manager = ECUManager()