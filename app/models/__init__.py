# Import all models to ensure they are registered with SQLAlchemy's Base
from .product import Product
from .package import Package
from .order import Order
from .payment import Payment
from .analytics import Analytics
from .health_data import HealthData
from .nutritionist import Nutritionist

# This module initializes all the models for the application
# It ensures that all models are imported and registered with the SQLAlchemy Base
# This is necessary for creating the database tables and establishing relationships

__all__ = [
    "Product",
    "Package",
    "Order",
    "Payment",
    "Analytics",
    "HealthData",
    "Nutritionist",
]