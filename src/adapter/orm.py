from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DATETIME, Boolean, Float, Integer, String, Numeric
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.domain.address.model import Address
from src.domain.customer.model import Customer

metadata = Base.metadata

table_category = Table(
    'category',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(45)),
)

table_supplier = Table(
    'supplier',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(45)),
)

table_product = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('description', String(100)),
    Column('technical_details', String(255)),
    Column('price', Float(10, 2)),
    Column('visible', Boolean),
    Column('category_id', ForeignKey('category.id')),
    Column('supplier_id', ForeignKey('supplier.id'))
)

table_coupon = Table(
    'coupon',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('mode', String(45)),
    Column('code', String(10)),
    Column('expire_at', DATETIME),
    Column('limit', Integer),
    Column('value', Numeric(10, 2)),
)

table_payment_method = Table(
    'payment_method',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(45)),
    Column('enabled', Boolean, default=True),
)

table_product_discount = Table(
    'product_discount',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('mode', String(45)),
    Column('value', Numeric(10, 2)),
    Column('product_id', ForeignKey('products.id')),
    Column('payment_method_id', ForeignKey('payment_method.id')),
)

table_address = Table(
    'address',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('address', String),
    Column('city', String(45)),
    Column('state', String(2)),
    Column('number', String(10)),
    Column('zipcode', String(6)),
    Column('neighbourhood', String(45)),
    Column('primary', Boolean),
)

table_customer = Table(
    'customer',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('first_name', String(45)),
    Column('last_name', String(45)),
    Column('phone_number', String(45)),
    Column('genre', String(45)),
    Column('cpf_cnpj', String(45)),
    Column('addresses_id', ForeignKey('address.id'))
)


def start_mapper():
    category_mapper = mapper(Category, table_category)
    supplier_mapper = mapper(Supplier, table_supplier)
    payment_method_mapper = mapper(PaymentMethod, table_payment_method)
    mapper(Coupon, table_coupon)

    product_discount_mapper = mapper(ProductDiscount, table_product_discount, properties={
        'payment_method': relationship(payment_method_mapper)
    })

    product_mapper = mapper(Product, table_product, properties={
        'category': relationship(category_mapper),
        'supplier': relationship(supplier_mapper),
        'discounts': relationship(product_discount_mapper)
    })

    address_mapper = mapper(Address, table_address)
    customer_mapper = mapper(Customer, table_customer, properties={
        'address': relationship(address_mapper)
    })
