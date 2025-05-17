from pydantic import BaseModel
from typing import Optional

class HealthDataBase(BaseModel):
    user_id: int
    height: Optional[float] = None  # Height in centimeters
    weight: Optional[float] = None  # Weight in kilograms
    age: Optional[int] = None
    gender: Optional[str] = None
    activity_level: Optional[str] = None  # e.g., Sedentary, Active, etc.
    dietary_preferences: Optional[str] = None  # e.g., Vegan, Vegetarian, etc.

class HealthDataCreate(HealthDataBase):
    pass

class HealthData(HealthDataBase):
    id: int

    class Config:
        orm_mode = True