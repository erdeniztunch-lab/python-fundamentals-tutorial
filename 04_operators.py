"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 4: OPERATORS
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ Arithmetic operators
✓ Augmented assignment operators
✓ Comparison operators
✓ Logical operators
✓ Operator precedence

Goal: Master all types of operators in Python
"""

import math

# ═══════════════════════════════════════════════════════════════════════════
# 1. ARITHMETIC OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. ARITHMETIC OPERATORS")
print("=" * 70)

print("""
Arithmetic operators perform mathematical operations on numbers.
""")

print("📌 Basic Arithmetic Operators:\n")

# Addition
print("1. Addition (+)")
print(f"   10 + 3 = {10 + 3}")

# Subtraction
print("\n2. Subtraction (-)")
print(f"   10 - 3 = {10 - 3}")

# Multiplication
print("\n3. Multiplication (*)")
print(f"   10 * 3 = {10 * 3}")

# Division (always returns float)
print("\n4. Division (/)")
print(f"   10 / 3 = {10 / 3}")
print(f"   Note: Always returns a float")

# Floor Division (returns integer)
print("\n5. Floor Division (//)")
print(f"   10 // 3 = {10 // 3}")
print(f"   Note: Returns the quotient without remainder")

# Modulus (remainder)
print("\n6. Modulus (%)")
print(f"   10 % 3 = {10 % 3}")
print(f"   Note: Returns the remainder after division")

# Exponentiation (power)
print("\n7. Exponentiation (**)")
print(f"   2 ** 3 = {2 ** 3}")
print(f"   10 ** 2 = {10 ** 2}")

# 🌍 REAL-WORLD EXAMPLE: Shopping Calculator
print("\n🌍 Real-World Example: Shopping Bill Calculator")
print("-" * 70)

item_price = 29.99
quantity = 3
tax_rate = 0.08

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Item Price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Check if we can split the bill evenly
people = 4
per_person = total / people
print(f"\nSplit between {people} people: ${per_person:.2f} each")

# 🌍 REAL-WORLD EXAMPLE: Even/Odd Checker
print("\n🌍 Real-World Example: Even/Odd Number Checker")
print("-" * 70)

numbers = [10, 15, 22, 37, 44, 51]
print("Checking numbers:", numbers)
print()

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is EVEN (remainder when divided by 2: {num % 2})")
    else:
        print(f"{num} is ODD (remainder when divided by 2: {num % 2})")

# ═══════════════════════════════════════════════════════════════════════════
# 2. BUILT-IN MATH FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. BUILT-IN MATH FUNCTIONS")
print("=" * 70)

print("\n📌 Common Math Functions:\n")

# round() - Round to nearest integer
print("1. round() - Rounds to nearest integer")
print(f"   round(3.14159) = {round(3.14159)}")
print(f"   round(3.14159, 2) = {round(3.14159, 2)}  (2 decimal places)")
print(f"   round(2.5) = {round(2.5)}  (rounds to nearest even)")
print(f"   round(3.5) = {round(3.5)}")

# abs() - Absolute value
print("\n2. abs() - Returns absolute value")
print(f"   abs(-10) = {abs(-10)}")
print(f"   abs(10) = {abs(10)}")
print(f"   abs(-3.14) = {abs(-3.14)}")

# pow() - Power
print("\n3. pow() - Raises to power")
print(f"   pow(2, 3) = {pow(2, 3)}  (2^3)")
print(f"   pow(5, 2) = {pow(5, 2)}  (5^2)")

# min() and max()
print("\n4. min() and max() - Find minimum and maximum")
numbers = [15, 42, 7, 23, 91, 4]
print(f"   Numbers: {numbers}")
print(f"   min(numbers) = {min(numbers)}")
print(f"   max(numbers) = {max(numbers)}")

# sum()
print("\n5. sum() - Calculates sum")
print(f"   sum([1, 2, 3, 4, 5]) = {sum([1, 2, 3, 4, 5])}")

# 🌍 REAL-WORLD EXAMPLE: Temperature Analysis
print("\n🌍 Real-World Example: Weekly Temperature Analysis")
print("-" * 70)

temperatures = [72.3, 68.9, 75.1, 71.4, 69.8, 73.2, 70.5]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Weekly Temperature Report:")
print("-" * 40)
for day, temp in zip(days, temperatures):
    print(f"{day}: {temp}°F")

print("-" * 40)
min_temp = min(temperatures)
max_temp = max(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

print(f"Minimum Temperature: {min_temp}°F")
print(f"Maximum Temperature: {max_temp}°F")
print(f"Average Temperature: {round(avg_temp, 1)}°F")
print(f"Temperature Range: {round(max_temp - min_temp, 1)}°F")

# ═══════════════════════════════════════════════════════════════════════════
# 3. MATH MODULE
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. MATH MODULE")
print("=" * 70)

print("""
The math module provides additional mathematical functions.
Import it with: import math
""")

print("\n📌 Math Module Functions:\n")

# ceil() and floor()
print("1. ceil() and floor() - Rounding functions")
print(f"   math.ceil(3.2) = {math.ceil(3.2)}  (round up)")
print(f"   math.floor(3.8) = {math.floor(3.8)}  (round down)")

# sqrt() - Square root
print("\n2. sqrt() - Square root")
print(f"   math.sqrt(16) = {math.sqrt(16)}")
print(f"   math.sqrt(25) = {math.sqrt(25)}")

# Constants
print("\n3. Mathematical Constants")
print(f"   math.pi = {math.pi}")
print(f"   math.e = {math.e}")

# Trigonometric functions
print("\n4. Trigonometric Functions")
print(f"   math.sin(math.pi/2) = {math.sin(math.pi/2):.2f}")
print(f"   math.cos(0) = {math.cos(0):.2f}")

# ═══════════════════════════════════════════════════════════════════════════
# 4. AUGMENTED ASSIGNMENT OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. AUGMENTED ASSIGNMENT OPERATORS")
print("=" * 70)

print("""
Augmented assignment operators provide a shorthand way to update variables.
They combine an arithmetic operation with assignment.
""")

print("\n📌 Augmented Assignment Operators:\n")

# +=
x = 10
print(f"Starting value: x = {x}")
x += 5  # Same as: x = x + 5
print(f"After x += 5: x = {x}")

# -=
x -= 3  # Same as: x = x - 3
print(f"After x -= 3: x = {x}")

# *=
x *= 2  # Same as: x = x * 2
print(f"After x *= 2: x = {x}")

# /=
x /= 4  # Same as: x = x / 4
print(f"After x /= 4: x = {x}")

# //=
x = 25
x //= 4  # Same as: x = x // 4
print(f"\nStarting with 25, after x //= 4: x = {x}")

# %=
x = 17
x %= 5  # Same as: x = x % 5
print(f"Starting with 17, after x %= 5: x = {x}")

# **=
x = 2
x **= 3  # Same as: x = x ** 3
print(f"Starting with 2, after x **= 3: x = {x}")

# 🌍 REAL-WORLD EXAMPLE: Bank Account
print("\n🌍 Real-World Example: Bank Account Transactions")
print("-" * 70)

balance = 1000.00
print(f"Initial Balance: ${balance:.2f}")

# Deposit
deposit = 500.00
balance += deposit
print(f"After deposit of ${deposit:.2f}: ${balance:.2f}")

# Withdrawal
withdrawal = 200.00
balance -= withdrawal
print(f"After withdrawal of ${withdrawal:.2f}: ${balance:.2f}")

# Interest (3% monthly)
interest_rate = 0.03
balance *= (1 + interest_rate)
print(f"After {interest_rate*100}% interest: ${balance:.2f}")

# Fee
fee = 10.00
balance -= fee
print(f"After ${fee:.2f} fee: ${balance:.2f}")

# ═══════════════════════════════════════════════════════════════════════════
# 5. COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. COMPARISON OPERATORS")
print("=" * 70)

print("""
Comparison operators compare two values and return a boolean (True/False).
""")

print("\n📌 Comparison Operators:\n")

a = 10
b = 5

print(f"a = {a}, b = {b}\n")

# Greater than
print(f"1. Greater than (>)")
print(f"   a > b: {a > b}")

# Less than
print(f"\n2. Less than (<)")
print(f"   a < b: {a < b}")

# Greater than or equal
print(f"\n3. Greater than or equal (>=)")
print(f"   a >= 10: {a >= 10}")

# Less than or equal
print(f"\n4. Less than or equal (<=)")
print(f"   b <= 5: {b <= 5}")

# Equal to
print(f"\n5. Equal to (==)")
print(f"   a == b: {a == b}")
print(f"   a == 10: {a == 10}")

# Not equal to
print(f"\n6. Not equal to (!=)")
print(f"   a != b: {a != b}")

# String comparison
print("\n📌 String Comparison (Alphabetical/ASCII):")
print(f"   'apple' > 'banana': {'apple' > 'banana'}")
print(f"   'apple' < 'banana': {'apple' < 'banana'}")
print(f"   ord('a') = {ord('a')} (ASCII value)")
print(f"   ord('b') = {ord('b')} (ASCII value)")

# 🌍 REAL-WORLD EXAMPLE: Age Verification
print("\n🌍 Real-World Example: Age Verification System")
print("-" * 70)


def verify_age(age, name):
    """Verify if person meets age requirements"""
    MINIMUM_AGE = 18
    SENIOR_AGE = 65

    print(f"\nChecking {name}, age {age}:")

    if age < MINIMUM_AGE:
        print(f"   ❌ Too young. Must be {MINIMUM_AGE} or older.")
        return "Minor"
    elif age >= SENIOR_AGE:
        print(f"   ✅ Approved. Senior citizen (65+)")
        return "Senior"
    else:
        print(f"   ✅ Approved. Adult")
        return "Adult"


verify_age(16, "John")
verify_age(25, "Alice")
verify_age(70, "Bob")

# ═══════════════════════════════════════════════════════════════════════════
# 6. LOGICAL OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("6. LOGICAL OPERATORS")
print("=" * 70)

print("""
Logical operators combine multiple boolean expressions.
""")

print("\n📌 Logical Operators:\n")

# AND operator
print("1. AND operator - Returns True if BOTH conditions are True")
print(f"   True and True = {True and True}")
print(f"   True and False = {True and False}")
print(f"   False and False = {False and False}")

# OR operator
print("\n2. OR operator - Returns True if AT LEAST ONE condition is True")
print(f"   True or False = {True or False}")
print(f"   False or False = {False or False}")
print(f"   True or True = {True or True}")

# NOT operator
print("\n3. NOT operator - Reverses the boolean value")
print(f"   not True = {not True}")
print(f"   not False = {not False}")

# Combining operators
print("\n📌 Combining Logical Operators:")
age = 25
has_license = True
has_insurance = True

print(
    f"age = {age}, has_license = {has_license}, has_insurance = {has_insurance}")
print(f"Can drive = age >= 18 and has_license and has_insurance")
print(f"Result: {age >= 18 and has_license and has_insurance}")

# 🌍 REAL-WORLD EXAMPLE: Loan Approval System
print("\n🌍 Real-World Example: Loan Approval System")
print("-" * 70)


def check_loan_eligibility(income, credit_score, employment_years, is_student):
    """
    Check if applicant is eligible for a loan

    Requirements:
    - Income >= $30,000
    - Credit score >= 650
    - Employment >= 2 years OR not a student
    """
    MINIMUM_INCOME = 30000
    MINIMUM_CREDIT = 650
    MINIMUM_EMPLOYMENT = 2

    print(f"\nLoan Application Review:")
    print(f"  Income: ${income:,}")
    print(f"  Credit Score: {credit_score}")
    print(f"  Employment Years: {employment_years}")
    print(f"  Student: {is_student}")
    print()

    # Check individual criteria
    income_ok = income >= MINIMUM_INCOME
    credit_ok = credit_score >= MINIMUM_CREDIT
    employment_ok = employment_years >= MINIMUM_EMPLOYMENT or not is_student

    print(f"  Income requirement: {'✅' if income_ok else '❌'}")
    print(f"  Credit requirement: {'✅' if credit_ok else '❌'}")
    print(f"  Employment requirement: {'✅' if employment_ok else '❌'}")

    # Final decision
    approved = income_ok and credit_ok and employment_ok

    if approved:
        print(f"\n  🎉 LOAN APPROVED!")
    else:
        print(f"\n  ❌ LOAN DENIED")

    return approved


# Test cases
check_loan_eligibility(45000, 720, 3, False)
check_loan_eligibility(25000, 680, 1, True)
check_loan_eligibility(50000, 600, 5, False)

# ═══════════════════════════════════════════════════════════════════════════
# 7. SHORT-CIRCUIT EVALUATION
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("7. SHORT-CIRCUIT EVALUATION")
print("=" * 70)

print("""
Python uses short-circuit evaluation for logical operators:
- With AND: If first condition is False, second isn't checked
- With OR: If first condition is True, second isn't checked
""")

print("\n📌 Short-Circuit with AND:\n")

high_income = False
good_credit = True
student = False

print(f"high_income = {high_income}")
print(f"good_credit = {good_credit}")
print(f"student = {student}")
print()

# If high_income is False, the rest won't be evaluated
if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")
    print("(good_credit and 'not student' weren't even checked)")

print("\n📌 Short-Circuit with OR:\n")

has_admin_rights = True
has_manager_rights = False

print(f"has_admin_rights = {has_admin_rights}")
print(f"has_manager_rights = {has_manager_rights}")
print()

# If has_admin_rights is True, has_manager_rights won't be checked
if has_admin_rights or has_manager_rights:
    print("Access Granted")
    print("(has_manager_rights wasn't even checked)")

# ═══════════════════════════════════════════════════════════════════════════
# 8. CHAINING COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("8. CHAINING COMPARISON OPERATORS")
print("=" * 70)

print("""
Python allows you to chain comparison operators for cleaner code.
""")

age = 25

print(f"age = {age}\n")

print("📌 Traditional Way:")
print(f"   age >= 18 and age < 65")
print(f"   Result: {age >= 18 and age < 65}")

print("\n📌 Chained Way (Pythonic):")
print(f"   18 <= age < 65")
print(f"   Result: {18 <= age < 65}")

# More examples
x = 15
print(f"\nx = {x}")
print(f"10 < x < 20: {10 < x < 20}")
print(f"10 <= x <= 15: {10 <= x <= 15}")
print(f"x < 10 or x > 20: {x < 10 or x > 20}")

# 🌍 REAL-WORLD EXAMPLE: Grade Classification
print("\n🌍 Real-World Example: Grade Classification System")
print("-" * 70)


def classify_grade(score):
    """Classify student grade based on score"""
    print(f"\nScore: {score}")

    if 90 <= score <= 100:
        grade = 'A'
        comment = "Excellent!"
    elif 80 <= score < 90:
        grade = 'B'
        comment = "Good job!"
    elif 70 <= score < 80:
        grade = 'C'
        comment = "Satisfactory"
    elif 60 <= score < 70:
        grade = 'D'
        comment = "Needs improvement"
    elif 0 <= score < 60:
        grade = 'F'
        comment = "Failed"
    else:
        grade = 'Invalid'
        comment = "Score must be between 0-100"

    print(f"Grade: {grade}")
    print(f"Comment: {comment}")
    return grade


# Test cases
classify_grade(95)
classify_grade(82)
classify_grade(55)
classify_grade(110)

# ═══════════════════════════════════════════════════════════════════════════
# 9. OPERATOR PRECEDENCE
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("9. OPERATOR PRECEDENCE")
print("=" * 70)

print("""
Operator precedence determines the order of operations.
From highest to lowest:
1. ** (Exponentiation)
2. *, /, //, % (Multiplication, Division, Floor Division, Modulus)
3. +, - (Addition, Subtraction)
4. <, <=, >, >=, ==, != (Comparison)
5. not (Logical NOT)
6. and (Logical AND)
7. or (Logical OR)
""")

print("\n📌 Examples:")

result = 10 + 2 * 3
print(f"10 + 2 * 3 = {result}  (multiplication first)")

result = (10 + 2) * 3
print(f"(10 + 2) * 3 = {result}  (parentheses first)")

result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}  (right to left for **)")

result = 20 / 4 * 2
print(f"20 / 4 * 2 = {result}  (left to right for same precedence)")

# Complex expression
print("\n📌 Complex Expression:")
x = 5
y = 10
z = 3

result = x + y * z - 2 ** 2
print(f"x={x}, y={y}, z={z}")
print(f"x + y * z - 2 ** 2")
print(f"= 5 + 10 * 3 - 4")
print(f"= 5 + 30 - 4")
print(f"= {result}")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: Basic Arithmetic
----------------------------
Calculate the following:
a) 15 + 27
b) 100 - 42
c) 8 * 7
d) 45 / 6
e) 45 // 6
f) 45 % 6
g) 3 ** 4

Exercise 2: Augmented Assignment
--------------------------------
Starting with x = 50, perform these operations in order:
a) Add 10
b) Multiply by 2
c) Subtract 20
d) Divide by 4
What is the final value?

Exercise 3: Temperature Converter
---------------------------------
Create a function that converts Celsius to Fahrenheit.
Formula: F = (C * 9/5) + 32
Test with: 0°C, 25°C, 100°C

Exercise 4: Even or Odd
-----------------------
Write a function that takes a number and returns:
- "Even" if the number is divisible by 2
- "Odd" otherwise
Test with: 10, 15, 22, 37

Exercise 5: Comparison Challenge
--------------------------------
Given: a = 15, b = 25, c = 15
Evaluate:
a) a == c
b) a != b
c) a < b
d) b >= 25
e) a <= c

Exercise 6: Logical Operators
-----------------------------
Create a function to check if someone can vote:
- Must be >= 18 years old
- Must be a citizen
- Must be registered

Test cases:
- Age: 20, Citizen: True, Registered: True
- Age: 16, Citizen: True, Registered: True
- Age: 25, Citizen: False, Registered: True

Exercise 7: BMI Calculator
--------------------------
Create a BMI calculator that:
- Takes weight (kg) and height (m)
- Calculates BMI = weight / (height ** 2)
- Classifies result:
  - BMI < 18.5: Underweight
  - 18.5 <= BMI < 25: Normal
  - 25 <= BMI < 30: Overweight
  - BMI >= 30: Obese

Exercise 8: Discount Calculator
-------------------------------
Create a function that calculates final price:
- If purchase >= $100: 10% discount
- If purchase >= $200: 15% discount
- If purchase >= $300: 20% discount

Test with: $50, $150, $250, $350

Exercise 9: Triangle Validator
------------------------------
Create a function that checks if three sides can form a triangle.
Rule: Sum of any two sides must be greater than the third side.
Test with: (3, 4, 5), (1, 2, 10), (5, 5, 5)

Bonus Exercise: Leap Year Checker
---------------------------------
A year is a leap year if:
- Divisible by 4 AND
- (Not divisible by 100 OR divisible by 400)

Test with: 2000, 1900, 2024, 2023
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 4")
print("=" * 70)
print("\nNext Module: Conditional Statements")
print("Keep practicing and happy coding! 🚀")
