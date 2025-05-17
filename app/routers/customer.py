from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models import Product, Package, Order, Payment, HealthData
from app.schemas import OrderCreate, PaymentCreate, HealthDataCreate
from app.services import (
    get_products,
    get_packages,
    create_order,
    create_payment,
    update_health_data
)

router = APIRouter(
    prefix="/customer",
    tags=["customer"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)

# Route to get all available products
@router.get("/products/")
def list_products(db: Session = Depends(get_db)):
    return get_products(db=db)

# Route to get all available packages
@router.get("/packages/")
def list_packages(db: Session = Depends(get_db)):
    return get_packages(db=db)

# Route to create a new order
@router.post("/orders/", response_model=OrderCreate)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_order(db=db, order=order, user_id=current_user.id)

# Route to create a new payment
@router.post("/payments/", response_model=PaymentCreate)
def create_new_payment(payment: PaymentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_payment(db=db, payment=payment, user_id=current_user.id)

# Route to update health data
@router.put("/health-data/", response_model=HealthDataCreate)
def update_customer_health_data(health_data: HealthDataCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_health_data(db=db, health_data=health_data, user_id=current_user.id)