from src.services.supplier.supplier_dto import SupplierDTO
from src.domain.supplier.model import Supplier
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_supplier(supplier_dto: SupplierDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        supplier = Supplier(name=supplier_dto.name)
        uow.supplier_repository.add(supplier)
        uow.commit()

    return supplier
