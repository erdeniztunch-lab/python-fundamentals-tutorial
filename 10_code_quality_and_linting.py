# ============================================
# CODE QUALITY AND LINTING
# ============================================

# --------------------------------------------
# WHAT IS LINTING?
# --------------------------------------------

# Linting is checking your code for:
# - Style mistakes
# - Potential bugs
# - Code that's hard to read

# Think of it like spell-check for code!

# Why use linting?
# - Catch errors before running code
# - Make code easier to read
# - Learn good coding habits
# - Follow Python standards

# --------------------------------------------
# PYTHON CODING STANDARDS (PEP 8)
# --------------------------------------------

# PEP 8 is Python's official style guide
# It tells you how to write clean, readable code

# Rule 1: Use 4 spaces for indentation
# ❌ BAD (only 2 spaces - shown in comment below)
# if True:
#   print("Wrong")  # Only 2 spaces - this is incorrect!

# ✅ GOOD
if True:
    print("Correct")  # 4 spaces

# Rule 2: Add spaces around operators
# ❌ BAD (no spaces)
# result=5+3*2

# ✅ GOOD
result = 5 + 3 * 2

# Rule 3: Use blank lines to separate sections
# ❌ BAD (no blank line between functions)
# def function1():
#     print("Hello")
# def function2():
#     print("World")

# ✅ GOOD


def function1():
    print("Hello")


def function2():
    print("World")


# Rule 4: Keep lines under 79 characters
# ❌ BAD (line too long - shown in comment)
# message = "This is a very long line that goes on and on and makes the code hard to read"

# ✅ GOOD
message = "This is a shorter line"
# Or split long lines:
message = (
    "This is a very long line "
    "split across multiple lines"
)

# Rule 5: Use lowercase with underscores for variables
# ❌ BAD
# MyVariable = 10
# my-variable = 10  # This causes a syntax error!

# ✅ GOOD
my_variable = 10

# Rule 6: Use descriptive names
# ❌ BAD (not descriptive)
# x = 10
# y = 20

# ✅ GOOD
width = 10
height = 20

# --------------------------------------------
# FUNCTION NAMING
# --------------------------------------------

# Functions should:
# - Use lowercase with underscores
# - Start with a verb (action word)
# - Be descriptive

# ❌ BAD


def f():
    """Bad function name - too short."""
    pass


def MyFunction():
    """Bad function name - uses CamelCase instead of snake_case."""
    pass


# ✅ GOOD


def calculate_total():
    """Good function name - descriptive and uses snake_case."""
    pass


def get_user_name():
    """Good function name - starts with verb."""
    pass


def send_email():
    """Good function name - clear action."""
    pass


# --------------------------------------------
# COMMENTING YOUR CODE
# --------------------------------------------

# Good comments explain WHY, not WHAT

# ❌ BAD COMMENT (states the obvious)
x = 0
x = x + 1  # Add 1 to x

# ✅ GOOD COMMENT (explains the reason)
y = 0
y = y + 1  # Account for 1-based indexing

# ❌ BAD (no comment when needed)
score = 85
attendance = 90
# if score * 0.6 + attendance * 0.4 >= 70:
#     print("Pass")

# ✅ GOOD (explains complex logic)
# Final grade is 60% score, 40% attendance
# Passing grade is 70
if score * 0.6 + attendance * 0.4 >= 70:
    print("Pass")

# --------------------------------------------
# FUNCTIONS SHOULD BE FOCUSED
# --------------------------------------------

# Each function should do ONE thing

# ❌ BAD (does too much)
# This function example shows what NOT to do - it handles everything


def read_file():
    """Dummy function for example."""
    return "data"


def clean_data(data):
    """Dummy function for example."""
    return data


def analyze(data):
    """Dummy function for example."""
    return data


def create_report(data):
    """Dummy function for example."""
    return data


def send_email_report(data):
    """Dummy function for example."""
    pass


def process_data():
    """BAD: This function does too many things."""
    # Read file
    data = read_file()
    # Clean data
    cleaned = clean_data(data)
    # Analyze data
    results = analyze(cleaned)
    # Generate report
    report = create_report(results)
    # Send email
    send_email_report(report)
    return report


# ✅ GOOD (separate functions)


def read_and_clean_data():
    """GOOD: Focused on reading and cleaning."""
    data = read_file()
    return clean_data(data)


def process_and_report(data):
    """GOOD: Focused on processing and reporting."""
    results = analyze(data)
    report = create_report(results)
    return report


def complete_workflow():
    """GOOD: Orchestrates the workflow by calling focused functions."""
    data = read_and_clean_data()
    report = process_and_report(data)
    send_email_report(report)
    return report


# --------------------------------------------
# USING LINTING TOOLS
# --------------------------------------------

# Popular Python linting tools:
# 1. pylint - Comprehensive checker
# 2. flake8 - Fast and simple
# 3. black - Auto-formats code
# 4. mypy - Checks types

# Installing a linter (using terminal):
# pip install pylint
# pip install flake8
# pip install black

# Using pylint (in terminal):
"""
# Check a file
pylint myfile.py

# Example output:
# myfile.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# myfile.py:3:0: C0103: Variable name "X" doesn't conform to snake_case
# 
# Your code has been rated at 7.50/10
"""

# Using flake8 (in terminal):
"""
# Check a file
flake8 myfile.py

# Example output:
# myfile.py:1:1: E302 expected 2 blank lines, found 1
# myfile.py:5:80: E501 line too long (85 > 79 characters)
"""

# Using black (auto-fixes formatting):
"""
# Format a file
black myfile.py

# Black will automatically fix:
# - Indentation
# - Spacing
# - Line length
# - Quote style
"""

# --------------------------------------------
# IDE LINTING (BUILT-IN)
# --------------------------------------------

# Most code editors have built-in linting:

# VS Code:
# - Install Python extension
# - Linting happens automatically
# - Squiggly underlines show problems
# - Hover over them to see what's wrong

# PyCharm:
# - Linting is built-in
# - Yellow/red highlights show issues
# - Right-click to see suggested fixes

# --------------------------------------------
# COMMON LINTING WARNINGS
# --------------------------------------------

# Warning: Line too long
# Solution: Break into multiple lines
# ❌ BAD
# result = some_function(parameter1, parameter2, parameter3, parameter4, parameter5)

# ✅ GOOD
# result = some_function(
#     parameter1,
#     parameter2,
#     parameter3,
#     parameter4,
#     parameter5
# )

# Warning: Unused variable
# Solution: Remove it or use it
# ❌ BAD


def calculate_total_bad(a, b, c):
    """BAD: Parameter 'c' is never used."""
    return a + b  # 'c' is never used


# ✅ GOOD


def calculate_total_good(a, b):
    """GOOD: Only the parameters we actually use."""
    return a + b


# Warning: Undefined variable
# Solution: Define it first
# ❌ BAD (shown in comment)
# print(result)  # 'result' is not defined - this would cause an error!

# ✅ GOOD
final_result = 10
print(final_result)

# Warning: Import not used
# Solution: Remove unused imports
# ❌ BAD (shown in comment)
# import math
# import random
# print("Hello")  # Neither math nor random is used

# ✅ GOOD
print("Hello")  # No unnecessary imports

# --------------------------------------------
# BEFORE AND AFTER EXAMPLES
# --------------------------------------------

# ❌ BAD: No linting


def calculate_bad(x, y, z):
    """Example of poorly formatted code."""
    if x > y:
        result_bad = x+y+z  # No spaces around operators
    else:
        result_bad = x-y-z  # No spaces around operators
    return result_bad


total_bad = calculate_bad(5, 3, 2)
print(total_bad)

# ✅ GOOD: After linting


def calculate_good(x, y, z):
    """Calculate result based on x, y, z values."""
    if x > y:
        result_good = x + y + z
    else:
        result_good = x - y - z
    return result_good


total_good = calculate_good(5, 3, 2)
print(total_good)

# --------------------------------------------
# PRACTICAL TIPS
# --------------------------------------------

# 1. Set up linting in your editor
#    - Install Python extension/plugin
#    - Enable automatic formatting
#    - Save time and learn good habits

# 2. Run linting before sharing code
#    - Quick check: flake8 yourfile.py
#    - Fix major issues
#    - Your code looks professional

# 3. Don't obsess over perfect scores
#    - 8/10 or higher is fine
#    - Some warnings are okay to ignore
#    - Readable code > perfect score

# 4. Learn from the warnings
#    - Each warning teaches you something
#    - Over time, you'll write better code naturally
#    - Eventually you'll need fewer corrections

# 5. Use auto-formatters
#    - Black formats code automatically
#    - Saves time on manual fixes
#    - Consistent style across projects

# --------------------------------------------
# EXAMPLE: FIXING LINTING ISSUES
# --------------------------------------------

# Original code with issues (shown in comment):
"""
def calculate_price(price,discount,tax):
    if discount>0:
        price=price-discount
    total=price+(price*tax)
    return total

result=calculate_price(100,10,.08)
print(result)
"""

# After running flake8, we see:
# - Missing spaces around operators
# - Inconsistent spacing
# - No blank line at end

# Fixed version:


def calculate_price(price, discount, tax):
    """Calculate final price with discount and tax."""
    if discount > 0:
        price = price - discount
    total = price + (price * tax)
    return total


result_price = calculate_price(100, 10, 0.08)
print(result_price)

# --------------------------------------------
# QUICK REFERENCE: PEP 8 RULES
# --------------------------------------------

"""
✅ DO:
- Use 4 spaces for indentation
- Name variables like: my_variable
- Name functions like: calculate_total()
- Add spaces around operators: x = y + z
- Keep lines under 79 characters
- Use blank lines between functions
- Write clear comments

❌ DON'T:
- Mix tabs and spaces
- Use names like: MyVariable or my-variable
- Cram code together: x=y+z
- Write super long lines
- Leave no space between functions
- Over-comment obvious things
"""

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Fix this code using PEP 8
# (Look for spacing, naming, and formatting issues)
"""
def CalculateArea(width,height):
  area=width*height
  return area
result=CalculateArea(5,10)
print(result)
"""

# Correct version:


def calculate_area(width, height):
    """Calculate area of a rectangle."""
    area = width * height
    return area


area_result = calculate_area(5, 10)
print(area_result)


# Exercise 2: Add appropriate comments
# Add comments to explain WHY this code works


def is_prime(n):
    """Check if a number is prime."""
    # Numbers less than 2 are not prime by definition
    if n < 2:
        return False
    # Check divisibility up to square root for efficiency
    # If n has a divisor, it must be <= sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Exercise 3: Improve variable names
# Make these variable names more descriptive

# ❌ BAD
# x = 100
# y = 0.08
# z = x + (x * y)

# ✅ GOOD
price = 100
tax_rate = 0.08
total_with_tax = price + (price * tax_rate)

# Exercise 4: Split long line
# This line is too long - split it properly

# ❌ BAD (shown in comment)
# long_message = "This is a very long message that exceeds 79 characters and needs to be split"

# ✅ GOOD
message_split = (
    "This is a very long message that exceeds 79 characters "
    "and needs to be split across multiple lines"
)

# Exercise 5: Install and use a linter
# 1. Install flake8: pip install flake8
# 2. Create a Python file with some messy code
# 3. Run: flake8 yourfile.py
# 4. Fix all the issues it finds
# 5. Run again to confirm your code is clean!

print("All exercises completed!")
