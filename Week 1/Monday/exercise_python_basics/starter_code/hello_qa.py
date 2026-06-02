"""
Hello QA — Your first Python script.
Fill in the code below where you see # TODO comments.
"""

import sys

# TODO 1: Ask the user for their name using input()
name = input("Enter your name: ")

# TODO 2: Ask the user for their role
role = input("Enter your role: ")

# TODO 3: Print a greeting using an f-string
# Expected: "Welcome, {name}! Your role is {role}."
print(f"Welcome, {name}! Your role is {role}.")

# TODO 4: Print the Python version
# Hint: sys.version_info gives you (major, minor, micro)
print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")