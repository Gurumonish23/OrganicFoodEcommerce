from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_admin_user
from app.models import Product, Package, Order, Analytics, Payment, HealthData, Nutritionist
from app.schemas import ProductCreate, PackageCreate, OrderCreate, PaymentCreate, AnalyticsCreate, HealthDataCreate, NutritionistCreate
from app.services import (
    create_product,
    create_package,
    create_order,
    create_payment,
    create_analytics,
    create_health_data,
    create_nutritionist
)

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_current_admin_user)],
    responses={404: {"description": "Not found"}},
)

# Route to create a new product
@router.post("/products/", response_model=ProductCreate)
def admin_create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

# Route to create a new package
@router.post("/packages/", response_model=PackageCreate)
def admin_create_package(package: PackageCreate, db: Session = Depends(get_db)):
    return create_package(db=db, package=package)

# Route to create a new order
@router.post("/orders/", response_model=OrderCreate)
def admin_create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)

# Route to create a new payment
@router.post("/payments/", response_model=PaymentCreate)
def admin_create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db=db, payment=payment)

# Route to create a new analytics entry
@router.post("/analytics/", response_model=AnalyticsCreate)
def admin_create_analytics(analytics: AnalyticsCreate, db: Session = Depends(get_db)):
    return create_analytics(db=db, analytics=analytics)

# Route to create a new health data entry
@router.post("/health-data/", response_model=HealthDataCreate)
def admin_create_health_data(health_data: HealthDataCreate, db: Session = Depends(get_db)):
    return create_health_data(db=db, health_data=health_data)

# Route to create a new nutritionist
@router.post("/nutritionists/", response_model=NutritionistCreate)
def admin_create_nutritionist(nutritionist: NutritionistCreate, db: Session = Depends(get_db)):
    return create_nutritionist(db=db, nutritionist=nutritionist)