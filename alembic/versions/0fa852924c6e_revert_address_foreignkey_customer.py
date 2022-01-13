"""revert address foreignkey customer

Revision ID: 0fa852924c6e
Revises: 
Create Date: 2022-01-13 11:09:47.598213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fa852924c6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coupon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mode', sa.String(length=45), nullable=True),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('expire_at', sa.DATETIME(), nullable=True),
    sa.Column('limit', sa.Integer(), nullable=True),
    sa.Column('value', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=True),
    sa.Column('last_name', sa.String(length=45), nullable=True),
    sa.Column('phone_number', sa.String(length=45), nullable=True),
    sa.Column('genre', sa.String(length=45), nullable=True),
    sa.Column('cpf_cnpj', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_method',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=45), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('number', sa.String(length=10), nullable=True),
    sa.Column('zipcode', sa.String(length=6), nullable=True),
    sa.Column('neighbourhood', sa.String(length=45), nullable=True),
    sa.Column('primary', sa.Boolean(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('technical_details', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_discount',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mode', sa.String(length=45), nullable=True),
    sa.Column('value', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('payment_method_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['payment_method_id'], ['payment_method.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_discount')
    op.drop_table('products')
    op.drop_table('address')
    op.drop_table('supplier')
    op.drop_table('payment_method')
    op.drop_table('customer')
    op.drop_table('coupon')
    op.drop_table('category')
    # ### end Alembic commands ###