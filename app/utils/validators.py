import re
from typing import Any

# Validator function to check if a string is a valid email address
def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Validator function to check if a string is a valid phone number
def validate_phone_number(phone_number: str) -> bool:
    phone_regex = r'^\+?1?\d{9,15}$'  # International format
    return re.match(phone_regex, phone_number) is not None

# Validator function to check if a value is a positive integer
def validate_positive_integer(value: Any) -> bool:
    return isinstance(value, int) and value > 0

# Validator function to check if a string is a valid URL
def validate_url(url: str) -> bool:
    url_regex = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return re.match(url_regex, url) is not None

# Validator function to check if a string is a valid credit card number
def validate_credit_card_number(card_number: str) -> bool:
    card_regex = r'^\d{13,19}$'  # Basic check for length and digits
    return re.match(card_regex, card_number) is not None