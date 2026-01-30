"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 5: CONDITIONAL STATEMENTS
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ if statements
✓ if-else statements
✓ if-elif-else statements
✓ Ternary operator
✓ Indentation in Python
✓ Nested conditionals

Goal: Master decision-making in Python programs
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. IF STATEMENTS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. IF STATEMENTS")
print("=" * 70)

print("""
The if statement executes a block of code only if a condition is True.

Syntax:
    if condition:
        # code block executes if condition is True
""")

# Basic if statement
age = 20

print(f"Age: {age}")
if age >= 18:
    print("You are an adult.")
    print("You can vote.")

print("\n💡 Key Points:")
print("   • Condition must evaluate to True/False")
print("   • Colon (:) is required after the condition")
print("   • Code block must be indented")
print("   • If condition is False, block is skipped")

# 🌍 REAL-WORLD EXAMPLE: Temperature Warning
print("\n🌍 Real-World Example: Temperature Warning System")
print("-" * 70)

temperature = 102
HIGH_TEMP_THRESHOLD = 100

print(f"Current Temperature: {temperature}°F")
print(f"High Temperature Alert Threshold: {HIGH_TEMP_THRESHOLD}°F")
print()

if temperature > HIGH_TEMP_THRESHOLD:
    print("⚠️ WARNING: High temperature detected!")
    print("Please stay hydrated and stay indoors.")

# ═══════════════════════════════════════════════════════════════════════════
# 2. IF-ELSE STATEMENTS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. IF-ELSE STATEMENTS")
print("=" * 70)

print("""
The if-else statement provides an alternative path when condition is False.

Syntax:
    if condition:
        # executes if condition is True
    else:
        # executes if condition is False
""")

age = 16

print(f"Age: {age}")
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 🌍 REAL-WORLD EXAMPLE: Password Strength
print("\n🌍 Real-World Example: Password Strength Checker")
print("-" * 70)


def check_password_strength(password):
    """Check if password meets minimum requirements"""
    MIN_LENGTH = 8

    print(f"Checking password: {'*' * len(password)}")
    print(f"Length: {len(password)} characters")
    print()

    if len(password) >= MIN_LENGTH:
        print("✅ Password meets minimum length requirement")
        return True
    else:
        print(
            f"❌ Password too short! Must be at least {MIN_LENGTH} characters")
        return False


check_password_strength("Pass123")
print()
check_password_strength("SecurePassword123")

# ═══════════════════════════════════════════════════════════════════════════
# 3. IF-ELIF-ELSE STATEMENTS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. IF-ELIF-ELSE STATEMENTS")
print("=" * 70)

print("""
The if-elif-else statement checks multiple conditions sequentially.

Syntax:
    if condition1:
        # executes if condition1 is True
    elif condition2:
        # executes if condition1 is False and condition2 is True
    elif condition3:
        # executes if previous conditions are False and condition3 is True
    else:
        # executes if all conditions are False
""")

age = 25

print(f"Age: {age}\n")
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 🌍 REAL-WORLD EXAMPLE: Shipping Cost Calculator
print("\n🌍 Real-World Example: Shipping Cost Calculator")
print("-" * 70)


def calculate_shipping(weight, destination):
    """Calculate shipping cost based on weight and destination"""
    print(f"Package weight: {weight} kg")
    print(f"Destination: {destination}")
    print()

    # Determine shipping cost
    if destination == "Local":
        if weight <= 1:
            cost = 5.00
        elif weight <= 5:
            cost = 10.00
        elif weight <= 10:
            cost = 15.00
        else:
            cost = 25.00
    elif destination == "National":
        if weight <= 1:
            cost = 10.00
        elif weight <= 5:
            cost = 20.00
        elif weight <= 10:
            cost = 30.00
        else:
            cost = 50.00
    elif destination == "International":
        if weight <= 1:
            cost = 25.00
        elif weight <= 5:
            cost = 50.00
        elif weight <= 10:
            cost = 75.00
        else:
            cost = 125.00
    else:
        cost = 0
        print("❌ Invalid destination!")
        return None

    print(f"Shipping Cost: ${cost:.2f}")
    return cost


calculate_shipping(3, "Local")
print()
calculate_shipping(7, "National")
print()
calculate_shipping(12, "International")

# ═══════════════════════════════════════════════════════════════════════════
# 4. INDENTATION
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. INDENTATION IN PYTHON")
print("=" * 70)

print("""
Indentation is CRITICAL in Python!
• Python uses indentation to define code blocks
• Use 4 spaces for each indentation level (PEP 8 standard)
• Do NOT mix tabs and spaces
• Consistent indentation is required
""")

print("\n✅ CORRECT Indentation:")
print("""
age = 20
if age >= 18:
    print("Adult")      # 4 spaces indentation
    print("Can vote")   # Same indentation level
""")

print("❌ INCORRECT Indentation:")
print("""
age = 20
if age >= 18:
print("Adult")          # IndentationError!
    print("Can vote")
""")

# Example with multiple levels
score = 85
print(f"\nScore: {score}")

if score >= 60:
    print("Passed!")
    if score >= 90:
        print("  Excellent work!")
        print("  Grade: A")
    elif score >= 80:
        print("  Good job!")
        print("  Grade: B")
    else:
        print("  Satisfactory")
        print("  Grade: C")
else:
    print("Failed")
    print("  Please try again")

# ═══════════════════════════════════════════════════════════════════════════
# 5. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. TERNARY OPERATOR")
print("=" * 70)

print("""
The ternary operator provides a concise way to write simple if-else.

Syntax:
    variable = value_if_true if condition else value_if_false
""")

# Traditional if-else
age = 20
print("📌 Traditional Way:")
print("age = 20")
print("""
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
""")

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"Result: status = '{status}'")

# Ternary operator
print("\n📌 Ternary Operator Way:")
print("status = 'Adult' if age >= 18 else 'Minor'")

status = "Adult" if age >= 18 else "Minor"
print(f"Result: status = '{status}'")

# More examples
print("\n📌 More Ternary Examples:")

num = 15
result = "Even" if num % 2 == 0 else "Odd"
print(f"   {num} is {result}")

score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"   Score {score}: {grade}")

temperature = 75
weather = "Hot" if temperature > 80 else "Pleasant" if temperature > 60 else "Cold"
print(f"   {temperature}°F is {weather}")

# 🌍 REAL-WORLD EXAMPLE: Discount Badge
print("\n🌍 Real-World Example: Product Discount Badge")
print("-" * 70)


def get_discount_badge(price, original_price):
    """Generate discount badge for product"""
    discount_percent = ((original_price - price) / original_price) * 100

    badge = (
        "🔥 HOT DEAL!" if discount_percent >= 50 else
        "💰 GREAT SALE!" if discount_percent >= 30 else
        "✨ ON SALE" if discount_percent >= 10 else
        "Regular Price"
    )

    print(f"Original: ${original_price:.2f}")
    print(f"Current: ${price:.2f}")
    print(f"Discount: {discount_percent:.0f}%")
    print(f"Badge: {badge}")


get_discount_badge(50, 100)
print()
get_discount_badge(70, 100)
print()
get_discount_badge(90, 100)

# ═══════════════════════════════════════════════════════════════════════════
# 6. NESTED CONDITIONALS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("6. NESTED CONDITIONALS")
print("=" * 70)

print("""
Nested conditionals are if statements inside other if statements.
Use them when decisions depend on multiple factors.
""")

# Example: Login system
username = "admin"
password = "secure123"
is_active = True

print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print(f"Account Active: {is_active}")
print()

if username == "admin":
    print("✓ Username correct")
    if password == "secure123":
        print("✓ Password correct")
        if is_active:
            print("✓ Account is active")
            print("🎉 Login successful!")
        else:
            print("❌ Account is deactivated")
    else:
        print("❌ Incorrect password")
else:
    print("❌ User not found")

# 🌍 REAL-WORLD EXAMPLE: Loan Approval
print("\n🌍 Real-World Example: Loan Approval System")
print("-" * 70)


def process_loan_application(income, credit_score, employment_years, has_debt):
    """Process loan application with multiple criteria"""
    print("Loan Application Processing")
    print("=" * 40)
    print(f"Annual Income: ${income:,}")
    print(f"Credit Score: {credit_score}")
    print(f"Years Employed: {employment_years}")
    print(f"Has Existing Debt: {has_debt}")
    print("=" * 40)
    print()

    # First level: Check income
    if income >= 40000:
        print("✓ Income requirement met")

        # Second level: Check credit score
        if credit_score >= 650:
            print("✓ Credit score requirement met")

            # Third level: Check employment
            if employment_years >= 2:
                print("✓ Employment requirement met")

                # Fourth level: Check debt
                if not has_debt:
                    print("✓ No existing debt")
                    print("\n🎉 LOAN APPROVED!")
                    print("   Interest Rate: 3.5%")
                    return "Approved"
                else:
                    print("⚠️ Has existing debt")
                    print("\n✅ LOAN APPROVED (Higher Rate)")
                    print("   Interest Rate: 5.0%")
                    return "Approved (Higher Rate)"
            else:
                print("❌ Insufficient employment history")
                print(f"   Need {2 - employment_years} more year(s)")
        else:
            print("❌ Credit score too low")
            print(f"   Need {650 - credit_score} more points")
    else:
        print("❌ Income too low")
        print(f"   Need ${40000 - income:,} more annual income")

    print("\n❌ LOAN DENIED")
    return "Denied"


process_loan_application(50000, 700, 3, False)
print("\n")
process_loan_application(35000, 600, 1, True)

# ═══════════════════════════════════════════════════════════════════════════
# 7. PRACTICAL EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("7. PRACTICAL EXAMPLES")
print("=" * 70)

# Example 1: Grade Calculator
print("\n🌍 Example 1: Grade Calculator")
print("-" * 70)


def calculate_letter_grade(score):
    """Convert numerical score to letter grade"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


scores = [95, 87, 72, 68, 55]
for score in scores:
    grade = calculate_letter_grade(score)
    status = "Pass" if grade != 'F' else "Fail"
    print(f"Score: {score} → Grade: {grade} → {status}")

# Example 2: Ticket Pricing
print("\n🌍 Example 2: Movie Ticket Pricing")
print("-" * 70)


def calculate_ticket_price(age, is_student, is_weekend):
    """Calculate movie ticket price based on multiple factors"""
    BASE_PRICE = 15.00

    # Age discount
    if age < 12:
        price = BASE_PRICE * 0.5  # 50% off for children
        category = "Child"
    elif age >= 65:
        price = BASE_PRICE * 0.7  # 30% off for seniors
        category = "Senior"
    else:
        price = BASE_PRICE
        category = "Adult"

    # Student discount (only for adults)
    if is_student and 12 <= age < 65:
        price *= 0.85  # 15% student discount
        category += " (Student)"

    # Weekend surcharge
    if is_weekend:
        price *= 1.2  # 20% weekend surcharge
        category += " - Weekend"
    else:
        category += " - Weekday"

    print(f"Age: {age}, Student: {is_student}, Weekend: {is_weekend}")
    print(f"Category: {category}")
    print(f"Price: ${price:.2f}")
    print()


calculate_ticket_price(10, False, False)
calculate_ticket_price(25, True, True)
calculate_ticket_price(70, False, False)

# Example 3: Temperature Converter with Validation
print("\n🌍 Example 3: Temperature Converter with Validation")
print("-" * 70)


def convert_temperature(value, unit):
    """Convert temperature between Celsius and Fahrenheit"""
    ABSOLUTE_ZERO_C = -273.15
    ABSOLUTE_ZERO_F = -459.67

    if unit.upper() == 'C':
        if value < ABSOLUTE_ZERO_C:
            print(f"❌ Error: {value}°C is below absolute zero!")
            return None

        fahrenheit = (value * 9/5) + 32
        print(f"{value}°C = {fahrenheit:.2f}°F")

        if fahrenheit > 100:
            print("  ⚠️ Very hot!")
        elif fahrenheit > 70:
            print("  ☀️ Warm")
        elif fahrenheit > 32:
            print("  🌤️ Cool")
        else:
            print("  ❄️ Freezing")

        return fahrenheit

    elif unit.upper() == 'F':
        if value < ABSOLUTE_ZERO_F:
            print(f"❌ Error: {value}°F is below absolute zero!")
            return None

        celsius = (value - 32) * 5/9
        print(f"{value}°F = {celsius:.2f}°C")

        if celsius > 38:
            print("  ⚠️ Very hot!")
        elif celsius > 21:
            print("  ☀️ Warm")
        elif celsius > 0:
            print("  🌤️ Cool")
        else:
            print("  ❄️ Freezing")

        return celsius

    else:
        print(f"❌ Error: Invalid unit '{unit}'. Use 'C' or 'F'")
        return None


convert_temperature(25, 'C')
print()
convert_temperature(77, 'F')
print()
convert_temperature(-300, 'C')

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: Number Classification
---------------------------------
Write a program that classifies a number as:
- Positive, Negative, or Zero
Test with: 10, -5, 0

Exercise 2: Leap Year Checker
-----------------------------
Create a function to check if a year is a leap year.
Rules:
- Divisible by 4: Leap year
- EXCEPT if divisible by 100: Not a leap year
- EXCEPT if divisible by 400: Leap year

Test with: 2024, 2000, 1900, 2023

Exercise 3: BMI Calculator with Categories
------------------------------------------
Create a BMI calculator that:
1. Calculates BMI = weight / (height ** 2)
2. Categorizes result:
   - BMI < 18.5: Underweight
   - 18.5 <= BMI < 25: Normal weight
   - 25 <= BMI < 30: Overweight
   - BMI >= 30: Obese

Test with: weight=70kg, height=1.75m

Exercise 4: Day of Week
-----------------------
Create a function that takes a number (1-7) and returns:
1 = Monday, 2 = Tuesday, ..., 7 = Sunday
If number is not 1-7, return "Invalid day"

Use if-elif-else

Exercise 5: Triangle Type
-------------------------
Write a function that determines triangle type:
- Equilateral: All sides equal
- Isosceles: Two sides equal
- Scalene: All sides different
- Invalid: Sides can't form a triangle

Test with: (3,3,3), (5,5,3), (3,4,5), (1,2,10)

Exercise 6: Tax Calculator
--------------------------
Create a progressive tax calculator:
Income brackets:
- $0 - $10,000: 0% tax
- $10,001 - $40,000: 10% tax
- $40,001 - $100,000: 20% tax
- Above $100,000: 30% tax

Calculate tax for: $8,000, $35,000, $75,000, $150,000

Exercise 7: Login System
------------------------
Create a simple login system that checks:
1. Username exists (check against a list)
2. Password is correct
3. Account is not locked
4. Account is active

Print appropriate messages for each validation step.

Exercise 8: Shipping Calculator
-------------------------------
Calculate shipping cost based on:
- Weight (kg)
- Destination (Local/National/International)
- Express shipping (Yes/No)

Rules:
- Local: $5 base + $2/kg
- National: $10 base + $3/kg
- International: $20 base + $5/kg
- Express adds 50% to total

Exercise 9: Student Eligibility
-------------------------------
Check if a student is eligible for a scholarship:
Requirements:
- GPA >= 3.5 AND
- (Extracurricular activities OR community service) AND
- Family income < $50,000

Test different combinations.

Bonus Exercise: Vending Machine
-------------------------------
Create a vending machine simulator:
- Products with prices
- Check if money inserted is enough
- Calculate change
- Handle "out of stock" scenarios
- Handle exact change situations

Items:
- Soda: $1.50
- Chips: $1.25
- Candy: $0.75
- Water: $1.00
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 5")
print("=" * 70)
print("\nNext Module: Loops")
print("Keep practicing and happy coding! 🚀")
