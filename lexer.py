# Chubi Adejoh
# Homework 1
# CS 3500

import sys

def is_integer(s):
    """Checks if a string is an integer."""
    if not s:
        return False
    if s[0] in "+-":
        s = s[1:]
    return s.isdigit()

def is_scientific(s):
    """Checks if a string is a number in scientific notation."""
    if not s:
        return False
    
    # Split the input 'E'
    parts = s.split('E')
    
    # Ensure exactly one 'E' is present
    if len(parts) != 2:
        return False
    
    valid_decimal_or_integer, exponent = parts
    
    # Valid decimal or integer (positive or negative)
    if not (is_decimal(valid_decimal_or_integer) or is_integer(valid_decimal_or_integer)):
        return False
    
    # Exponent must be a valid integer (positive or negative), non-zero
    if not is_integer(exponent) or exponent == "0":
        return False
    
    return True

def is_decimal(s):
    """Checks if a string is a decimal number."""
    if not s:
        return False
    parts = s.split('.')
    if len(parts) != 2:
        return False
    if not parts[0] and not parts[1]:  # Handle case like '.'
        return False
    return (is_integer(parts[0]) or not parts[0]) and parts[1].isdigit()

def is_hexadecimal(s):
    """Checks if a string is a hexadecimal number."""
    if not s or len(s) < 3 or not s.endswith('H'):
        return False
    hex_digits = s[:-1]  # Exclude 'H'
    for c in hex_digits:
        if c.lower() not in '0123456789abcdef':
            return False
    return True

def is_character_literal(s):
    """Checks if a string is a character literal."""
    if not s or len(s) != 3 or not s.endswith('X'):
        return False
    hex_digits = s[:-1]  # Exclude 'X'
    return len(hex_digits) == 2 and all(c in '0123456789abcdef' for c in hex_digits.lower())

def is_keyword(s):
    """Checks if a string is a keyword."""
    keywords = ['DEF', 'IF', 'FI', 'LOOP', 'POOL', 'PRINT']
    return s.upper() in keywords

def is_string_literal(s):
    """Checks if a string is a string literal."""
    if not s or len(s) < 2:
        return False
    return s.startswith('"') and s.endswith('"') and '"' not in s[1:-1] and len(s) > 2

def is_identifier(s):
    """Checks if a string is an identifier."""
    if is_keyword(s) or is_hexadecimal(s) or is_character_literal(s):
        return False
    if not s:
        return False
    if not s[0].isalpha() and s[0] != '_':
        return False
    for c in s[1:]:
        if not c.isalnum() and c != '_':
            return False
    return True

def classify_token(token):
    """Classifies a token based on its content."""
    if not token:
        return "INVALID!"

    if is_keyword(token):
        return "Keyword"
    elif is_integer(token):
        return "Integer"
    elif is_decimal(token):
        return "Decimal"
    elif is_scientific(token):
        return "Scientific"
    elif is_hexadecimal(token):
        return "Hexadecimal"
    elif is_string_literal(token):
        return "String"
    elif is_character_literal(token):
        return "Character"
    elif is_identifier(token):
        return "Identifier"
    else:
        return "INVALID!"

def lexical_analyzer():
    """Performs lexical analysis on a given input."""
    # Read number of input strings
    N = int(input().strip())

    # Process each input string
    for i in range(1, N + 1):
        token = input().strip()
        token_type = classify_token(token)
        print(f"{i}: {token_type}")

# Example usage
if __name__ == "__main__":
    lexical_analyzer()