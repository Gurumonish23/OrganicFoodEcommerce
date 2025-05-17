from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import Order, User, Product
from app.schemas import OrderCreate

# Service function to handle customer inquiries
def handle_customer_inquiry(user_id: int, inquiry: str, db: Session) -> str:
    # Log the inquiry in the database or send it to a customer care system
    # For simplicity, we'll just return a response string
    return f"Inquiry from user {user_id} received: {inquiry}"

# Service function to get order history for a customer
def get_order_history(user_id: int, db: Session) -> List[Order]:
    return db.query(Order).filter(Order.user_id == user_id).all()

# Service function to recommend products based on user's order history
def recommend_products(user_id: int, db: Session) -> List[Product]:
    # Fetch user's order history
    orders = get_order_history(user_id, db)
    # Extract product IDs from orders
    product_ids = {order.package_id for order in orders}
    # Recommend products not yet ordered by the user
    recommended_products = db.query(Product).filter(Product.id.notin_(product_ids)).all()
    return recommended_products

# Service function to update customer profile
def update_customer_profile(user_id: int, new_data: dict, db: Session) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    for key, value in new_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user