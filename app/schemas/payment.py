from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentBase(BaseModel):
    order_id: int
    user_id: int
    amount: float
    status: Optional[str] = "Pending"  # e.g., Pending, Completed, Failed
    payment_method: str  # e.g., Credit Card, PayPal

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    payment_date: datetime

    class Config:
        orm_mode = True