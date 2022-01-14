from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.coupon_schema import CreateCouponSchema
from src.services.coupon.coupon_dto import CouponDTO
from src.services.coupon.coupon_service import create_coupon
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateCouponSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = CouponDTO(**schema.dict())
  
  coupon = create_coupon(dto, uow=uow)

  return coupon