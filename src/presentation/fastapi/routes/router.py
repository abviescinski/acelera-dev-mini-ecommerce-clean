from fastapi import APIRouter
from src.presentation.fastapi.routes.address_route import router as address_route
from src.presentation.fastapi.routes.category_route import router as category_route
from src.presentation.fastapi.routes.coupon_route import router as coupon_route
from src.presentation.fastapi.routes.customer_route import router as customer_route
from src.presentation.fastapi.routes.payment_method_route import router as payment_method_route
from src.presentation.fastapi.routes.product_discount_route import router as product_discount_route
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.supplier_route import router as supplier_route

router = APIRouter()

router.include_router(category_route, prefix='/category', tags=['category'])
router.include_router(supplier_route, prefix='/supplier', tags=['supplier'])
router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(payment_method_route, prefix='/payment_method', tags=['payment_method'])
router.include_router(product_discount_route, prefix='/product_discount', tags=['product_discount'])
router.include_router(coupon_route, prefix='/coupon', tags=['coupon'])
router.include_router(customer_route, prefix='/customer', tags=['customer'])
router.include_router(address_route, prefix='/address', tags=['address'])

