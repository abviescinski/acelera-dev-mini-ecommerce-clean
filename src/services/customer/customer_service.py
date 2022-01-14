from src.domain.customer.model import Customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_customer(first_name, last_name, phone_number, genre, cpf_cnpj, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.customer_repository.add(
            Customer(first_name, last_name, phone_number, genre, cpf_cnpj))
        uow.commit()
