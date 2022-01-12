from typing import Optional


class PaymentMethod:
    def __init__(self, name, enabled, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.enabled = enabled