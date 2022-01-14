from dataclasses import dataclass


@dataclass
class PaymentMethodDTO:
  id: int
  name: str
  enabled: bool
