from src.services.payment_method.payment_method_dto import PaymentMethodDTO
from src.domain.payment_method.model import PaymentMethod
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from typing import Optional


def create_payment_method(payment_method_dto: PaymentMethodDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        payment_method = PaymentMethod(payment_method_dto.name, payment_method_dto.enabled, payment_method_dto.id)
        uow.payment_method_repository.add(payment_method)
        uow.commit()
    
    return payment_method
