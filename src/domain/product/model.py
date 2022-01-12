from src.domain.category.model import Category
from src.domain.supplier.model import Supplier


class Product:
    def __init__(self, description: str, price: float, technical_details: str, image: str, visible: bool, category: Category, supplier: Supplier):
        self.description = description
        self.price = price
        self.technical_details = technical_details
        self.image = image
        self.visible = visible
        self.category = category
        self.supplier = supplier
