# ============================================
# VARIABLES
# ============================================

# --------------------------------------------
# WHAT IS A VARIABLE?
# --------------------------------------------

# A variable is like a labeled box where you store information.
# You give it a name and put a value inside.

students_count = 1000  # A box labeled "students_count" containing 1000

# Think of variables like:
# - A container with a label
# - A locker with your name on it
# - A folder with a name tag

# --------------------------------------------
# WHY USE VARIABLES?
# --------------------------------------------

# Variables let you:
# 1. Store information to use later
# 2. Give meaningful names to values
# 3. Update values when needed
# 4. Make your code easier to understand

# --------------------------------------------
# TYPES OF VARIABLES (DATA TYPES)
# --------------------------------------------

# 1. INTEGER (whole numbers)
age = 25
year = 2024
score = 100

# 2. FLOAT (decimal numbers)
price = 19.99
height = 5.9
temperature = 72.5

# 3. STRING (text)
name = "Alice"
city = "New York"
message = "Hello, World!"

# 4. BOOLEAN (True or False)
is_student = True
is_raining = False
has_license = True

# Note: Boolean values always start with a capital letter
# True (not true), False (not false)

# --------------------------------------------
# VARIABLE NAMING RULES
# --------------------------------------------

# ✅ GOOD VARIABLE NAMES:
first_name = "John"      # Use underscores for multiple words
age = 30                 # Descriptive names
total_price = 49.99      # Clear what it contains

# ❌ BAD VARIABLE NAMES (These cause errors):
# 2students = 50         # Can't start with a number
# first-name = "Jane"    # Can't use dashes
# class = "Math"         # Can't use Python keywords

# 💡 TIPS FOR GOOD NAMES:
# - Use lowercase letters
# - Use underscores for spaces
# - Make names descriptive
# - Avoid single letters (except in loops)

# --------------------------------------------
# USING VARIABLES
# --------------------------------------------

# Create a variable:
price = 50

# Use the variable:
print(price)  # Displays: 50

# Update the variable:
price = 75
print(price)  # Displays: 75

# Use in calculations:
total = price + 10
print(total)  # Displays: 85

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Store customer information
customer_name = "Sarah Johnson"
customer_age = 28
is_member = True
balance = 1234.50

print(customer_name)  # Sarah Johnson
print(balance)        # 1234.50

# Example 2: Calculate shopping total
shirt_price = 25.99
pants_price = 45.00
tax = 5.50
total_cost = shirt_price + pants_price + tax
print(total_cost)  # 76.49

# Example 3: Store and update game score
player_score = 0
print("Starting score:", player_score)  # 0
player_score = 10
print("After level 1:", player_score)   # 10
player_score = player_score + 15
print("After level 2:", player_score)   # 25

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Create variables
# Create 4 variables:
# - Your name (string)
# - Your age (integer)
# - Your height in feet (float)
# - Whether you like pizza (boolean)


# Exercise 2: Use variables in calculations
# Create two variables with numbers.
# Add them together and store the result in a third variable.
# Display the result.


# Exercise 3: Update variables
# Create a variable called "money" with value 100.
# Subtract 30 from it and update the variable.
# Add 50 to it and update again.
# Display the final value.


# Exercise 4: Real-world scenario
# You're running a lemonade stand.
# Create variables for:
# - Number of cups sold
# - Price per cup
# - Total earnings (cups sold × price)
# Display your total earnings.
