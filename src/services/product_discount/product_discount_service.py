from src.domain.product_discount.model import ProductDiscount
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_product_discount(mode, value, product_id, payment_method_id, uow: SqlAlchemyUnitOfWork):
    with uow:
        product_obj = uow.product_repository.get(id=product_id)
        payment_obj = uow.payment_method_repository.get(id=payment_method_id)
        if not product_obj or not payment_obj or not payment_obj.enabled:
            raise Exception
        discount_obj = ProductDiscount(mode, value, product_obj, payment_obj)
        product_obj.add_discount(discount_obj)
        uow.product_discount_repository.add(discount_obj)
        uow.commit()
