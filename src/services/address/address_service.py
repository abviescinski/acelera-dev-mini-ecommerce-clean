from src.domain.address.model import Address
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_address(address, city, state, number, zipcode, neighbourhood, primary, customer_id, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer_obj = uow.customer_repository.get(id=customer_id)
        if not customer_obj:
            return Exception
        address_obj = Address(address, city, state, number,
                              zipcode, neighbourhood, primary, customer_id)
        customer_obj.add_address(address_obj)
        uow.address_repository.add(address_obj)
        uow.commit()
