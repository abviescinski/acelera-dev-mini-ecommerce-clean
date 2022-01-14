from src.domain.payment_method.model import PaymentMethod
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from typing import Optional


def create_payment_method(name, enabled, uow: SqlAlchemyUnitOfWork, id: Optional[int] = None,):
    with uow:
        uow.payment_method_repository.add(PaymentMethod(name, enabled, id))
        uow.commit()
