from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.dependencies.database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    package_id = Column(Integer, ForeignKey("packages.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False, default="Pending")  # e.g., Pending, Shipped, Delivered
    total_price = Column(Float, nullable=False)

    user = relationship("User", back_populates="orders")
    package = relationship("Package", back_populates="orders")

# Assuming a User model exists with a relationship to Order
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    orders = relationship("Order", back_populates="user")

# Assuming a Package model exists with a relationship to Order
class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    orders = relationship("Order", back_populates="package")