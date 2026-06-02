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


def create_test_result(name, status="pass", duration_ms=0, error=None):
    """Create a test result dictionary.

    Args:
        name: Test name (required)
        status: "pass" or "fail" (default: "pass")
        duration_ms: Execution time in ms (default: 0)
        error: Error message if failed (default: None)

    Returns:
        dict with keys: name, status, duration_ms, error
    """
    return {
        "name":        name,
        "status":      status,
        "duration_ms": duration_ms,
        "error":       error,
    }


def format_duration(ms, unit="ms"):
    """Format a duration value with the specified unit.

    Args:
        ms: Duration in milliseconds
        unit: "ms", "s", or "min" (default: "ms")

    Returns:
        Formatted string like "1,200ms" or "1.20s" or "0.02min"
    """
    if unit == "ms":
        return f"{ms:,}ms"
    elif unit == "s":
        return f"{ms / 1000:.2f}s"
    elif unit == "min":
        return f"{ms / 60000:.2f}min"
    else:
        raise ValueError(f"Unknown unit: {unit!r}. Use 'ms', 's', or 'min'.")


def calculate_stats(*scores):
    """Calculate statistics for any number of scores.

    Returns:
        dict with keys: count, total, average, min, max

    Raises:
        ValueError if no scores provided
    """
    if not scores:
        raise ValueError("At least one score is required.")
    return {
        "count":   len(scores),
        "total":   sum(scores),
        "average": round(sum(scores) / len(scores), 1),
        "min":     min(scores),
        "max":     max(scores),
    }


def build_test_config(**settings):
    """Build a test configuration with defaults.

    Default config:
        browser: "chrome"
        headless: False
        timeout: 30
        retries: 0
        base_url: "http://localhost:3000"

    Any **settings passed override the defaults.

    Returns: dict
    """
    defaults = {
        "browser":  "chrome",
        "headless": False,
        "timeout":  30,
        "retries":  0,
        "base_url": "http://localhost:3000",
    }
    defaults.update(settings)
    return defaults


# --- Assertions / Self-Tests ---
if __name__ == "__main__":
    assert format_test_name("Valid Login") == "test_valid_login"
    assert format_test_name("  Search Results  ") == "test_search_results"
    assert is_valid_test_name("test_login") == True
    assert is_valid_test_name("login_test") == False
    assert is_valid_test_name("test_") == False

    # Task 2 assertions
    r1 = create_test_result("test_login")
    assert r1 == {"name": "test_login", "status": "pass", "duration_ms": 0, "error": None}

    r2 = create_test_result("test_checkout", status="fail", duration_ms=2300, error="Timeout")
    assert r2["status"] == "fail"
    assert r2["error"] == "Timeout"

    assert format_duration(1200) == "1,200ms"
    assert format_duration(1200, "s") == "1.20s"

    # Task 3 assertions
    stats = calculate_stats(85, 92, 78, 95, 88)
    assert stats["count"] == 5
    assert stats["average"] == 87.6
    assert stats["min"] == 78
    assert stats["max"] == 95

    config = build_test_config(headless=True, timeout=60)
    assert config["browser"] == "chrome"  # default
    assert config["headless"] == True     # overridden
    assert config["timeout"] == 60        # overridden

    print("✅ All assertions passed!")
