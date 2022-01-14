from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.product_discount_schema import CreateProductDiscountSchema
from src.services.product_discount.product_discount_dto import ProductDiscountDTO
from src.services.product_discount.product_discount_service import create_product_discount
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateProductDiscountSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = ProductDiscountDTO(**schema.dict())
  
  product_discount = create_product_discount(dto, uow=uow)

  return product_discount