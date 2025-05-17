import random
import string
from typing import List, Dict, Any

# Helper function to generate a random string of specified length
def generate_random_string(length: int = 8) -> str:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Helper function to calculate the total price of a list of items
def calculate_total_price(items: List[Dict[str, Any]]) -> float:
    return sum(item['price'] * item.get('quantity', 1) for item in items)

# Helper function to format a user's full name
def format_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.strip().title()} {last_name.strip().title()}"

# Helper function to validate an email address format
def is_valid_email(email: str) -> bool:
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Helper function to convert a list of dictionaries to a dictionary with a specified key
def list_to_dict(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {item[key]: item for item in items if key in item}