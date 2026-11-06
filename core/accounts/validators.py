from django.core.exceptions import ValidationError
import re

def validate_iranian_cellphone_number(value:str):
    pattern = r"^09\d{9}&"
    if re.match(pattern, value):
        raise ValidationError("Enter a valid iranian cellphone number")