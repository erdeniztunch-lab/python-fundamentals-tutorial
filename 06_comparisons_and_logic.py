# ============================================
# COMPARISON AND LOGICAL OPERATORS
# ============================================

# --------------------------------------------
# BOOLEAN VALUES
# --------------------------------------------

# Boolean values are True or False
# They answer yes/no questions

is_student = True
is_raining = False

# Note: Must be capitalized - True and False, not true and false

# --------------------------------------------
# TRUTHY AND FALSY VALUES
# --------------------------------------------

# Some values are treated as True or False in conditions

# FALSY VALUES (treated as False):
print(bool(0))        # False - zero is falsy
print(bool(""))       # False - empty string is falsy
print(bool([]))       # False - empty list is falsy
print(bool(None))     # False - None is falsy

# TRUTHY VALUES (treated as True):
print(bool(1))        # True - any non-zero number is truthy
print(bool(-5))       # True - negative numbers are truthy
print(bool("Hello"))  # True - non-empty strings are truthy
print(bool([1, 2]))   # True - non-empty lists are truthy

# --------------------------------------------
# COMPARISON OPERATORS
# --------------------------------------------

# Comparison operators compare values and return True or False

# Greater than (>)
print(5 > 3)     # True
print(2 > 10)    # False

# Less than (<)
print(5 < 10)    # True
print(20 < 5)    # False

# Equal to (==)
print(5 == 5)    # True
print(5 == 3)    # False

# Not equal to (!=)
print(5 != 3)    # True
print(5 != 5)    # False

# Greater than or equal (>=)
print(5 >= 5)    # True
print(10 >= 20)  # False

# Less than or equal (<=)
print(5 <= 5)    # True
print(10 <= 5)   # False

# Comparing strings (alphabetical order):
print("apple" < "banana")  # True (a comes before b)
print("cat" > "dog")       # False (c comes before d)

# How it works: Python compares ASCII values
# Each letter has a number value
print(ord("a"))  # 97 (ASCII value of 'a')
print(ord("b"))  # 98 (ASCII value of 'b')

# --------------------------------------------
# LOGICAL OPERATORS
# --------------------------------------------

# Logical operators combine multiple conditions

# AND - both conditions must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# Think of AND as "both must be true"
age = 25
has_license = True
print(age >= 18 and has_license)  # True (both are true)

# OR - at least one condition must be True
print(True or False)    # True
print(False or False)   # False
print(True or True)     # True

# Think of OR as "at least one must be true"
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)  # True (one is true)

# NOT - reverses the condition
print(not True)   # False
print(not False)  # True

is_raining = False
print(not is_raining)  # True (it's NOT raining)

# --------------------------------------------
# COMBINING COMPARISONS AND LOGIC
# --------------------------------------------

# Example 1: Check if someone can drive
age = 20
has_license = True
has_car = True

can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True

# Example 2: Check eligibility for discount
age = 15
is_student = True

gets_discount = age < 18 or is_student
print(f"Gets discount: {gets_discount}")  # True

# Example 3: Security system
motion_detected = True
alarm_enabled = True
is_daytime = False

trigger_alarm = motion_detected and alarm_enabled and not is_daytime
print(f"Trigger alarm: {trigger_alarm}")  # True

# --------------------------------------------
# SHORT-CIRCUIT EVALUATION
# --------------------------------------------

# Python stops checking as soon as it knows the answer

# AND example:
high_income = False
good_credit = True

# Python checks high_income first
# Since it's False, the whole AND is False
# Python doesn't even check good_credit
eligible = high_income and good_credit
print(eligible)  # False

# OR example:
has_permission = True
is_admin = False

# Python checks has_permission first
# Since it's True, the whole OR is True
# Python doesn't need to check is_admin
can_access = has_permission or is_admin
print(can_access)  # True

# --------------------------------------------
# CHAINING COMPARISONS
# --------------------------------------------

# You can chain multiple comparisons

# Regular way:
age = 30
result = age >= 18 and age < 65
print(result)  # True

# Chained way (easier to read):
age = 30
result = 18 <= age < 65
print(result)  # True

# More examples:
score = 85
is_passing = 60 <= score <= 100
print(f"Passing: {is_passing}")  # True

temperature = 72
is_comfortable = 65 <= temperature <= 75
print(f"Comfortable: {is_comfortable}")  # True

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Login system
username = "alice"
password = "secret123"
stored_username = "alice"
stored_password = "secret123"

login_successful = username == stored_username and password == stored_password
print(f"Login successful: {login_successful}")  # True

# Example 2: Shopping eligibility
age = 25
has_account = True
balance = 500
item_price = 300

can_purchase = age >= 18 and has_account and balance >= item_price
print(f"Can purchase: {can_purchase}")  # True

# Example 3: Weather app
temperature = 85
humidity = 70
is_sunny = True

heat_advisory = temperature > 90 or (temperature > 80 and humidity > 60)
good_beach_day = is_sunny and 70 <= temperature <= 85 and not heat_advisory
print(f"Heat advisory: {heat_advisory}")      # False
print(f"Good beach day: {good_beach_day}")    # True

# Example 4: Movie ratings
age = 16
with_parent = False
movie_rating = "R"

# PG-13: anyone
# R: 17+ or with parent
can_watch = (movie_rating == "PG-13") or (movie_rating ==
                                          "R" and (age >= 17 or with_parent))
print(f"Can watch: {can_watch}")  # False

# Example 5: Grade calculator
score = 85
attendance = 95
submitted_project = True

passing_grade = score >= 60 and attendance >= 80 and submitted_project
honor_roll = score >= 90 and attendance >= 95
print(f"Passing: {passing_grade}")    # True
print(f"Honor roll: {honor_roll}")     # False

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Basic comparisons
# Create two variables with numbers.
# Display the result of:
# - Is the first greater than the second?
# - Are they equal?
# - Is the first less than or equal to the second?


# Exercise 2: Logical operators
# Create three boolean variables.
# Display the result of:
# - All three using AND
# - At least one using OR
# - The opposite of the first variable using NOT


# Exercise 3: Age checker
# Create a variable: age = 16
# Check if the person:
# - Can vote (18 or older)
# - Can get a driver's permit (15-17)
# - Is a child (under 13)


# Exercise 4: Password validator
# Create variables for a password and confirmation.
# Check if:
# - They match
# - Password length is at least 8 characters
# - Both conditions are true


# Exercise 5: Store hours checker
# A store is open Monday-Friday, 9 AM - 5 PM.
# Create variables:
# - current_day = "Wednesday"
# - current_hour = 14 (2 PM)
# Check if the store is open using logical operators.


# Exercise 6: Temperature alert
# Create a variable: temperature = 95
# Create alerts for:
# - Cold (below 32)
# - Hot (above 90)
# - Perfect (between 65 and 75)


# Exercise 7: Loan approval
# Create variables for:
# - Credit score (e.g., 720)
# - Annual income (e.g., 50000)
# - Debt-to-income ratio (e.g., 0.3)
# Approve loan if:
# - Credit score >= 650 AND
# - Income >= 30000 AND
# - Debt ratio < 0.4
# Display whether approved.
