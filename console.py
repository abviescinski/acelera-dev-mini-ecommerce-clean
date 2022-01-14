from src.adapter.database import Session
from src.adapter.orm import start_mapper
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from services.address.address_service import create_address
from services.category.category_service import create_category
from services.coupon.coupon_service import create_coupon
from services.customer.customer_service import create_customer
from services.payment_method.payment_method_service import create_payment_method
from services.product_discount.product_discount_service import create_product_discount
from services.product.product_service import create_product
from services.supplier.supplier_service import create_supplier


start_mapper()

db = Session()

uow = SqlAlchemyUnitOfWork(db)

create_category('Categoria 1', uow)
create_supplier('Fornecedor 1', uow)
create_product(description='descricao 1', price=10, technical_details='detalhes tecnicos 1',
               image='', visible=True, category_id=1, supplier_id=1, uow=uow)

create_customer(first_name='Cliente 1', last_name='Sobrenome',
                phone_number='11111111111', genre='U', cpf_cnpj='11111111111', uow=uow)
create_address(address='rua 1', city='Cidade 1', state='ST', number='1',
               zipcode='111111', neighbourhood='', primary=True, customer_id=1, uow=uow)

create_payment_method(name='pagamento 1', enabled=True, uow=uow)
create_product_discount(mode='percentage', value='10',
                        product_id=1, payment_method_id=1, uow=uow)


#p = db.query(Product).filter_by(id=1).first()

# print(p.id)
# db.close()
"""

payment_method = PaymentMethod(name='Methodo de pagamento 5', enabled=True, id=6)
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
"""
# print(db.query(Product).filter_by(discount=1).first())
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

# print(len(p.discounts))


# p.add_discount(pd)

# print(p.id)
# db.commit()
# db.close()


# Buscando um desconto no banco de dados

#pd = db.query(ProductDiscount).filter_by(id=1).first()

# print(pd.value)
# print(pd.payment_method.name)
"""

# Testando Customer e Address
address = Address('rua 1', 'cidade 1', 'ES', '1234', '111111', '', True)
#db.add(address)
customer = Customer('cliente 1', 'sobrenome', '11111111111', 'feminino', '11111111111')
customer.add_address(address)
db.add(customer)
db.commit()

print(db.query(Customer).filter_by(id=1).first().__dict__)
#print(db.query(Customer).filter_by(addresses_id=1).first())
db.close()
"""
