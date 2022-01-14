from pydantic import BaseModel
from datetime import datetime

class CreateCouponSchema(BaseModel):
    mode: str
    code: str
    expire_at: datetime
    limit: int
    value: float
