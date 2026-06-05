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


class TestResult:
    """The outcome of running a single test.

    Instance Attributes:
        test_name (str): Which test was run
        status (str): "pass" or "fail"
        duration_ms (float): How long it took
        error_message (str or None): Error details if failed
    """

    def __init__(self, test_name, status, duration_ms=0.0, error_message=None):
        self.test_name = test_name
        self.status = status.lower()
        self.duration_ms = duration_ms
        self.error_message = error_message

    def is_passed(self):
        """Return True if the test passed."""
        return self.status == "pass"

    def summary(self):
        """Return a one-line summary like: '✅ test_login (120ms)'"""
        icon = "✅" if self.is_passed() else "❌"
        line = f"{icon} {self.test_name} ({self.duration_ms:.1f}ms)"
        if self.error_message:
            line += f" — {self.error_message}"
        return line

    def __str__(self):
        return self.summary()

    def __repr__(self):
        return f"TestResult(test_name='{self.test_name}', status='{self.status}')"


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

    # TestResult smoke test
    print("\n── TestResult ──────────────────────────")
    tr1 = TestResult("test_login_valid", "pass", duration_ms=120.5)
    tr2 = TestResult("test_fail_checkout", "fail", duration_ms=45.0, error_message="Card declined")
    for tr in [tr1, tr2]:
        print(tr.summary())
