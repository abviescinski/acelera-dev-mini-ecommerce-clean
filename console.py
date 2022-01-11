from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier

from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

repository = ProductRepository(db)
product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True)

repository.add(product)

print(product.id)
print(product.description)


repository = CategoryRepository(db)
category = Category(name='Categoria 1')

repository.add(category)

print(category.id)
print(category.name)


repository = SupplierRepository(db)
supplier = Supplier(name='Fornecedor 1')

repository.add(supplier)

print(supplier.id)
print(supplier.name)