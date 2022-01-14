from src.services.product.product_dto import ProductDTO
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_product(product_dto: ProductDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        category_obj = uow.category_repository.get(id=product_dto.category_id)
        supplier_obj = uow.supplier_repository.get(id=product_dto.supplier_id)
        if not category_obj or not supplier_obj:
            return Exception

        product = Product(description=product_dto.description,
                          price=product_dto.price,
                          technical_details=product_dto.technical_details,
                          image=product_dto.image,
                          visible=product_dto.visible,
                          category=category_obj,
                          supplier=supplier_obj)
        uow.product_repository.add(product)
        uow.commit()
    return product
