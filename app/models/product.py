from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.dependencies.database import Base
from app.models.package import package_product_association

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    category = Column(String, nullable=True)  # e.g., Vegetables, Fruits, Dairy

    packages = relationship("Package", secondary=package_product_association, back_populates="products")