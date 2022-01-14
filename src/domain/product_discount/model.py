

from src.domain.payment_method.model import PaymentMethod


class ProductDiscount:
    def __init__(self, mode: str, value: float, product_id, payment_method: PaymentMethod):
        self.mode = mode
        self.value = value
        self.product_id = product_id
        self.payment_method = payment_method
