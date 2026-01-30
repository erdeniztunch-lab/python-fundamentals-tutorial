# ============================================
# NUMBERS AND ARITHMETIC
# ============================================

# --------------------------------------------
# ARITHMETIC OPERATORS
# --------------------------------------------

# Arithmetic operators let you do math with numbers

# Addition (+)
print(3 + 5)      # 8
print(10 + 20)    # 30

# Subtraction (-)
print(10 - 2)     # 8
print(50 - 15)    # 35

# Multiplication (*)
print(4 * 2)      # 8
print(5 * 10)     # 50

# Division (/)
print(16 / 4)     # 4.0 (always gives a decimal)
print(10 / 3)     # 3.3333...

# Floor Division (//) - divides and removes the decimal part
print(16 // 4)    # 4 (whole number)
print(10 // 3)    # 3 (removes the .333...)

# Modulus (%) - gives the remainder
print(16 % 4)     # 0 (16 divided by 4 has no remainder)
print(10 % 3)     # 1 (10 divided by 3 has remainder 1)
print(17 % 5)     # 2 (17 divided by 5 has remainder 2)

# Power (**) - raises to a power
print(2 ** 3)     # 8 (2 × 2 × 2)
print(5 ** 2)     # 25 (5 × 5)
print(10 ** 3)    # 1000 (10 × 10 × 10)

# --------------------------------------------
# ORDER OF OPERATIONS
# --------------------------------------------

# Python follows math rules (PEMDAS):
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print(2 + 3 * 4)      # 14 (multiply first: 3*4=12, then 2+12=14)
print((2 + 3) * 4)    # 20 (parentheses first: 2+3=5, then 5*4=20)
print(10 + 5 / 2)     # 12.5 (divide first: 5/2=2.5, then 10+2.5=12.5)

# --------------------------------------------
# AUGMENTED ASSIGNMENT
# --------------------------------------------

# Shortcut for updating a variable with an operation

# Long way:
x = 10
x = x + 5    # Add 5 to x
print(x)     # 15

# Short way (augmented assignment):
x = 10
x += 5       # Same as: x = x + 5
print(x)     # 15

# Works with all operators:
x = 10
x += 3       # x = x + 3 → 13
x -= 2       # x = x - 2 → 11
x *= 4       # x = x * 4 → 44
x /= 2       # x = x / 2 → 22.0
print(x)     # 22.0

# Real-world example:
balance = 100
print(f"Starting balance: ${balance}")
balance += 50    # Deposit money
print(f"After deposit: ${balance}")
balance -= 30    # Withdraw money
print(f"After withdrawal: ${balance}")

# --------------------------------------------
# BUILT-IN MATH FUNCTIONS
# --------------------------------------------

# round() - rounds a decimal number
print(round(3.7))       # 4
print(round(3.14159))   # 3
print(round(3.14159, 2))  # 3.14 (2 decimal places)

# abs() - gives the absolute value (removes negative sign)
print(abs(-10))    # 10
print(abs(10))     # 10
print(abs(-5.5))   # 5.5

# pow() - raises to a power (like **)
print(pow(2, 3))   # 8 (2³)
print(pow(5, 2))   # 25 (5²)

# max() - finds the largest number
print(max(5, 2, 9, 1))      # 9
print(max(10, 25, 15))      # 25

# min() - finds the smallest number
print(min(5, 2, 9, 1))      # 1
print(min(10, 25, 15))      # 10

# --------------------------------------------
# TYPE CONVERSION
# --------------------------------------------

# Converting between number types and strings

# String to integer:
age_text = "25"
age_number = int(age_text)
print(age_number + 5)  # 30

# String to float:
price_text = "19.99"
price_number = float(price_text)
print(price_number * 2)  # 39.98

# Number to string:
score = 100
score_text = str(score)
message = "Your score is: " + score_text
print(message)  # Your score is: 100

# Why do we need type conversion?
# You can't do math with strings:
# "5" + "3" = "53" (joins them as text)
# 5 + 3 = 8 (adds them as numbers)

# Getting input from users (input is always a string):
# This is how you would get input in a real program:
# age_input = input("Enter your age: ")  # Returns a string
# age = int(age_input)  # Convert to number
# next_year = age + 1
# print(f"Next year you'll be {next_year}")

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Calculate restaurant bill
meal_cost = 45.00
tip_percentage = 0.20
tip_amount = meal_cost * tip_percentage
total = meal_cost + tip_amount
print(f"Meal: ${meal_cost}")
print(f"Tip (20%): ${tip_amount}")
print(f"Total: ${total}")

# Example 2: Convert temperature
fahrenheit = 72
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {round(celsius, 1)}°C")

# Example 3: Calculate shopping discount
original_price = 100
discount_percent = 25
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount
print(f"Original: ${original_price}")
print(f"Discount: ${discount_amount}")
print(f"You pay: ${final_price}")

# Example 4: Check if number is even
number = 17
remainder = number % 2
if remainder == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example 5: Calculate loan payment
loan_amount = 10000
interest_rate = 0.05  # 5%
years = 3
monthly_rate = interest_rate / 12
months = years * 12
monthly_payment = loan_amount / months
interest_per_month = loan_amount * monthly_rate
total_monthly = monthly_payment + interest_per_month
print(f"Monthly payment: ${round(total_monthly, 2)}")

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Basic arithmetic
# Calculate and display:
# - 25 + 17
# - 100 - 43
# - 8 * 9
# - 50 / 7
# - 23 % 4


# Exercise 2: Augmented assignment
# Create a variable called "points" with value 0.
# Add 10 to it.
# Multiply it by 2.
# Subtract 5 from it.
# Display the final value.


# Exercise 3: Built-in functions
# Create a list of numbers: 15, 7, 23, 4, 18
# Find and display:
# - The largest number
# - The smallest number
# - The average (sum divided by count)


# Exercise 4: Type conversion
# Create a variable: price = "49.99"
# Convert it to a number.
# Calculate tax (8% of price).
# Display the total (price + tax).


# Exercise 5: Real-world calculation
# You're planning a road trip.
# Create variables for:
# - Distance in miles: 300
# - Miles per gallon your car gets: 25
# - Price per gallon of gas: 3.50
# Calculate and display:
# - Gallons needed
# - Total gas cost


# Exercise 6: Circle calculations
# Create a variable: radius = 5
# Calculate:
# - Circumference (2 × π × radius) - use 3.14159 for π
# - Area (π × radius²)
# Display both results rounded to 2 decimal places
