"""
Task 1: Input Validator
Validates a password against multiple strength criteria.
"""


def validate_password(password):
    errors = []

    # Check length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    # Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter")

    # Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        errors.append("Password must contain at least one lowercase letter")

    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one digit")

    # Check for at least one special character
    special_characters = "!@#$%^&*"
    if not any(c in special_characters for c in password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


# Test cases
if __name__ == "__main__":
    test_passwords = [
        "Abc123!x",    # valid
        "abc",         # too short, no upper, no digit, no special
        "ABCDEFGH",    # no lower, no digit, no special
        "ABCDefgh1!"   # valid
    ]

    for pwd in test_passwords:
        result = validate_password(pwd)
        print(f"\nPassword: '{pwd}'")
        print(f"  Valid: {result['valid']}")
        if result['errors']:
            for error in result['errors']:
                print(f"  - {error}")
