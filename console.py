from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime
from src.domain.address.model import Address
from src.domain.customer.model import Customer
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

p = db.query(Product).filter_by(id=1).first()

print(p.id)
db.close()


payment_method = PaymentMethod(name='Methodo de pagamento 5', enabled=True, id=5)
db.add(payment_method)
product_discount = ProductDiscount(mode='value', value=50, payment_method=payment_method)
db.add(product_discount)

category = Category(name='Categoria 5')
db.add(category)
supplier = Supplier(name='Fornecedor 5')
db.add(supplier)

product = Product(description='descricao 5', price=50, technical_details='detalhes tecnicos2',
                  image='', visible=True, category=category, supplier=supplier)
db.add(product)

product.add_discount(product_discount)
print(len(product.discounts))
db.commit()
db.close()

#print(db.query(Product).filter_by(discount=1).first())
"""
payment_method2 = PaymentMethod(name='Methodo de pagamento 2', enabled=True, id=2)
db.add(payment_method2)
product_discount2 = ProductDiscount(mode='value', value=20, payment_method=payment_method2)
db.add(product_discount2)

#product2 = Product(description='descricao 2', price=20, technical_details='detalhes tecnicos 2',
#                  image='', visible=True, category=category, supplier=supplier)

product.add_discount(product_discount2)

db.commit()
db.close()
"""
"""

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
"""

# Adicionando um novo desconto

#p = db.query(Product).filter_by(id=1).first()

# pm = db.query(PaymentMethod).filter_by(id=1).first()
#pm = PaymentMethod('cartão de crédito', enabled=True, id=3)

#pd = ProductDiscount(mode='value', value=100, payment_method=pm)

#print(len(p.discounts))


#p.add_discount(pd)

#print(p.id)
#db.commit()
#db.close()


# Buscando um desconto no banco de dados

#pd = db.query(ProductDiscount).filter_by(id=1).first()

#print(pd.value)
#print(pd.payment_method.name)


# Testando Customer e Address
address = Address('rua 1', 'cidade 1', 'ES', '1234', '111111', '', True)
db.add(address)
customer = Customer('cliente 1', 'sobrenome', '11111111111', 'feminino', '11111111111')
customer.add_address(address)
db.add(customer)
db.commit()
db.close()

print(db.query(Customer).filter_by(id=1).first().__dict__)
print(db.query(Customer).filter_by(addresses_id=1).first())