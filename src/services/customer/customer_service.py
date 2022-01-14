import re
from src.services.customer.customer_dto import CustomerDTO
from src.domain.customer.model import Customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_customer(customer_dto: CustomerDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer = Customer(customer_dto.first_name, customer_dto.last_name, 
                            customer_dto.phone_number, customer_dto.genre, 
                            customer_dto.cpf_cnpj)
        uow.customer_repository.add(customer)
        uow.commit()

    return customer
