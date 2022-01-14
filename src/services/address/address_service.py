from src.services.address.address_dto import AddresstDTO
from src.domain.address.model import Address
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_address(address_dto: AddresstDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer_obj = uow.customer_repository.get(id=address_dto.customer_id)
        if not customer_obj:
            return Exception
        address_obj = Address(address_dto.address, address_dto.city,
                              address_dto.state, address_dto.number,
                              address_dto.zipcode, address_dto.neighbourhood,
                              address_dto.primary, address_dto.customer_id)
        customer_obj.add_address(address_obj)
        uow.address_repository.add(address_obj)
        uow.commit()
    return address_obj
