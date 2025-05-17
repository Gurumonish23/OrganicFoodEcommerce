from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalyticsBase(BaseModel):
    user_id: int
    action: str
    details: Optional[str] = None

class AnalyticsCreate(AnalyticsBase):
    pass

class Analytics(AnalyticsBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True