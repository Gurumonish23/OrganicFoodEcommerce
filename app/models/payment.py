from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.dependencies.database import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False, default="Pending")  # e.g., Pending, Completed, Failed
    payment_method = Column(String, nullable=False)  # e.g., Credit Card, PayPal

    order = relationship("Order", back_populates="payments")
    user = relationship("User", back_populates="payments")

# Assuming an Order model exists with a relationship to Payment
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    payments = relationship("Payment", back_populates="order")

# Assuming a User model exists with a relationship to Payment
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    payments = relationship("Payment", back_populates="user")