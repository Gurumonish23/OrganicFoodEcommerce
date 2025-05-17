from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.dependencies.database import Base

class Nutritionist(Base):
    __tablename__ = "nutritionists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    certification = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    specialties = Column(String, nullable=True)  # e.g., Weight Loss, Sports Nutrition, etc.

    user = relationship("User", back_populates="nutritionist")

# Assuming a User model exists with a relationship to Nutritionist
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    nutritionist = relationship("Nutritionist", back_populates="user")