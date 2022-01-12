from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.product_discount_repository import ProductDiscountRepository
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount

from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

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


repository = ProductRepository(db)
product = Product(description='descricao 4', price=14, technical_details='detalhes tecnicos',
                  image='', visible=True, category=category, supplier=supplier)

repository.add(product)

print(product.id)
print(product.description)


repository = CouponRepository(db)
coupon = Coupon(code='codigo1', mode='percentage',
                expire_at=datetime.now(), value=10, limit=5)

repository.add(coupon)

print(coupon.id)
print(coupon.code)


repository = PaymentMethodRepository(db)
payment_method = PaymentMethod(name='Methodo de pagamento 1', enabled=True)

repository.add(payment_method)

print(payment_method.id)
print(payment_method.name)


repository = ProductDiscountRepository(db)
product_discount = ProductDiscount(
    mode='value', value=10, product=product, payment_method=payment_method)

repository.add(product_discount)

print(product_discount.id)
