from sqlalchemy.orm import Session
from app.models import Product, Order, HealthData
from typing import List

# Service function to recommend products based on user's order history
def recommend_products_based_on_orders(user_id: int, db: Session) -> List[Product]:
    # Fetch user's order history
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    # Extract product IDs from orders
    ordered_product_ids = {order.package_id for order in orders}
    # Recommend products not yet ordered by the user
    recommended_products = db.query(Product).filter(Product.id.notin_(ordered_product_ids)).all()
    return recommended_products

# Service function to recommend products based on user's health data
def recommend_products_based_on_health(user_id: int, db: Session) -> List[Product]:
    # Fetch user's health data
    health_data = db.query(HealthData).filter(HealthData.user_id == user_id).first()
    if not health_data:
        return []

    # Example logic: Recommend products based on dietary preferences
    if health_data.dietary_preferences:
        recommended_products = db.query(Product).filter(Product.category == health_data.dietary_preferences).all()
    else:
        recommended_products = db.query(Product).all()

    return recommended_products

# Service function to get personalized product recommendations
def get_personalized_recommendations(user_id: int, db: Session) -> List[Product]:
    # Combine recommendations from different strategies
    order_based_recommendations = recommend_products_based_on_orders(user_id, db)
    health_based_recommendations = recommend_products_based_on_health(user_id, db)

    # Combine and deduplicate recommendations
    recommended_products = {product.id: product for product in order_based_recommendations + health_based_recommendations}
    return list(recommended_products.values())