from pydantic import BaseModel


class CreatePaymentMethodSchema(BaseModel):
    id: int
    name: str
    enabled: bool
