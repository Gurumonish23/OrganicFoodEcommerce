# Import all routers to ensure they are registered with the FastAPI application
from .admin import router as admin_router
from .customer import router as customer_router
from .nutritionist import router as nutritionist_router

# This module initializes all the routers for the application
# It ensures that all routers are imported and can be included in the main FastAPI application

__all__ = [
    "admin_router",
    "customer_router",
    "nutritionist_router",
]