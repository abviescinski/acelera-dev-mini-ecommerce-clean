
from src.domain.product.model import Product
from src.domain.payment_method.model import PaymentMethod



class ProductDiscount:
    def __init__(self, mode: str, value: float, product: Product, payment_method: PaymentMethod):
        self.mode = mode
        self.value = value
        self.product = product
        self.payment_method = payment_method

