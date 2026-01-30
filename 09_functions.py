# ============================================
# FUNCTIONS
# ============================================

# --------------------------------------------
# WHAT ARE FUNCTIONS?
# --------------------------------------------

# A function is a reusable block of code that performs a specific task
# Think of it like a recipe - write once, use many times

# Why use functions?
# 1. Avoid repeating code
# 2. Organize code into logical pieces
# 3. Make code easier to test and fix
# 4. Make code easier to understand

# --------------------------------------------
# BUILT-IN FUNCTIONS
# --------------------------------------------

# Python comes with many ready-to-use functions

# print() - displays output
print("Hello!")

# len() - gets length of strings, lists, etc.
length = len("Python")
print(length)  # 6

# sum() - adds numbers in a list
total = sum([1, 2, 3, 4])
print(total)  # 10

# type() - tells you what type something is
print(type(42))      # <class 'int'>
print(type("hello"))  # <class 'str'>

# input() - gets user input (returns a string)
# name = input("What's your name? ")
# print(f"Hello, {name}!")

# --------------------------------------------
# CREATING YOUR OWN FUNCTIONS
# --------------------------------------------

# Basic syntax:


def function_name():
    # Code goes here
    print("This is a function")


# Call the function to use it:
function_name()

# Example 1: Simple greeting


def greet():
    print("Hello!")
    print("Welcome to Python!")


greet()  # Calls the function
# Output:
# Hello!
# Welcome to Python!

# Example 2: Multiple uses


def say_hello():
    print("Hello!")


say_hello()  # Hello!
say_hello()  # Hello!
say_hello()  # Hello!

# --------------------------------------------
# FUNCTIONS WITH PARAMETERS
# --------------------------------------------

# Parameters let you pass information into a function
# Think of parameters as inputs to your recipe


def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")


greet("Alice")  # "Alice" is an argument
greet("Bob")    # "Bob" is an argument

# Parameter vs Argument:
# - Parameter: variable in the function definition
# - Argument: actual value you pass when calling

# Multiple parameters:


def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


add(5, 3)   # 5 + 3 = 8
add(10, 7)  # 10 + 7 = 17

# Example: Personalized message


def welcome_user(name, age):
    print(f"Welcome, {name}!")
    print(f"You are {age} years old.")


welcome_user("Sarah", 25)
welcome_user("Mike", 30)

# --------------------------------------------
# RETURN STATEMENT
# --------------------------------------------

# RETURN sends a value back from the function
# After return, the function stops


def add(a, b):
    return a + b


result = add(5, 3)
print(result)  # 8

# Without return, function returns None:


def greet(name):
    print(f"Hello, {name}!")


result = greet("Alice")
print(result)  # None

# With return:


def greet(name):
    return f"Hello, {name}!"


message = greet("Alice")
print(message)  # Hello, Alice!

# Multiple return values (using a tuple):


def get_user_info():
    name = "Alice"
    age = 25
    return name, age


user_name, user_age = get_user_info()
print(user_name)  # Alice
print(user_age)   # 25

# --------------------------------------------
# DEFAULT ARGUMENTS
# --------------------------------------------

# Give parameters default values


def greet(name="Guest"):  # Default value is "Guest"
    print(f"Hello, {name}!")


greet()         # Uses default: Hello, Guest!
greet("Alice")  # Uses provided value: Hello, Alice!

# More examples:


def calculate_price(price, tax_rate=0.08):
    total = price + (price * tax_rate)
    return total


print(calculate_price(100))      # 108.0 (uses default 8% tax)
print(calculate_price(100, 0.10))  # 110.0 (uses 10% tax)

# --------------------------------------------
# KEYWORD ARGUMENTS
# --------------------------------------------

# Specify which parameter gets which value


def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


# Positional arguments (order matters):
describe_person("Alice", 25, "New York")

# Keyword arguments (order doesn't matter):
describe_person(age=25, city="New York", name="Alice")
describe_person(city="Boston", name="Bob", age=30)

# Mix positional and keyword (positional must come first):
describe_person("Charlie", age=35, city="Chicago")

# --------------------------------------------
# *ARGS (VARIABLE NUMBER OF ARGUMENTS)
# --------------------------------------------

# *args lets you pass any number of arguments


def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add_all(1, 2, 3))           # 6
print(add_all(10, 20, 30, 40))    # 100
print(add_all(5))                  # 5

# How it works:
# *numbers collects all arguments into a tuple
# You can then loop through them

# Another example:


def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")


greet_all("Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Calculate total with tip


def calculate_total(bill_amount, tip_percent=15):
    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    return total


meal_cost = 50
final_total = calculate_total(meal_cost)
print(f"Total with 15% tip: ${final_total}")  # $57.50

custom_total = calculate_total(meal_cost, 20)
print(f"Total with 20% tip: ${custom_total}")  # $60.00

# Example 2: Validate email


def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False


print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))      # False

# Example 3: Calculate discount


def calculate_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price, discount


original = 100
new_price, saved = calculate_discount(original, 25)
print(f"Original: ${original}")
print(f"You save: ${saved}")
print(f"You pay: ${new_price}")

# Example 4: Temperature converter


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

# Example 5: Grade calculator


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


student_score = 85
grade = calculate_grade(student_score)
print(f"Score: {student_score} = Grade: {grade}")

# Example 6: Shopping cart


def calculate_cart_total(*prices):
    subtotal = sum(prices)
    tax = subtotal * 0.08
    total = subtotal + tax
    return total


order_total = calculate_cart_total(19.99, 29.99, 9.99)
print(f"Order total: ${order_total:.2f}")

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Create a simple function
# Write a function called "say_goodbye" that displays "Goodbye!"
# Call it 3 times


# Exercise 2: Function with one parameter
# Write a function called "square" that:
# - Takes one number as input
# - Returns the number squared
# Test it with different numbers


# Exercise 3: Function with multiple parameters
# Write a function called "full_name" that:
# - Takes first_name and last_name as parameters
# - Returns them combined with a space
# Test: full_name("John", "Smith") should return "John Smith"


# Exercise 4: Function with return value
# Write a function called "multiply" that:
# - Takes two numbers as parameters
# - Returns their product
# Store the result and display it


# Exercise 5: Default arguments
# Write a function called "greet_user" that:
# - Takes a name parameter with default value "Guest"
# - Returns a greeting message
# Test it with and without providing a name


# Exercise 6: Calculate area
# Write a function called "rectangle_area" that:
# - Takes length and width as parameters
# - Returns the area (length × width)
# Test with different rectangles


# Exercise 7: Temperature check
# Write a function called "check_temperature" that:
# - Takes temperature as parameter
# - Returns "Hot" if temp > 80
# - Returns "Comfortable" if temp 60-80
# - Returns "Cold" if temp < 60


# Exercise 8: Shopping discount
# Write a function called "apply_discount" that:
# - Takes price and discount_percent as parameters
# - Returns the discounted price
# Test: apply_discount(100, 20) should return 80


# Exercise 9: Multiple returns
# Write a function called "min_max" that:
# - Takes three numbers as parameters
# - Returns both the smallest and largest
# Example: min_max(5, 2, 8) returns 2, 8


# Exercise 10: Flexible sum
# Write a function called "sum_all" that:
# - Uses *args to accept any number of values
# - Returns their sum
# Test with different amounts of numbers


# Exercise 11: Password strength
# Write a function called "check_password_strength" that:
# - Takes a password as parameter
# - Returns "Strong" if length >= 12
# - Returns "Medium" if length >= 8
# - Returns "Weak" if length < 8


# Exercise 12: BMI calculator
# Write a function called "calculate_bmi" that:
# - Takes weight (kg) and height (m) as parameters
# - Returns the BMI (weight / height²)
# Also create a function "bmi_category" that:
# - Takes BMI value
# - Returns the category (Underweight, Normal, Overweight)
