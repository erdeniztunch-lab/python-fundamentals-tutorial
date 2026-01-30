"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 6: LOOPS
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ for loops
✓ while loops
✓ for-else and while-else
✓ Nested loops
✓ break and continue statements
✓ Iterables
✓ Range function

Goal: Master repetition and iteration in Python
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. FOR LOOPS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. FOR LOOPS")
print("=" * 70)

print("""
A for loop iterates over a sequence (list, tuple, string, or range).
It executes a block of code for each item in the sequence.

Syntax:
    for variable in sequence:
        # code block
""")

# Basic for loop with range
print("📌 Basic for Loop with range():\n")

for i in range(5):
    print(f"Iteration {i}")

print("\n💡 range(5) generates: 0, 1, 2, 3, 4")

# Different range variations
print("\n📌 Range Variations:\n")

print("range(1, 6) → starts at 1, ends before 6:")
for i in range(1, 6):
    print(i, end=" ")

print("\n\nrange(0, 10, 2) → starts at 0, ends before 10, step by 2:")
for i in range(0, 10, 2):
    print(i, end=" ")

print("\n\nrange(10, 0, -1) → counts backwards from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")

# Iterating over strings
print("\n\n📌 Iterating Over Strings:\n")

word = "Python"
for letter in word:
    print(f"Letter: {letter}")

# Iterating over lists
print("\n📌 Iterating Over Lists:\n")

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Using enumerate() for index and value
print("\n📌 Using enumerate() for Index and Value:\n")

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Start enumerate from 1
print("\nStarting enumerate from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")

# 🌍 REAL-WORLD EXAMPLE: Shopping Cart
print("\n🌍 Real-World Example: Shopping Cart Total")
print("-" * 70)

cart_items = [
    {"name": "Laptop", "price": 999.99, "quantity": 1},
    {"name": "Mouse", "price": 29.99, "quantity": 2},
    {"name": "Keyboard", "price": 79.99, "quantity": 1},
    {"name": "Monitor", "price": 299.99, "quantity": 2}
]

print("Shopping Cart:")
print("-" * 70)
print(f"{'Item':<15} {'Price':>10} {'Qty':>5} {'Total':>12}")
print("-" * 70)

total = 0
for item in cart_items:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(
        f"{item['name']:<15} ${item['price']:>9.2f} {item['quantity']:>5} ${item_total:>11.2f}")

print("-" * 70)
print(f"{'GRAND TOTAL':>33} ${total:>11.2f}")
print("-" * 70)

# ═══════════════════════════════════════════════════════════════════════════
# 2. WHILE LOOPS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. WHILE LOOPS")
print("=" * 70)

print("""
A while loop repeats as long as a condition is True.
It's useful when you don't know how many iterations you need.

Syntax:
    while condition:
        # code block
        # don't forget to update the condition!
""")

# Basic while loop
print("📌 Basic while Loop:\n")

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# User input example (simulated)
print("\n📌 While Loop with Input (Simulated):\n")


def password_check_simulation():
    """Simulate password checking"""
    correct_password = "Python123"
    attempts = 0
    max_attempts = 3

    passwords_tried = ["wrong1", "wrong2", "Python123"]  # Simulated inputs

    while attempts < max_attempts:
        # Simulate input
        user_password = passwords_tried[attempts]
        attempts += 1

        print(f"Attempt {attempts}: Trying password '{user_password}'")

        if user_password == correct_password:
            print("✅ Access granted!")
            break
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Incorrect! {remaining} attempts remaining.\n")
            else:
                print("❌ Account locked! Too many failed attempts.")


password_check_simulation()

# 🌍 REAL-WORLD EXAMPLE: ATM Withdrawal
print("\n🌍 Real-World Example: ATM Withdrawal System")
print("-" * 70)


def atm_withdrawal(balance):
    """Simulate ATM withdrawal process"""
    print(f"Initial Balance: ${balance:.2f}")
    print()

    # Simulated withdrawal attempts
    withdrawals = [100, 50, 500, 1000]

    for withdrawal in withdrawals:
        print(f"Attempting to withdraw: ${withdrawal:.2f}")

        if withdrawal <= balance:
            balance -= withdrawal
            print(f"✅ Withdrawal successful!")
            print(f"   Remaining balance: ${balance:.2f}")
        else:
            print(f"❌ Insufficient funds!")
            print(f"   Available balance: ${balance:.2f}")
        print()

        # Stop if balance is too low
        if balance < 10:
            print("⚠️ Low balance warning! Ending session.")
            break

    print(f"Final Balance: ${balance:.2f}")
    return balance


atm_withdrawal(500)

# ═══════════════════════════════════════════════════════════════════════════
# 3. FOR-ELSE AND WHILE-ELSE
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. FOR-ELSE AND WHILE-ELSE")
print("=" * 70)

print("""
The else clause in loops executes when the loop completes normally
(i.e., not terminated by a break statement).
""")

# for-else example
print("📌 for-else Example (Search):\n")

numbers = [1, 3, 5, 7, 9]
search_for = 6

print(f"Searching for {search_for} in {numbers}")

for num in numbers:
    print(f"  Checking {num}...")
    if num == search_for:
        print(f"  ✅ Found {search_for}!")
        break
else:
    print(f"  ❌ {search_for} not found in list")

# Another example with found item
print(f"\nSearching for 5 in {numbers}")

for num in numbers:
    print(f"  Checking {num}...")
    if num == 5:
        print(f"  ✅ Found 5!")
        break
else:
    print(f"  ❌ 5 not found in list")

# while-else example
print("\n📌 while-else Example:\n")


def find_first_even():
    """Find first even number"""
    numbers = [1, 3, 5, 7, 8, 9]
    index = 0

    print(f"Numbers: {numbers}")
    print("Searching for first even number...")

    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print(f"✅ Found even number: {numbers[index]} at index {index}")
            break
        index += 1
    else:
        print("❌ No even numbers found")


find_first_even()

# 🌍 REAL-WORLD EXAMPLE: Inventory Search
print("\n🌍 Real-World Example: Product Inventory Search")
print("-" * 70)


def search_product(product_id):
    """Search for product in inventory"""
    inventory = [
        {"id": 101, "name": "Laptop", "stock": 5},
        {"id": 102, "name": "Mouse", "stock": 15},
        {"id": 103, "name": "Keyboard", "stock": 8},
        {"id": 104, "name": "Monitor", "stock": 3}
    ]

    print(f"Searching for Product ID: {product_id}")

    for product in inventory:
        if product["id"] == product_id:
            print(f"✅ Product Found!")
            print(f"   Name: {product['name']}")
            print(f"   Stock: {product['stock']} units")
            if product["stock"] > 0:
                print(f"   Status: IN STOCK")
            else:
                print(f"   Status: OUT OF STOCK")
            break
    else:
        print(f"❌ Product ID {product_id} not found in inventory")


search_product(102)
print()
search_product(999)

# ═══════════════════════════════════════════════════════════════════════════
# 4. NESTED LOOPS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. NESTED LOOPS")
print("=" * 70)

print("""
Nested loops are loops inside other loops.
The inner loop completes all iterations for each iteration of the outer loop.
""")

# Basic nested loop
print("📌 Basic Nested Loop (Multiplication Table):\n")

for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{i} x {j} = {product:2}", end="  ")
    print()  # New line after inner loop

# Pattern printing
print("\n📌 Pattern Printing:\n")

# Right triangle
print("Right Triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Square
print("\nSquare (5x5):")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# 🌍 REAL-WORLD EXAMPLE: Seating Chart
print("\n🌍 Real-World Example: Theater Seating Chart")
print("-" * 70)


def display_seating_chart():
    """Display theater seating with booked seats"""
    rows = 5
    seats_per_row = 8

    # Booked seats (row, seat)
    booked = [(0, 2), (0, 3), (1, 5), (2, 1), (2, 7), (4, 4)]

    print("Theater Seating Chart")
    print("✅ = Available, ❌ = Booked\n")
    print("   ", end="")
    for seat_num in range(1, seats_per_row + 1):
        print(f"  {seat_num} ", end="")
    print()

    for row in range(rows):
        print(f"{chr(65 + row)}  ", end="")  # A, B, C, D, E
        for seat in range(seats_per_row):
            if (row, seat) in booked:
                print(" ❌ ", end="")
            else:
                print(" ✅ ", end="")
        print()


display_seating_chart()

# 🌍 REAL-WORLD EXAMPLE: Student Gradebook
print("\n🌍 Real-World Example: Class Gradebook")
print("-" * 70)

students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [
    [85, 92, 88],  # Alice's grades
    [78, 85, 90],  # Bob's grades
    [92, 88, 95]   # Charlie's grades
]

print(f"{'Student':<12}", end="")
for subject in subjects:
    print(f"{subject:>10}", end="")
print(f"{'Average':>10}")
print("-" * 52)

for i in range(len(students)):
    print(f"{students[i]:<12}", end="")
    total = 0
    for j in range(len(subjects)):
        grade = grades[i][j]
        print(f"{grade:>10}", end="")
        total += grade
    average = total / len(subjects)
    print(f"{average:>10.1f}")

# ═══════════════════════════════════════════════════════════════════════════
# 5. BREAK AND CONTINUE
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. BREAK AND CONTINUE STATEMENTS")
print("=" * 70)

print("""
break: Exits the loop immediately
continue: Skips the rest of the current iteration and moves to the next
""")

# break example
print("📌 break Example:\n")

for i in range(1, 11):
    if i == 6:
        print(f"  Found {i}! Breaking out of loop.")
        break
    print(f"  Number: {i}")

print("  Loop ended\n")

# continue example
print("📌 continue Example (Skip even numbers):\n")

for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  Odd number: {i}")

# 🌍 REAL-WORLD EXAMPLE: Form Validation
print("\n🌍 Real-World Example: Email List Validation")
print("-" * 70)

emails = [
    "user1@example.com",
    "invalid-email",
    "user2@example.com",
    "",
    "user3@example.com",
    "another@invalid",
    "user4@example.com"
]

valid_emails = []
invalid_count = 0

print("Validating email list...")
print()

for email in emails:
    # Skip empty emails
    if not email:
        print(f"  ⚠️ Skipping empty email")
        continue

    # Check basic validity
    if "@" in email and "." in email.split("@")[1]:
        valid_emails.append(email)
        print(f"  ✅ Valid: {email}")
    else:
        invalid_count += 1
        print(f"  ❌ Invalid: {email}")

        # Stop if too many invalid emails
        if invalid_count >= 3:
            print(f"\n  ⚠️ Too many invalid emails! Stopping validation.")
            break

print(f"\nValid emails found: {len(valid_emails)}")
print(f"Invalid emails found: {invalid_count}")

# ═══════════════════════════════════════════════════════════════════════════
# 6. ITERABLES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("6. ITERABLES")
print("=" * 70)

print("""
An iterable is any object that can be looped over.
Common iterables: strings, lists, tuples, dictionaries, sets, range objects
""")

# String iterable
print("📌 String (iterable):\n")

for char in "Python":
    print(f"  {char}")

# List iterable
print("\n📌 List (iterable):\n")

for item in [1, 2, 3, 4, 5]:
    print(f"  {item}")

# Tuple iterable
print("\n📌 Tuple (iterable):\n")

for item in (10, 20, 30):
    print(f"  {item}")

# Dictionary iterable
print("\n📌 Dictionary (iterable):\n")

person = {"name": "John", "age": 30, "city": "New York"}

print("Keys:")
for key in person.keys():
    print(f"  {key}")

print("\nValues:")
for value in person.values():
    print(f"  {value}")

print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 🌍 REAL-WORLD EXAMPLE: Iterating Through Data
print("\n🌍 Real-World Example: Processing Sales Data")
print("-" * 70)

sales_data = {
    "January": 25000,
    "February": 28000,
    "March": 31000,
    "April": 27000,
    "May": 33000
}

print("Monthly Sales Report")
print("-" * 40)

total_sales = 0
best_month = ""
best_sales = 0

for month, sales in sales_data.items():
    print(f"{month:<12} ${sales:>8,}")
    total_sales += sales

    if sales > best_sales:
        best_sales = sales
        best_month = month

print("-" * 40)
print(f"{'Total':<12} ${total_sales:>8,}")
print(f"\nBest Month: {best_month} (${best_sales:,})")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: Basic for Loop
--------------------------
Print numbers from 1 to 10 using a for loop.
Then print the same numbers in reverse order.

Exercise 2: Sum Calculator
--------------------------
Calculate the sum of numbers from 1 to 100 using a for loop.
Expected result: 5050

Exercise 3: Factorial Calculator
--------------------------------
Write a function to calculate factorial of a number using a while loop.
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

Exercise 4: Even Numbers
-----------------------
Print all even numbers between 1 and 20 using:
a) for loop with continue
b) for loop with if statement
c) range with step

Exercise 5: Fibonacci Sequence
------------------------------
Generate first 10 numbers of Fibonacci sequence.
(Each number is sum of previous two: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)

Exercise 6: Multiplication Table
--------------------------------
Create a complete multiplication table from 1 to 10.
Format:
1 x 1 = 1   1 x 2 = 2   ... 1 x 10 = 10
2 x 1 = 2   2 x 2 = 4   ... 2 x 10 = 20
...

Exercise 7: Prime Number Checker
--------------------------------
Write a function to check if a number is prime.
Test with: 7, 15, 23, 100

Exercise 8: Password Validator
------------------------------
Create a while loop that keeps asking for password until:
- Password is at least 8 characters
- Contains at least one number
- Contains at least one uppercase letter
Limit to 3 attempts.

Exercise 9: Number Guessing Game
--------------------------------
Create a number guessing game:
- Computer picks random number 1-100
- User has 7 attempts to guess
- Give hints: "Too high" or "Too low"
- Show number of attempts remaining

Exercise 10: Pattern Printing
-----------------------------
Create these patterns using nested loops:

a) Right triangle:
*
* *
* * *
* * * *
* * * * *

b) Inverted triangle:
* * * * *
* * * *
* * *
* *
*

c) Pyramid:
    *
   * *
  * * *
 * * * *
* * * * *

Exercise 11: List Processing
----------------------------
Given: numbers = [23, 45, 12, 67, 34, 89, 15, 78, 56]
a) Find the maximum number without using max()
b) Find the minimum number without using min()
c) Calculate the average
d) Count how many are above average

Exercise 12: String Reverser
----------------------------
Write a function that reverses a string using a for loop.
Don't use [::-1]
Test with: "Python", "Hello World"

Bonus Exercise: ATM Simulator
-----------------------------
Create a full ATM simulator with:
- Check balance
- Deposit money
- Withdraw money (check sufficient funds)
- Show transaction history
- Exit option

Use while loop for menu, for loop for transaction history.
Implement proper input validation.
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 6")
print("=" * 70)
print("\nNext Module: Functions")
print("Keep practicing and happy coding! 🚀")
