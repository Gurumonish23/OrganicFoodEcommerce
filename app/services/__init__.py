# Import all service functions to ensure they are available for use in the application
from .customer_care import (
    handle_customer_inquiry,
    get_order_history,
    recommend_products,
    update_customer_profile
)
from .payment import (
    create_payment,
    process_payment,
    refund_payment
)
from .recommendation import (
    recommend_products_based_on_orders,
    recommend_products_based_on_health,
    get_personalized_recommendations
)

# This module initializes all the services for the application
# It ensures that all service functions are imported and can be used throughout the application

__all__ = [
    "handle_customer_inquiry",
    "get_order_history",
    "recommend_products",
    "update_customer_profile",
    "create_payment",
    "process_payment",
    "refund_payment",
    "recommend_products_based_on_orders",
    "recommend_products_based_on_health",
    "get_personalized_recommendations",
]