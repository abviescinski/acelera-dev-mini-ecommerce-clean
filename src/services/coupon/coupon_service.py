from src.services.coupon.coupon_dto import CouponDTO
from src.domain.coupon.model import Coupon
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_coupon(coupon_dto: CouponDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        coupon_obj = Coupon(coupon_dto.mode, coupon_dto.code, 
                            coupon_dto.expire_at, coupon_dto.limit, 
                            coupon_dto.value)
        uow.coupon_repository.add(coupon_obj)
        uow.commit()

    return coupon_obj
