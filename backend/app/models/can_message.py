from datetime import datetime


class CANMessage:

    def __init__(
        self,
        can_id: str,
        source: str,
        data: str
    ):
        self.timestamp = datetime.now()

        self.can_id = can_id

        self.source = source

        self.data = data