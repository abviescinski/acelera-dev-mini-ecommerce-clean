from src.services.category.category_dto import CategoryDTO
from src.domain.category.model import Category
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_category(category_dto: CategoryDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        category_obj = Category(name=category_dto.name)
        uow.category_repository.add(category_obj)
        uow.commit()

    return category_obj
