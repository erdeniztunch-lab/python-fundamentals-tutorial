"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 7: FUNCTIONS
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ Defining and calling functions
✓ Parameters vs Arguments
✓ Return values
✓ Default parameters
✓ Keyword arguments
✓ *args and **kwargs
✓ Variable scope
✓ Docstrings

Goal: Master creating and using functions in Python
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. DEFINING AND CALLING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. DEFINING AND CALLING FUNCTIONS")
print("=" * 70)

print("""
A function is a reusable block of code that performs a specific task.

Syntax:
    def function_name():
        # code block
        
To call a function:
    function_name()
""")

# Simple function without parameters
print("📌 Simple Function:\n")


def greet():
    """Display a greeting message"""
    print("Hello!")
    print("Welcome to Python!")


# Calling the function
greet()

# Function naming conventions
print("\n💡 Function Naming Rules:")
print("   • Use descriptive names: calculate_total(), not ct()")
print("   • Use snake_case: get_user_name(), not getUserName()")
print("   • Use verbs: calculate(), process(), display()")
print("   • Avoid reserved keywords")

# 🌍 REAL-WORLD EXAMPLE: Display Menu
print("\n🌍 Real-World Example: Restaurant Menu Display")
print("-" * 70)


def display_menu():
    """Display restaurant menu"""
    print("╔════════════════════════════════╗")
    print("║       RESTAURANT MENU          ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Burger............... $8.99 ║")
    print("║ 2. Pizza............... $12.99 ║")
    print("║ 3. Salad................ $6.99 ║")
    print("║ 4. Pasta............... $10.99 ║")
    print("║ 5. Drink................ $2.99 ║")
    print("╚════════════════════════════════╝")


display_menu()

# ═══════════════════════════════════════════════════════════════════════════
# 2. PARAMETERS AND ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. PARAMETERS AND ARGUMENTS")
print("=" * 70)

print("""
Parameter: Variable in the function definition
Argument: Actual value passed when calling the function

def greet(name):  ← 'name' is a parameter
    print(f"Hello {name}!")
    
greet("Alice")  ← "Alice" is an argument
""")

# Function with single parameter
print("📌 Single Parameter:\n")


def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
print("\n📌 Multiple Parameters:\n")


def calculate_rectangle_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    print(f"Rectangle: {length} x {width}")
    print(f"Area: {area}")


calculate_rectangle_area(10, 5)
calculate_rectangle_area(7, 3)

# 🌍 REAL-WORLD EXAMPLE: Order Processing
print("\n🌍 Real-World Example: Process Customer Order")
print("-" * 70)


def process_order(customer_name, product, quantity, price):
    """Process a customer order"""
    total = quantity * price

    print(f"Order Confirmation")
    print(f"Customer: {customer_name}")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per unit: ${price:.2f}")
    print(f"Total: ${total:.2f}")


process_order("John Smith", "Laptop", 2, 999.99)

# ═══════════════════════════════════════════════════════════════════════════
# 3. RETURN VALUES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. RETURN VALUES")
print("=" * 70)

print("""
Functions can return values using the 'return' statement.
The return statement:
1. Ends function execution
2. Sends a value back to the caller
""")

# Function with return value
print("📌 Function with Return:\n")


def add(a, b):
    """Add two numbers and return the result"""
    return a + b


result = add(5, 3)
print(f"5 + 3 = {result}")

# Using return value in expression
total = add(10, 20) + add(5, 15)
print(f"(10 + 20) + (5 + 15) = {total}")

# Function without return (returns None)
print("\n📌 Function Without Return:\n")


def say_hello(name):
    """Greet a person"""
    print(f"Hello, {name}!")


result = say_hello("Alice")
print(f"Return value: {result}")  # None

# Multiple return statements
print("\n📌 Multiple Return Statements:\n")


def get_grade(score):
    """Convert score to letter grade"""
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


print(f"Score 95: Grade {get_grade(95)}")
print(f"Score 82: Grade {get_grade(82)}")
print(f"Score 55: Grade {get_grade(55)}")

# Returning multiple values (tuple)
print("\n📌 Returning Multiple Values:\n")


def get_user_info():
    """Return multiple user details"""
    name = "Alice"
    age = 28
    city = "New York"
    return name, age, city  # Returns a tuple


user_name, user_age, user_city = get_user_info()
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"City: {user_city}")

# 🌍 REAL-WORLD EXAMPLE: Calculate Discount
print("\n🌍 Real-World Example: Price Calculator with Discount")
print("-" * 70)


def calculate_final_price(price, discount_percent):
    """Calculate final price after discount"""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return discount_amount, final_price


original_price = 100
discount_rate = 20

discount, final = calculate_final_price(original_price, discount_rate)
print(f"Original Price: ${original_price:.2f}")
print(f"Discount ({discount_rate}%): ${discount:.2f}")
print(f"Final Price: ${final:.2f}")

# ═══════════════════════════════════════════════════════════════════════════
# 4. DEFAULT PARAMETERS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. DEFAULT PARAMETERS")
print("=" * 70)

print("""
Default parameters have preset values that are used if no argument is provided.

def greet(name="Guest"):  ← "Guest" is default value
    print(f"Hello {name}!")
    
greet()         # Uses default: "Guest"
greet("Alice")  # Uses provided: "Alice"
""")

# Function with default parameter
print("📌 Default Parameters:\n")


def greet(name="Guest", greeting="Hello"):
    """Greet with customizable message"""
    print(f"{greeting}, {name}!")


greet()  # Uses both defaults
greet("Alice")  # Overrides name
greet("Bob", "Hi")  # Overrides both

# Order matters: default parameters must come after non-default
print("\n⚠️ Important: Default parameters must come AFTER non-default parameters")
print("""
✅ Correct:   def func(a, b, c=10)
❌ Incorrect: def func(a, c=10, b)
""")

# 🌍 REAL-WORLD EXAMPLE: Shipping Calculator
print("\n🌍 Real-World Example: Shipping Cost Calculator")
print("-" * 70)


def calculate_shipping(weight, distance=100, express=False):
    """
    Calculate shipping cost

    Args:
        weight: Package weight in kg
        distance: Shipping distance in km (default: 100)
        express: Express shipping option (default: False)
    """
    BASE_RATE = 5.00
    RATE_PER_KG = 2.00
    RATE_PER_KM = 0.10
    EXPRESS_MULTIPLIER = 1.5

    cost = BASE_RATE + (weight * RATE_PER_KG) + (distance * RATE_PER_KM)

    if express:
        cost *= EXPRESS_MULTIPLIER

    print(f"Weight: {weight}kg, Distance: {distance}km, Express: {express}")
    print(f"Shipping Cost: ${cost:.2f}")
    return cost


# Different ways to call
calculate_shipping(5)  # Uses defaults
calculate_shipping(5, 200)  # Custom distance
calculate_shipping(5, 200, True)  # All specified

# ═══════════════════════════════════════════════════════════════════════════
# 5. KEYWORD ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. KEYWORD ARGUMENTS")
print("=" * 70)

print("""
Keyword arguments allow you to pass arguments by parameter name.
This makes code more readable and allows passing arguments in any order.
""")

# Using keyword arguments
print("📌 Keyword Arguments:\n")


def create_profile(name, age, city, country):
    """Create user profile"""
    print(f"Profile Created:")
    print(f"  Name: {name}")
    print(f"  Age: {age}")
    print(f"  City: {city}")
    print(f"  Country: {country}")


# Positional arguments (order matters)
print("Positional Arguments:")
create_profile("Alice", 25, "New York", "USA")

# Keyword arguments (order doesn't matter)
print("\nKeyword Arguments:")
create_profile(city="London", name="Bob", country="UK", age=30)

# Mix of positional and keyword (positional must come first)
print("\nMixed:")
create_profile("Charlie", 28, country="Canada", city="Toronto")

# 🌍 REAL-WORLD EXAMPLE: Email Sender
print("\n🌍 Real-World Example: Send Email")
print("-" * 70)


def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    """
    Send an email with various options

    Args:
        to: Recipient email address
        subject: Email subject
        body: Email body content
        cc: CC recipients (optional)
        bcc: BCC recipients (optional)
        priority: Email priority (default: "normal")
    """
    print(f"Sending Email...")
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body[:50]}...")  # First 50 chars
    if cc:
        print(f"CC: {cc}")
    if bcc:
        print(f"BCC: {bcc}")
    print(f"Priority: {priority}")
    print("Email sent successfully!")


# Clear and readable calls using keyword arguments
send_email(
    to="client@example.com",
    subject="Project Update",
    body="Dear Client, The project is progressing well...",
    priority="high"
)

# ═══════════════════════════════════════════════════════════════════════════
# 6. *ARGS (VARIABLE LENGTH ARGUMENTS)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("6. *ARGS - VARIABLE LENGTH ARGUMENTS")
print("=" * 70)

print("""
*args allows a function to accept any number of positional arguments.
The arguments are collected into a tuple.

def func(*args):  # Can accept 0 or more arguments
    # args is a tuple
""")

# Function with *args
print("📌 Basic *args Usage:\n")


def multiply(*numbers):
    """Multiply all numbers together"""
    result = 1
    for num in numbers:
        result *= num
    return result


print(f"multiply(2, 3) = {multiply(2, 3)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")
print(f"multiply(1, 2, 3, 4, 5) = {multiply(1, 2, 3, 4, 5)}")

# More examples
print("\n📌 Sum Function with *args:\n")


def sum_all(*numbers):
    """Sum all provided numbers"""
    total = sum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    return total


sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)

# Mixing regular parameters with *args
print("\n📌 Mixing Parameters with *args:\n")


def greet_all(greeting, *names):
    """Greet multiple people with same greeting"""
    for name in names:
        print(f"{greeting}, {name}!")


greet_all("Hello", "Alice", "Bob", "Charlie")

# 🌍 REAL-WORLD EXAMPLE: Shopping Cart
print("\n🌍 Real-World Example: Calculate Total Price")
print("-" * 70)


def calculate_total(*prices, tax_rate=0.08):
    """
    Calculate total price with tax

    Args:
        *prices: Variable number of prices
        tax_rate: Tax rate (default: 8%)
    """
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax

    print(f"Items: {len(prices)}")
    print(f"Prices: ${prices}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate*100}%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    return total


calculate_total(29.99, 19.99, 49.99, 9.99)

# ═══════════════════════════════════════════════════════════════════════════
# 7. **KWARGS (KEYWORD ARGUMENTS)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("7. **KWARGS - KEYWORD VARIABLE ARGUMENTS")
print("=" * 70)

print("""
**kwargs allows a function to accept any number of keyword arguments.
The arguments are collected into a dictionary.

def func(**kwargs):  # Can accept 0 or more keyword arguments
    # kwargs is a dictionary
""")

# Function with **kwargs
print("📌 Basic **kwargs Usage:\n")


def print_user_info(**info):
    """Print user information"""
    print("User Information:")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")


print_user_info(name="Alice", age=25, city="New York", job="Engineer")

# Combining *args and **kwargs
print("\n📌 Combining *args and **kwargs:\n")


def create_order(order_id, *items, **details):
    """Create an order with items and details"""
    print(f"Order #{order_id}")
    print(f"\nItems ({len(items)}):")
    for item in items:
        print(f"  - {item}")
    print(f"\nDetails:")
    for key, value in details.items():
        print(f"  {key}: {value}")


create_order(
    12345,
    "Laptop",
    "Mouse",
    "Keyboard",
    customer="John Doe",
    payment="Credit Card",
    shipping="Express"
)

# 🌍 REAL-WORLD EXAMPLE: Database Query Builder
print("\n🌍 Real-World Example: Flexible Database Query")
print("-" * 70)


def build_query(table, *fields, **conditions):
    """
    Build a database query

    Args:
        table: Table name
        *fields: Fields to select
        **conditions: WHERE conditions
    """
    # Build SELECT clause
    if fields:
        select_clause = ", ".join(fields)
    else:
        select_clause = "*"

    # Build WHERE clause
    where_clauses = []
    for column, value in conditions.items():
        if isinstance(value, str):
            where_clauses.append(f"{column} = '{value}'")
        else:
            where_clauses.append(f"{column} = {value}")

    # Construct query
    query = f"SELECT {select_clause} FROM {table}"
    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)

    print("Generated SQL Query:")
    print(query)
    return query


# Different query examples
build_query("users", "name", "email", "age", status="active", age=25)
print()
build_query("products", price=100, category="Electronics")

# ═══════════════════════════════════════════════════════════════════════════
# 8. VARIABLE SCOPE
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("8. VARIABLE SCOPE")
print("=" * 70)

print("""
Scope determines where a variable can be accessed.

Types of scope:
1. Local scope: Variables inside a function
2. Global scope: Variables outside all functions
""")

# Global vs Local scope
print("📌 Global vs Local Scope:\n")

# Global variable
global_var = "I'm global"


def demo_scope():
    """Demonstrate variable scope"""
    # Local variable
    local_var = "I'm local"
    print(f"Inside function:")
    print(f"  Local: {local_var}")
    print(f"  Global: {global_var}")


demo_scope()
print(f"\nOutside function:")
print(f"  Global: {global_var}")
# print(f"  Local: {local_var}")  # Would cause error!

# Modifying global variables
print("\n📌 Modifying Global Variables:\n")

counter = 0


def increment():
    """Increment global counter"""
    global counter  # Declare we're using global variable
    counter += 1
    print(f"Counter: {counter}")


increment()
increment()
increment()
print(f"Final counter: {counter}")

# ⚠️ Best practice: Avoid modifying global variables
print("\n💡 Best Practice: Return values instead of modifying globals\n")


def increment_better(count):
    """Better way: return new value"""
    return count + 1


my_counter = 0
my_counter = increment_better(my_counter)
my_counter = increment_better(my_counter)
my_counter = increment_better(my_counter)
print(f"Counter (better way): {my_counter}")

# ═══════════════════════════════════════════════════════════════════════════
# 9. DOCSTRINGS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("9. DOCSTRINGS - DOCUMENTING FUNCTIONS")
print("=" * 70)

print("""
Docstrings are string literals that document what a function does.
They appear right after the function definition.

Access docstring with: function_name.__doc__
""")

# Well-documented function
print("📌 Example of Well-Documented Function:\n")


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    BMI is calculated as weight (kg) divided by height (meters) squared.

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: Calculated BMI value

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


# Access docstring
print(calculate_bmi.__doc__)

# Use the function
result = calculate_bmi(70, 1.75)
print(f"\nBMI for 70kg, 1.75m: {result}")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: Temperature Converter
---------------------------------
Create a function that converts Celsius to Fahrenheit.
Formula: F = (C * 9/5) + 32
Test with: 0, 25, 100

Exercise 2: Even or Odd
-----------------------
Create a function that returns True if number is even, False if odd.
Test with: 10, 15, 22, 37

Exercise 3: Find Maximum
------------------------
Create a function that takes multiple numbers (*args) and returns the maximum.
Don't use the built-in max() function.
Test with: (5, 2, 9, 1, 7)

Exercise 4: Area Calculator
---------------------------
Create a function that calculates area of different shapes:
- Circle: π * r²
- Rectangle: length * width
- Triangle: (base * height) / 2

Use default parameters or **kwargs for flexibility.

Exercise 5: String Reverser
---------------------------
Create a function that reverses a string without using [::-1].
Test with: "Python", "Hello World"

Exercise 6: Palindrome Checker
------------------------------
Create a function that checks if a string is a palindrome.
(Reads the same forwards and backwards)
Test with: "racecar", "hello", "madam"

Exercise 7: Factorial Calculator
--------------------------------
Create a recursive function to calculate factorial.
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

Exercise 8: Grade Statistics
----------------------------
Create a function that takes multiple grades (*args) and returns:
- Average grade
- Highest grade
- Lowest grade
- Number of passing grades (>= 60)

Test with: (85, 92, 78, 65, 90, 55, 88)

Exercise 9: Shopping Cart
-------------------------
Create a shopping cart system with functions:
- add_item(name, price, quantity)
- calculate_total()
- apply_discount(percent)
- display_receipt()

Exercise 10: User Profile
-------------------------
Create a function that builds a user profile using **kwargs.
Required: name, email
Optional: age, phone, address, city, country

Display all provided information nicely formatted.

Bonus Exercise: Password Strength Checker
-----------------------------------------
Create a function that checks password strength:
- Returns strength level: Weak, Medium, Strong, Very Strong
- Criteria:
  * Length (min 8 chars)
  * Contains uppercase letter
  * Contains lowercase letter
  * Contains number
  * Contains special character (!@#$%^&*)

Test various passwords and explain the strength level.
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 7")
print("=" * 70)
print("\nCongratulations! You've completed the Python Fundamentals course!")
print("Keep practicing and happy coding! 🚀")
