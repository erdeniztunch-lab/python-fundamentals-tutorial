"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 2: VARIABLES AND DATA TYPES
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ What are variables and how to use them
✓ Variable naming rules and conventions
✓ Data types in Python (int, float, string, boolean)
✓ Type conversion
✓ Truthy and Falsy values

Goal: Master variables and understand Python's data types
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. WHAT ARE VARIABLES?
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. INTRODUCTION TO VARIABLES")
print("=" * 70)

print("""
A variable is a named location in memory that stores a value.
Think of it as a labeled box that holds data.
""")

# Creating variables
students_count = 1000
school_name = "Central High School"
is_open = True
average_grade = 85.5

print("📌 Variable Examples:")
print(f"   students_count = {students_count}")
print(f"   school_name = '{school_name}'")
print(f"   is_open = {is_open}")
print(f"   average_grade = {average_grade}")

print("\n💡 Key Concepts:")
print("   • Variables store data in memory")
print("   • Variable names are case-sensitive")
print("   • Python is dynamically typed (no type declaration needed)")
print("   • You can reassign variables with different values")

# Variable reassignment
print("\n📌 Variable Reassignment:")
x = 10
print(f"   x = {x}")
x = 20
print(f"   x = {x} (reassigned)")
x = "Hello"
print(f"   x = '{x}' (reassigned to different type)")

# ═══════════════════════════════════════════════════════════════════════════
# 2. VARIABLE NAMING RULES AND CONVENTIONS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. VARIABLE NAMING RULES")
print("=" * 70)

print("\n✅ VALID Variable Names:")
# Valid names
name = "Alice"
age_2023 = 25
_private_var = "hidden"
camelCase = "works but not pythonic"
snake_case = "pythonic way"

print(f"   name = '{name}'")
print(f"   age_2023 = {age_2023}")
print(f"   _private_var = '{_private_var}'")
print(f"   snake_case = '{snake_case}' ← Recommended!")

print("\n❌ INVALID Variable Names (will cause errors):")
print("   2name = 'Bob'          # Cannot start with number")
print("   first-name = 'Alice'   # Cannot use hyphen")
print("   class = 'Python'       # Cannot use reserved keywords")
print("   first name = 'Bob'     # Cannot have spaces")

print("\n💡 Naming Conventions (PEP 8):")
print("   • Use snake_case for variables: my_variable")
print("   • Use UPPER_CASE for constants: MAX_SIZE = 100")
print("   • Use descriptive names: total_price (not tp)")
print("   • Avoid single letters (except in loops: i, j, k)")

# 🌍 REAL-WORLD EXAMPLE: Customer Database
print("\n🌍 Real-World Example: Customer Information System")
print("-" * 70)

# Good naming practice
customer_id = "C12345"
customer_first_name = "John"
customer_last_name = "Smith"
customer_email = "john.smith@email.com"
account_balance = 1250.50
is_premium_member = True
MINIMUM_BALANCE = 100  # Constant

print(f"Customer ID: {customer_id}")
print(f"Name: {customer_first_name} {customer_last_name}")
print(f"Email: {customer_email}")
print(f"Balance: ${account_balance}")
print(f"Premium Member: {is_premium_member}")
print(f"Minimum Required Balance: ${MINIMUM_BALANCE}")

# ═══════════════════════════════════════════════════════════════════════════
# 3. DATA TYPES IN PYTHON
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. PYTHON DATA TYPES")
print("=" * 70)

print("\n📌 Main Data Types:")

# 1. Integer (int) - Whole numbers
age = 25
year = 2024
temperature = -5

print(f"\n1. Integer (int) - Whole numbers")
print(f"   age = {age} → type: {type(age).__name__}")
print(f"   year = {year} → type: {type(year).__name__}")
print(f"   temperature = {temperature} → type: {type(temperature).__name__}")

# 2. Float - Decimal numbers
height = 1.75
price = 99.99
pi = 3.14159

print(f"\n2. Float - Decimal numbers")
print(f"   height = {height} → type: {type(height).__name__}")
print(f"   price = {price} → type: {type(price).__name__}")
print(f"   pi = {pi} → type: {type(pi).__name__}")

# 3. String (str) - Text
first_name = "Alice"
message = "Hello, World!"
address = '123 Main St'  # Single or double quotes work

print(f"\n3. String (str) - Text")
print(f"   first_name = '{first_name}' → type: {type(first_name).__name__}")
print(f"   message = '{message}' → type: {type(message).__name__}")

# 4. Boolean (bool) - True or False
is_student = True
has_license = False

print(f"\n4. Boolean (bool) - True or False")
print(f"   is_student = {is_student} → type: {type(is_student).__name__}")
print(f"   has_license = {has_license} → type: {type(has_license).__name__}")
print(f"   Note: Boolean values must be capitalized: True, False")

# 🌍 REAL-WORLD EXAMPLE: Product Inventory
print("\n🌍 Real-World Example: Product Inventory System")
print("-" * 70)

# Product details using different data types
product_id = 12345                    # int
product_name = "Wireless Mouse"       # str
product_price = 29.99                 # float
stock_quantity = 150                  # int
is_available = True                   # bool
discount_rate = 0.15                  # float
manufacturer = "TechCorp"             # str

print(f"Product ID: {product_id} ({type(product_id).__name__})")
print(f"Name: {product_name} ({type(product_name).__name__})")
print(f"Price: ${product_price} ({type(product_price).__name__})")
print(f"Stock: {stock_quantity} units ({type(stock_quantity).__name__})")
print(f"Available: {is_available} ({type(is_available).__name__})")
print(f"Discount: {discount_rate * 100}% ({type(discount_rate).__name__})")

# Calculate final price
final_price = product_price * (1 - discount_rate)
print(f"\nFinal Price after discount: ${final_price:.2f}")

# ═══════════════════════════════════════════════════════════════════════════
# 4. TYPE CONVERSION
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. TYPE CONVERSION (TYPE CASTING)")
print("=" * 70)

print("""
Type conversion is the process of converting one data type to another.
This is essential when working with user input or mixing data types.
""")

# String to Integer
print("📌 String to Integer:")
age_str = "25"
age_int = int(age_str)
print(f"   '{age_str}' (string) → {age_int} (integer)")

# String to Float
print("\n📌 String to Float:")
price_str = "99.99"
price_float = float(price_str)
print(f"   '{price_str}' (string) → {price_float} (float)")

# Number to String
print("\n📌 Number to String:")
count = 100
count_str = str(count)
print(f"   {count} (integer) → '{count_str}' (string)")

# Integer to Float
print("\n📌 Integer to Float:")
whole_number = 42
decimal_number = float(whole_number)
print(f"   {whole_number} (integer) → {decimal_number} (float)")

# Float to Integer (loses decimal part)
print("\n📌 Float to Integer (truncates decimal):")
price = 19.99
price_int = int(price)
print(f"   {price} (float) → {price_int} (integer)")
print(f"   Note: Decimal part is removed, not rounded!")

# 🌍 REAL-WORLD EXAMPLE: User Input Processing
print("\n🌍 Real-World Example: Age Calculator")
print("-" * 70)

print("Simulating user input...")
# In real program: birth_year = input("Enter your birth year: ")
birth_year = "1990"  # Simulated input (always string from input())

print(f"User entered: '{birth_year}' (type: {type(birth_year).__name__})")

# Convert to integer for calculation
birth_year_int = int(birth_year)
current_year = 2024
age = current_year - birth_year_int

print(
    f"Converted to: {birth_year_int} (type: {type(birth_year_int).__name__})")
print(f"Calculated age: {age} years old")

# ⚠️ Common errors
print("\n⚠️ Common Type Conversion Errors:")
print("   int('hello')      # ValueError: can't convert text to int")
print("   int('3.14')       # ValueError: use float() first")
print("   float('abc')      # ValueError: can't convert text to float")

# ═══════════════════════════════════════════════════════════════════════════
# 5. TRUTHY AND FALSY VALUES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. TRUTHY AND FALSY VALUES")
print("=" * 70)

print("""
In Python, every value has a boolean context (True or False).
Some values are considered "Falsy" (evaluate to False).
Everything else is "Truthy" (evaluates to True).
""")

print("\n📌 Falsy Values (evaluate to False):")
falsy_values = [
    (0, "Zero"),
    (0.0, "Zero float"),
    ("", "Empty string"),
    ([], "Empty list"),
    ({}, "Empty dictionary"),
    (None, "None type"),
    (False, "False boolean")
]

for value, description in falsy_values:
    print(f"   {str(value):15} → {bool(value)} ({description})")

print("\n📌 Truthy Values (evaluate to True):")
truthy_values = [
    (1, "Any non-zero number"),
    (-5, "Negative numbers"),
    ("Hello", "Non-empty string"),
    ([1, 2], "Non-empty list"),
    (True, "True boolean")
]

for value, description in truthy_values:
    print(f"   {str(value):15} → {bool(value)} ({description})")

# 🌍 REAL-WORLD EXAMPLE: Form Validation
print("\n🌍 Real-World Example: Form Validation")
print("-" * 70)


def validate_user_input(username, password, age):
    """Validates user registration form"""
    print(f"Validating user: '{username}'")

    # Check if username is provided (truthy)
    if not username:  # Empty string is falsy
        print("   ❌ Username is required!")
        return False

    # Check if password is provided
    if not password:
        print("   ❌ Password is required!")
        return False

    # Check if age is valid
    if not age or age <= 0:  # 0 or None are falsy
        print("   ❌ Valid age is required!")
        return False

    print("   ✅ All fields valid!")
    return True


# Test cases
print("\nTest Case 1:")
validate_user_input("john_doe", "pass123", 25)

print("\nTest Case 2:")
validate_user_input("", "pass123", 25)

print("\nTest Case 3:")
validate_user_input("jane_doe", "", 30)

print("\nTest Case 4:")
validate_user_input("alice", "secure", 0)

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: Variable Creation
-----------------------------
Create variables for a person with the following information:
- First name: "Sarah"
- Last name: "Connor"
- Age: 28
- Height: 1.68 (meters)
- Is employed: True
- Salary: 55000.50

Print all variables with their types.

Exercise 2: Variable Naming
---------------------------
Which of these variable names are VALID? Mark each as ✅ or ❌
a) user_name
b) 2nd_place
c) total-price
d) _private
e) for
f) userName
g) MAX_SIZE

Exercise 3: Type Conversion Challenge
-------------------------------------
You have these string values from user input:
age = "25"
height = "1.75"
name = "Alex"

Convert them to appropriate types and calculate:
- Age in months (age * 12)
- Height in centimeters (height * 100)
- Display: "Alex is 25 years old and 175 cm tall"

Exercise 4: Truthy/Falsy Quiz
-----------------------------
Predict the output (True or False):
a) bool(0)
b) bool(100)
c) bool("")
d) bool("False")
e) bool([])
f) bool([0])

Exercise 5: Real-World Application
----------------------------------
Create a simple shopping cart system:
1. Define variables for 3 products (name, price, quantity)
2. Calculate total for each product
3. Calculate grand total
4. Apply a 10% discount if grand total > $100
5. Display final receipt

Example output:
Product 1: Laptop - $999.99 x 1 = $999.99
Product 2: Mouse - $29.99 x 2 = $59.98
Product 3: Keyboard - $79.99 x 1 = $79.99
----------------------------------------
Subtotal: $1139.96
Discount (10%): -$113.99
Final Total: $1025.97

Bonus Exercise: Temperature Stats
---------------------------------
Given temperatures for a week: [72, 75, 68, 70, 73, 71, 69]
(Simulating user input - assume these were entered as strings)

Convert each to integers, then calculate and display:
- Minimum temperature
- Maximum temperature
- Average temperature
- How many days above 70°F
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 2")
print("=" * 70)
print("\nNext Module: Working with Strings")
print("Keep practicing and happy coding! 🚀")
