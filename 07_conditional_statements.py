# ============================================
# CONDITIONAL STATEMENTS (IF/ELIF/ELSE)
# ============================================

# --------------------------------------------
# WHAT ARE CONDITIONAL STATEMENTS?
# --------------------------------------------

# Conditional statements let your code make decisions
# They run different code based on whether conditions are True or False

# Think of it like:
# "IF it's raining, bring an umbrella"
# "IF you're hungry, eat something"

# --------------------------------------------
# IF STATEMENT
# --------------------------------------------

# IF runs code only when a condition is True

age = 18

if age >= 18:
    print("You are an adult.")

# How it works:
# 1. Python checks if age >= 18 is True
# 2. If True, it runs the indented code
# 3. If False, it skips the indented code

# More examples:
temperature = 85
if temperature > 80:
    print("It's hot outside!")

balance = 500
if balance > 100:
    print("You have enough money.")

# --------------------------------------------
# INDENTATION
# --------------------------------------------

# Indentation (spaces at the start of a line) is CRITICAL in Python
# It tells Python what code belongs to the IF statement

# ✅ CORRECT:
age = 20
if age >= 18:
    print("Adult")        # This runs if condition is True
    print("Can vote")     # This also runs if condition is True
print("Done")             # This always runs (not indented)

# ❌ WRONG (causes an error):
# if age >= 18:
# print("Adult")  # No indentation - ERROR!

# Use 4 spaces for indentation (most code editors do this automatically)

# --------------------------------------------
# IF-ELSE STATEMENT
# --------------------------------------------

# ELSE runs code when the IF condition is False

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# How it works:
# 1. Checks IF condition
# 2. If True: runs IF block
# 3. If False: runs ELSE block

# Real-world examples:
password = "secret123"
if password == "secret123":
    print("Access granted!")
else:
    print("Wrong password!")

temperature = 60
if temperature > 70:
    print("Wear a t-shirt")
else:
    print("Wear a jacket")

# --------------------------------------------
# IF-ELIF-ELSE STATEMENT
# --------------------------------------------

# ELIF (else if) checks multiple conditions

age = 15

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# How it works:
# 1. Checks first IF condition
# 2. If False, checks ELIF condition
# 3. If False, checks next ELIF (can have multiple)
# 4. If all False, runs ELSE

# You can have multiple ELIF statements:
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# --------------------------------------------
# NESTED IF STATEMENTS
# --------------------------------------------

# You can put IF statements inside other IF statements

age = 25
has_license = True

if age >= 18:
    print("You are old enough.")
    if has_license:
        print("You can drive!")
    else:
        print("You need a license.")
else:
    print("You are too young to drive.")

# Real-world example: Online shopping
is_member = True
purchase_amount = 150

if is_member:
    if purchase_amount >= 100:
        discount = 0.20  # 20% discount
        print("Member discount: 20%")
    else:
        discount = 0.10  # 10% discount
        print("Member discount: 10%")
else:
    discount = 0
    print("No discount. Join for savings!")

# --------------------------------------------
# TERNARY OPERATOR (ONE-LINE IF)
# --------------------------------------------

# A shorter way to write simple IF-ELSE statements

# Regular way:
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(status)

# Ternary way (one line):
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# More examples:
weather = "sunny"
activity = "go outside" if weather == "sunny" else "stay inside"
print(activity)

score = 85
result = "Pass" if score >= 60 else "Fail"
print(result)

# Even with elif logic:
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)

# --------------------------------------------
# USING LOGICAL OPERATORS IN IF
# --------------------------------------------

# Combine multiple conditions with AND, OR, NOT

# AND example:
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# OR example:
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Time to work")

# NOT example:
is_raining = False

if not is_raining:
    print("Good day for a walk!")
else:
    print("Stay inside")

# Complex example:
age = 25
income = 50000
credit_score = 720

if age >= 18 and income >= 30000 and credit_score >= 650:
    print("Loan approved!")
else:
    print("Loan denied")

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Login system
username = "alice"
password = "pass123"

if username == "alice" and password == "pass123":
    print("Welcome, Alice!")
elif username == "alice":
    print("Wrong password")
else:
    print("User not found")

# Example 2: Shipping calculator
weight = 15
distance = 200

if weight <= 10:
    cost = 5
elif weight <= 20:
    cost = 10
else:
    cost = 15

if distance > 100:
    cost += 5  # Add $5 for long distance

print(f"Shipping cost: ${cost}")

# Example 3: Movie ticket pricing
age = 12
is_student = False
day = "Wednesday"

if age < 12:
    price = 5
elif age >= 65:
    price = 7
elif is_student:
    price = 8
elif day == "Wednesday":
    price = 9
else:
    price = 12

print(f"Ticket price: ${price}")

# Example 4: Temperature advisor
temperature = 95
humidity = 80

if temperature > 100:
    print("Extreme heat! Stay indoors.")
elif temperature > 90:
    if humidity > 70:
        print("Hot and humid. Stay hydrated!")
    else:
        print("Hot. Seek shade.")
elif temperature > 70:
    print("Nice weather!")
else:
    print("Cool weather. Bring a jacket.")

# Example 5: Grade calculator with feedback
score = 88
attendance = 95

if score >= 90 and attendance >= 90:
    grade = "A"
    feedback = "Excellent work!"
elif score >= 80 and attendance >= 80:
    grade = "B"
    feedback = "Good job!"
elif score >= 70 and attendance >= 70:
    grade = "C"
    feedback = "Satisfactory"
elif score >= 60:
    grade = "D"
    feedback = "Needs improvement"
else:
    grade = "F"
    feedback = "See instructor"

print(f"Grade: {grade}")
print(f"Feedback: {feedback}")

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Basic IF
# Create a variable: temperature = 75
# If temperature is above 80, display "It's hot!"


# Exercise 2: IF-ELSE
# Create a variable: age = 16
# Display "Can drive" if age is 16 or older
# Otherwise display "Too young to drive"


# Exercise 3: IF-ELIF-ELSE
# Create a variable: grade = 85
# Display:
# - "Excellent" if grade is 90 or above
# - "Good" if grade is 80-89
# - "Fair" if grade is 70-79
# - "Needs work" if below 70


# Exercise 4: Multiple conditions
# Create variables:
# - age = 25
# - has_ticket = True
# Display "Can board plane" only if both:
# - Age is 18 or older
# - Has ticket is True


# Exercise 5: Nested IF
# Create variables:
# - is_weekend = True
# - weather = "sunny"
# If it's the weekend:
#   If weather is sunny: display "Go to the beach!"
#   Otherwise: display "Movie day!"
# If it's not the weekend:
#   Display "Work day"


# Exercise 6: Ternary operator
# Create a variable: points = 150
# Use ternary operator to set status:
# - "Winner" if points >= 100
# - "Keep trying" otherwise


# Exercise 7: Password strength checker
# Create a variable: password = "hello"
# Check password strength:
# - "Strong" if length >= 12
# - "Medium" if length >= 8
# - "Weak" if length < 8


# Exercise 8: BMI calculator
# Create variables:
# - weight (in kg)
# - height (in meters)
# Calculate BMI: weight / (height * height)
# Display category:
# - "Underweight" if BMI < 18.5
# - "Normal" if BMI 18.5-24.9
# - "Overweight" if BMI 25-29.9
# - "Obese" if BMI >= 30


# Exercise 9: Discount calculator
# Create variables:
# - is_member = True
# - total_purchase = 200
# Calculate discount:
# - If member AND purchase >= 100: 20% off
# - If member AND purchase < 100: 10% off
# - If not member: no discount
# Display final price


# Exercise 10: Traffic light
# Create a variable: light = "yellow"
# Display:
# - "Go" if green
# - "Slow down" if yellow
# - "Stop" if red
# - "Error" for any other value
