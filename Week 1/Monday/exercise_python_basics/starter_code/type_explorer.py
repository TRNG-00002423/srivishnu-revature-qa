"""
Data Type Explorer
Explores Python's primitive types and key operators.
"""

# --- Variable Declarations ---
age       = 28
price     = 19.99
name      = "Alice"
is_active = True
result    = None

print("Variable Exploration:")
print(f"  {'age':<12}= {str(age):<12} (type: {type(age).__name__})")
print(f"  {'price':<12}= {str(price):<12} (type: {type(price).__name__})")
print(f"  {'name':<12}= {str(name):<12} (type: {type(name).__name__})")
print(f"  {'is_active':<12}= {str(is_active):<12} (type: {type(is_active).__name__})")
print(f"  {'result':<12}= {str(result):<12} (type: {type(result).__name__})")

# --- Operators Demo ---
print()
print("Operators Demo:")
print(f"  17 // 5     = {17 // 5:<12} (floor division)")
print(f"  17 / 5      = {17 / 5:<12} (true division)")
print(f"  \"QA \" * 3  = {'QA ' * 3}")
print(f"  True + True = {True + True}")

# --- Floating-Point Precision Gotcha ---
print()
print("Precision Gotcha:")
print(f"  0.1 + 0.2  = {0.1 + 0.2} (not exactly 0.3!)")

# --- == vs is ---
print()
print("== vs is:")

# Example 1: small integers (cached by Python — same object)
a = 100
b = 100
print(f"  a = 100, b = 100")
print(f"  a == b  → {a == b}   (values are equal)")
print(f"  a is b  → {a is b}   (same object in memory — Python caches small ints)")

# Example 2: lists (equal values, different objects)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"  list1 = [1,2,3], list2 = [1,2,3]")
print(f"  list1 == list2  → {list1 == list2}   (values are equal)")
print(f"  list1 is list2  → {list1 is list2}  (different objects in memory)")
