from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_product(description, price, technical_details, image, visible, category_id, supplier_id, uow: SqlAlchemyUnitOfWork):
    with uow:
        category_obj = uow.category_repository.get(id=category_id)
        supplier_obj = uow.supplier_repository.get(id=supplier_id)
        if not category_obj or not supplier_obj:
            return Exception
        uow.product_repository.add(Product(description=description,
                                           price=price,
                                           technical_details=technical_details,
                                           image=image,
                                           visible=visible,
                                           category=category_obj,
                                           supplier=supplier_obj))
        uow.commit()
