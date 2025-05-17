from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models import Nutritionist, HealthData, User
from app.schemas import HealthDataCreate, NutritionistCreate
from app.services import (
    get_nutritionist_profile,
    update_nutritionist_profile,
    get_customer_health_data
)

router = APIRouter(
    prefix="/nutritionist",
    tags=["nutritionist"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)

# Route to get the nutritionist's profile
@router.get("/profile/", response_model=NutritionistCreate)
def get_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_nutritionist_profile(db=db, user_id=current_user.id)

# Route to update the nutritionist's profile
@router.put("/profile/", response_model=NutritionistCreate)
def update_profile(nutritionist: NutritionistCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_nutritionist_profile(db=db, nutritionist=nutritionist, user_id=current_user.id)

# Route to get a customer's health data
@router.get("/customer-health-data/{customer_id}", response_model=HealthDataCreate)
def get_customer_health_data(customer_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_customer_health_data(db=db, customer_id=customer_id)