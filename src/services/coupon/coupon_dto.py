from dataclasses import dataclass
from datetime import datetime


@dataclass
class CouponDTO:
  mode: str
  code: str
  expire_at: datetime
  limit: int
  value: float