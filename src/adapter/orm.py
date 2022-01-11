from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, Integer, String
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon

metadata = Base.metadata

table_product = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('description', String(100)),
    Column('technical_details', String(255)),
    Column('price', Float(10, 2)),
    Column('visible', Boolean),
)

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

table_coupon = Table(
    'coupon',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('mode', String(45)),
    Column('code', String(10)),
    Column('expire_at', DateTime),
    Column('limit', Integer),
    Column('value', Float),
)


def start_mapper():
    mapper(Product, table_product)
    mapper(Category, table_category)
    mapper(Supplier, table_supplier)
    mapper(Coupon, table_coupon)
