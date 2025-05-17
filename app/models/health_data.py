from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.dependencies.database import Base

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    height = Column(Float, nullable=True)  # Height in centimeters
    weight = Column(Float, nullable=True)  # Weight in kilograms
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    activity_level = Column(String, nullable=True)  # e.g., Sedentary, Active, etc.
    dietary_preferences = Column(String, nullable=True)  # e.g., Vegan, Vegetarian, etc.

    user = relationship("User", back_populates="health_data")

# Assuming a User model exists with a relationship to HealthData
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    health_data = relationship("HealthData", back_populates="user")