from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    user_id: int
    package_id: int
    status: Optional[str] = "Pending"  # e.g., Pending, Shipped, Delivered
    total_price: float

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_date: datetime

    class Config:
        orm_mode = True