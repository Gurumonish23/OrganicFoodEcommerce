from pydantic import BaseModel
from typing import List, Optional

class PackageBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class PackageCreate(PackageBase):
    product_ids: List[int]

class Package(PackageBase):
    id: int
    products: List[int]  # List of product IDs

    class Config:
        orm_mode = True