# scripts/python_fundamentals.py

"""
Python Fundamentals - Beginner Friendly Overview

This script introduces core Python concepts step-by-step:
- Printing output
- Variables and data types
- User input
- Comments
- Lists and loops
- Conditional statements
- Functions
- Basic error handling
"""

# 1. Printing output
print("Hello, world!")  # Simple print statement

# 2. Variables and data types
name = "Officer Smith"       # String (text)
age = 37                     # Integer (whole number)
height = 5.9                 # Float (decimal number)
is_on_duty = True            # Boolean (True/False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("On Duty?", is_on_duty)

# 3. User input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Welcome", user_name + "! You are", user_age, "years old.")

# 4. Comments
# This is a single-line comment explaining the code below

"""
This is a multi-line comment (or docstring) that can span
multiple lines and is often used to explain complex code blocks
or scripts.
"""

# 5. Lists (collections of items)
websites = ["example.com", "openintel.gov", "darkwebtracker.info"]
print("\nList of websites:")
print(websites)

# Accessing list items by index (starts at 0)
print("First website:", websites[0])

# Adding an item to the list
websites.append("newsite.org")
print("Updated websites:", websites)

# 6. Loops (repeat actions)
print("\nLooping through websites:")
for site in websites:
    print("Checking site:", site)

# 7. Conditional statements (making decisions)
print("\nChecking for priority sites:")
for site in websites:
    if "darkweb" in site:
        print(f"ALERT: High priority target found: {site}")
    elif "openintel" in site:
        print(f"Note: Open intel site: {site}")
    else:
        print(f"Regular site: {site}")

# 8. Functions - reusable blocks of code
def greet_officer(name):
    """Function that greets an officer by name."""
    print(f"\nHello, Officer {name}! Ready to start OSINT?")

greet_officer("Smith")

# Function with return value
def calculate_years_to_retirement(age, retirement_age=65):
    """Calculate years left until retirement."""
    years_left = retirement_age - age
    if years_left < 0:
        return 0
    return years_left

years_left = calculate_years_to_retirement(age)
print(f"Years until retirement: {years_left}")

# 9. Error handling with try-except
print("\nLet's try dividing numbers:")

try:
    numerator = int(input("Enter numerator (number): "))
    denominator = int(input("Enter denominator (number): "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print(f"Result of division: {result}")

# 10. Summary print
print("\n--- End of Python Fundamentals Demo ---")
