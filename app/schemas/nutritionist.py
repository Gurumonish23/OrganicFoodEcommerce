from pydantic import BaseModel
from typing import Optional

class NutritionistBase(BaseModel):
    user_id: int
    certification: str
    bio: Optional[str] = None
    specialties: Optional[str] = None  # e.g., Weight Loss, Sports Nutrition, etc.

class NutritionistCreate(NutritionistBase):
    pass

class Nutritionist(NutritionistBase):
    id: int

    class Config:
        orm_mode = True