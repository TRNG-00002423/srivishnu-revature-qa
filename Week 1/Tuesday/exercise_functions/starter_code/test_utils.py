"""
Test Utilities
Helper functions for formatting and validating test names.
"""


def format_test_name(name):
    """Convert a human-readable name to a test function name.

    Example:
        format_test_name("Valid Login") → "test_valid_login"
        format_test_name("  Search Results Page  ") → "test_search_results_page"

    Rules:
        - Lowercase
        - Spaces replaced with underscores
        - Leading/trailing whitespace stripped
        - Prefixed with "test_"
    """
    formatted = name.strip().lower().replace(" ", "_")
    # collapse any multiple underscores that may result from multiple spaces
    while "__" in formatted:
        formatted = formatted.replace("__", "_")
    return "test_" + formatted


def is_valid_test_name(name):
    """Check if a string is a valid test function name.

    Rules:
        - Must start with "test_"
        - Must contain only lowercase letters, digits, and underscores
        - Must be at least 6 characters (e.g., "test_x")

    Returns: bool
    """
    if not name.startswith("test_"):
        return False
    if len(name) < 6:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789_")
    return all(c in allowed for c in name)


# --- Assertions / Self-Tests ---
if __name__ == "__main__":
    assert format_test_name("Valid Login") == "test_valid_login"
    assert format_test_name("  Search Results  ") == "test_search_results"
    assert is_valid_test_name("test_login") == True
    assert is_valid_test_name("login_test") == False
    assert is_valid_test_name("test_") == False

    print("✅ All assertions passed!")
