from pydantic import BaseModel


class CreateProductDiscountSchema(BaseModel):
    mode: str
    value: float
    product_id: int
    payment_method_id: int
