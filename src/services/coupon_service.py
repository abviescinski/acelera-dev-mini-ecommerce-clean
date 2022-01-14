from src.domain.coupon.model import Coupon
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_coupon(mode, code, expire_at, limit, value, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.coupon_repository.add(Coupon(mode, code, expire_at, limit, value))
        uow.commit()
