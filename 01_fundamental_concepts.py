"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 1: FUNDAMENTAL CONCEPTS
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ Difference between Expression and Statement
✓ Built-in vs User-defined functions
✓ Linting and code quality
✓ How Python works

Goal: Understand the fundamental building blocks of Python
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. EXPRESSION vs STATEMENT
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. EXPRESSION AND STATEMENT CONCEPTS")
print("=" * 70)

# Expression: A piece of code that produces a value
# --------------------------------------------
# Expressions always return a result

print("\n📌 What is an Expression?")
print("   An expression is code that produces/evaluates to a value\n")

# Mathematical expressions
result1 = 2 + 3              # Produces value: 5
result2 = "Py" + "thon"      # Produces value: "Python"
result3 = len("Hello")       # Produces value: 5
result4 = 10 > 5             # Produces value: True

print("   Expression Examples:")
print(f"   • 2 + 3 = {result1}")
print(f"   • 'Py' + 'thon' = {result2}")
print(f"   • len('Hello') = {result3}")
print(f"   • 10 > 5 = {result4}")

# Statement: A command that performs an action
# --------------------------------------------
# Statements don't necessarily return a value

print("\n📌 What is a Statement?")
print("   A statement is code that performs an action\n")

print("   Statement Examples:")

# Assignment statement
x = 10
print(f"   • x = 10 (performs assignment)")

# Print statement
print(f"   • print(x) (performs output)")


# Function definition statement
def hello():
    """A simple greeting function"""
    print("   • def hello(): (defines a function)")


hello()

# 🎯 KEY CONCEPT: Expression vs Statement
print("\n💡 Key Difference:")
print("   Expression  → Produces a VALUE (e.g., 2 + 3 → 5)")
print("   Statement   → Performs an ACTION (e.g., x = 10)")
print("   Combined    → print(2 + 3)  ← statement using expression")

# ✨ REAL-WORLD EXAMPLE: E-commerce Shopping Cart
print("\n🌍 Real-World Example: Shopping Cart Calculator")
print("-" * 70)

# Expressions (produce values)
product_price = 100
quantity = 3
subtotal = product_price * quantity      # Expression: produces 300
tax_rate = 0.18
tax = subtotal * tax_rate                # Expression: produces 54
total = subtotal + tax                   # Expression: produces 354

# Statements (perform actions)
print(f"Product Price: ${product_price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal}")
print(f"Tax ({int(tax_rate * 100)}%): ${tax}")
print(f"Total: ${total}")

# ═══════════════════════════════════════════════════════════════════════════
# 2. BUILT-IN FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. BUILT-IN FUNCTIONS")
print("=" * 70)

print("""
Built-in functions are pre-defined functions that come with Python.
They are always available without needing to import anything.
""")

# Common built-in functions
print("📌 Common Built-in Functions:\n")

# print() - Output to screen
print("1. print() → Displays output to screen")
print("   Example: print('Hello World!')")

# len() - Get length
word = "Python"
print(f"\n2. len() → Returns length/size")
print(f"   Example: len('{word}') = {len(word)}")

# type() - Get data type
print(f"\n3. type() → Returns the data type")
print(f"   Example: type(42) = {type(42).__name__}")
print(f"   Example: type('Hello') = {type('Hello').__name__}")

# input() - Get user input
print(f"\n4. input() → Gets input from user")
print(f"   Example: name = input('Your name: ')")

# int(), float(), str() - Type conversion
print(f"\n5. Type conversion functions:")
print(f"   int('42') = {int('42')}")
print(f"   float('3.14') = {float('3.14')}")
print(f"   str(100) = '{str(100)}'")

# min(), max(), sum() - Mathematical operations
numbers = [10, 25, 5, 30, 15]
print(f"\n6. Mathematical functions:")
print(f"   Numbers: {numbers}")
print(f"   min() = {min(numbers)}")
print(f"   max() = {max(numbers)}")
print(f"   sum() = {sum(numbers)}")

# abs(), round(), pow() - More math functions
print(f"\n7. Additional math functions:")
print(f"   abs(-42) = {abs(-42)}  (absolute value)")
print(f"   round(3.14159, 2) = {round(3.14159, 2)}  (round to 2 decimals)")
print(f"   pow(2, 3) = {pow(2, 3)}  (2 to the power of 3)")

# 🌍 REAL-WORLD EXAMPLE: Student Grading System
print("\n🌍 Real-World Example: Student Grading System")
print("-" * 70)

student_name = "Alice Johnson"
grades = [85, 92, 78, 95, 88]

print(f"Student: {student_name}")
print(f"Grades: {grades}")
print(f"Number of Grades: {len(grades)}")
print(f"Lowest Grade: {min(grades)}")
print(f"Highest Grade: {max(grades)}")
print(f"Total Points: {sum(grades)}")
print(f"Average: {sum(grades) / len(grades):.2f}")

# Determine letter grade
average = sum(grades) / len(grades)
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
else:
    letter_grade = 'F'

print(f"Letter Grade: {letter_grade}")

# ═══════════════════════════════════════════════════════════════════════════
# 3. USER-DEFINED FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. USER-DEFINED FUNCTIONS")
print("=" * 70)

print("""
User-defined functions are custom functions created by programmers
to meet specific needs. They are defined using the 'def' keyword.
""")


# Simple function
def greet():
    """A simple greeting function"""
    print("Hello! Welcome!")


print("📌 Simple Function Example:")
greet()


# Function with parameter
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello {name}! Welcome!")


print("\n📌 Function with Parameter Example:")
greet_person("Alice")
greet_person("Bob")


# Function that returns a value
def square(number):
    """Calculates the square of a number"""
    return number ** 2


print("\n📌 Function with Return Value Example:")
result = square(5)
print(f"Square of 5: {result}")


# Function with multiple parameters
def calculate_area(length, width):
    """Calculates area of a rectangle"""
    return length * width


print("\n📌 Function with Multiple Parameters:")
area = calculate_area(10, 5)
print(f"Area of 10x5 rectangle: {area}")

# 🌍 REAL-WORLD EXAMPLE: Salary Calculator
print("\n🌍 Real-World Example: Salary Calculator System")
print("-" * 70)


def calculate_net_salary(gross_salary, overtime_hours=0):
    """
    Calculates net salary based on gross salary and overtime hours

    Args:
        gross_salary: Employee's gross salary
        overtime_hours: Number of overtime hours worked (default: 0)

    Returns:
        Net salary amount
    """
    # Constants
    SOCIAL_SECURITY_RATE = 0.14
    INCOME_TAX_RATE = 0.15
    OVERTIME_RATE = 25  # $ per hour

    # Calculate overtime pay
    overtime_pay = overtime_hours * OVERTIME_RATE

    # Calculate total gross
    total_gross = gross_salary + overtime_pay

    # Calculate deductions
    social_security = total_gross * SOCIAL_SECURITY_RATE
    income_tax = total_gross * INCOME_TAX_RATE
    total_deductions = social_security + income_tax

    # Calculate net salary
    net_salary = total_gross - total_deductions

    # Display breakdown
    print(f"Gross Salary: ${gross_salary:,.2f}")
    print(f"Overtime Pay ({overtime_hours}h): ${overtime_pay:,.2f}")
    print(f"Total Gross: ${total_gross:,.2f}")
    print(f"Social Security (14%): -${social_security:,.2f}")
    print(f"Income Tax (15%): -${income_tax:,.2f}")
    print(f"Net Salary: ${net_salary:,.2f}")

    return net_salary


# Test the function
print("Employee 1 (no overtime):")
calculate_net_salary(5000)

print("\nEmployee 2 (with 10 hours overtime):")
calculate_net_salary(5000, 10)

# ═══════════════════════════════════════════════════════════════════════════
# 4. LINTING AND CODE QUALITY
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. LINTING AND CODE QUALITY")
print("=" * 70)

print("""
Linting is the process of checking your code for:
• Syntax errors
• Style violations (PEP 8)
• Potential bugs
• Code smells

Popular Python linters:
• pylint
• flake8
• black (auto-formatter)
""")

print("\n📌 PEP 8 Style Guidelines Examples:\n")

# ❌ BAD: Poor style
print("❌ BAD STYLE:")
print("def add(a,b):return a+b")


# ✅ GOOD: Follows PEP 8
print("\n✅ GOOD STYLE:")


def add(a, b):
    """Adds two numbers together"""
    return a + b


print("def add(a, b):")
print("    return a + b")

print("\n💡 Key PEP 8 Rules:")
print("   • Use 4 spaces for indentation (not tabs)")
print("   • Add spaces around operators (a + b, not a+b)")
print("   • Use meaningful variable names")
print("   • Add docstrings to functions")
print("   • Keep lines under 79 characters")
print("   • Use snake_case for variables and functions")
print("   • Use UPPER_CASE for constants")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: Expression vs Statement
-----------------------------------
Identify which of the following are expressions and which are statements:
a) x = 5
b) 3 + 7
c) print("Hello")
d) len("Python")
e) y = len("Hello")

Exercise 2: Built-in Functions
------------------------------
Use built-in functions to solve:
a) Find the maximum of [45, 23, 67, 12, 89, 34]
b) Calculate the sum of [10, 20, 30, 40, 50]
c) Get the length of "Programming"
d) Convert "123" to an integer
e) Round 3.14159 to 2 decimal places

Exercise 3: Create Your Own Function
-----------------------------------
Create a function called calculate_bmi that:
- Takes two parameters: weight (in kg) and height (in meters)
- Calculates BMI = weight / (height ** 2)
- Returns the BMI value
- Test it with: weight=70, height=1.75

Exercise 4: Real-World Function
-------------------------------
Create a function called calculate_discount that:
- Takes price and discount_percentage as parameters
- Calculates the final price after discount
- Returns both the discount amount and final price
- Test with: price=100, discount=20

Bonus Exercise: Temperature Converter
-------------------------------------
Create a function that converts Celsius to Fahrenheit
Formula: F = (C * 9/5) + 32
Test with: 0°C, 25°C, 100°C
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 1")
print("=" * 70)
print("\nNext Module: Variables and Data Types")
print("Keep practicing and happy coding! 🚀")
