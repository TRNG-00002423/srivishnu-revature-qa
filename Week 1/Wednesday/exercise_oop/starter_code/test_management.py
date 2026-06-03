"""
Phase 2 - Task 1: TestCase Class
Test Management System — models a single test case.
"""


class TestCase:
    """Represents a single test case.

    Class Attributes:
        total_created (int): Count of all TestCase objects ever created

    Instance Attributes:
        name (str): Test name (e.g., "test_login_valid")
        description (str): What this test verifies
        priority (str): "high", "medium", or "low" (default: "medium")
        tags (list): Labels like ["smoke", "regression"]
    """

    total_created = 0  # class attribute — shared across all instances

    def __init__(self, name, description="", priority="medium", tags=None):
        if not TestCase.is_valid_name(name):
            raise ValueError(f"Invalid test name '{name}'. Must start with 'test_' and contain no spaces.")

        self.name = name
        self.description = description
        self.priority = priority
        self.tags = tags if tags is not None else []

        TestCase.total_created += 1  # increment class counter on each new instance

    def run(self):
        """Simulate running the test. Returns True for pass, False for fail.
        A test fails if 'fail' appears in its name.
        """
        return "fail" not in self.name

    @classmethod
    def from_dict(cls, data):
        """Create a TestCase from a dictionary.

        Example:
            TestCase.from_dict({"name": "test_login", "priority": "high"})
        """
        return cls(
            name=data.get("name", "test_unnamed"),
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
            tags=data.get("tags", [])
        )

    @staticmethod
    def is_valid_name(name):
        """Check if name starts with 'test_' and has no spaces."""
        return isinstance(name, str) and name.startswith("test_") and " " not in name

    def __str__(self):
        return f"[{self.priority.upper()}] {self.name} — {self.description or 'No description'} | Tags: {self.tags}"

    def __repr__(self):
        return f"TestCase(name='{self.name}', priority='{self.priority}')"


# test 
if __name__ == "__main__":
    # Create via constructor
    tc1 = TestCase("test_login_valid", "Checks valid login flow", priority="high", tags=["smoke"])
    tc2 = TestCase("test_fail_checkout", "Checkout with expired card", priority="medium", tags=["regression"])

    # Create via classmethod factory
    tc3 = TestCase.from_dict({"name": "test_search_empty", "priority": "low", "tags": ["smoke"]})

    for tc in [tc1, tc2, tc3]:
        result = "PASS" if tc.run() else "FAIL"
        print(f"{result} | {tc}")

    print(f"\nTotal TestCase objects created: {TestCase.total_created}")

    # is_valid_name checks
    print("\nName validation:")
    print(f"  'test_login'     → {TestCase.is_valid_name('test_login')}")
    print(f"  'login test'     → {TestCase.is_valid_name('login test')}")
    print(f"  'check_login'    → {TestCase.is_valid_name('check_login')}")
