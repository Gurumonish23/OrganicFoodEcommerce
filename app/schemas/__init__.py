# Import all schema models to ensure they are available for use in the application
from .product import Product, ProductCreate
from .package import Package, PackageCreate
from .order import Order, OrderCreate
from .payment import Payment, PaymentCreate
from .analytics import Analytics, AnalyticsCreate
from .health_data import HealthData, HealthDataCreate
from .nutritionist import Nutritionist, NutritionistCreate

# This module initializes all the schemas for the application
# It ensures that all schemas are imported and can be used for request and response validation

__all__ = [
    "Product",
    "ProductCreate",
    "Package",
    "PackageCreate",
    "Order",
    "OrderCreate",
    "Payment",
    "PaymentCreate",
    "Analytics",
    "AnalyticsCreate",
    "HealthData",
    "HealthDataCreate",
    "Nutritionist",
    "NutritionistCreate",
]