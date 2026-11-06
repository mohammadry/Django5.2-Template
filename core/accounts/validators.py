from django.core.exceptions import ValidationError
import re

def validate_iranian_cellphone_number(value: str):
    if not re.fullmatch(r"09\d{9}", value):
        raise ValidationError("Enter a valid iranian cellphone number")