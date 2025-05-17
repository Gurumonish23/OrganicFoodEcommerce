# Import necessary dependencies for the application
from .auth import get_current_user, get_current_admin_user
from .database import get_db

# This module initializes the dependencies for authentication and database access
# It provides functions to retrieve the current user and admin user based on authentication tokens
# It also provides a function to get a database session for interacting with the database

__all__ = [
    "get_current_user",
    "get_current_admin_user",
    "get_db",
]