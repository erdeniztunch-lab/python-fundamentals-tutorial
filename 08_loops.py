# ============================================
# LOOPS
# ============================================

# --------------------------------------------
# WHAT ARE LOOPS?
# --------------------------------------------

# Loops repeat code multiple times
# Instead of writing the same code over and over, use a loop

# Without a loop:
print("Hello 1")
print("Hello 2")
print("Hello 3")

# With a loop:
for i in range(3):
    print(f"Hello {i + 1}")

# --------------------------------------------
# FOR LOOPS
# --------------------------------------------

# FOR loops repeat code a specific number of times

# Basic syntax:
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# How it works:
# 1. range(5) creates numbers 0 to 4
# 2. Loop runs once for each number
# 3. Variable 'i' holds the current number

# range() explained:
# range(5) → 0, 1, 2, 3, 4 (5 numbers starting from 0)
# range(1, 6) → 1, 2, 3, 4, 5 (start at 1, stop before 6)
# range(0, 10, 2) → 0, 2, 4, 6, 8 (step by 2)

# Examples:
for x in range(3):
    print("Python")
# Output:
# Python
# Python
# Python

for number in range(1, 5):
    print(f"Count: {number}")
# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4

for even in range(0, 10, 2):
    print(even)
# Output: 0, 2, 4, 6, 8

# --------------------------------------------
# FOR-ELSE
# --------------------------------------------

# ELSE runs after the loop completes normally
# (doesn't run if you use 'break' to exit early)

for i in range(3):
    print(f"Attempt {i + 1}")
else:
    print("Done!")
# Output:
# Attempt 1
# Attempt 2
# Attempt 3
# Done!

# Real-world example: Search for a number
search_for = 7
numbers = [3, 5, 7, 9, 11]

for number in numbers:
    if number == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found")

# --------------------------------------------
# BREAK AND CONTINUE
# --------------------------------------------

# BREAK exits the loop immediately

for i in range(10):
    if i == 5:
        break  # Stop when i equals 5
    print(i)
# Output: 0, 1, 2, 3, 4 (stops at 5)

# CONTINUE skips the rest of the current iteration

for i in range(5):
    if i == 2:
        continue  # Skip when i equals 2
    print(i)
# Output: 0, 1, 3, 4 (skips 2)

# Real-world example: Process until error
for attempt in range(5):
    print(f"Attempt {attempt + 1}")
    if attempt == 2:
        print("Error occurred!")
        break
else:
    print("All attempts succeeded")
# Output:
# Attempt 1
# Attempt 2
# Attempt 3
# Error occurred!

# --------------------------------------------
# ITERABLES
# --------------------------------------------

# An iterable is something you can loop through
# Lists, strings, and ranges are iterables

# Loop through a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Loop through a string:
word = "hello"
for letter in word:
    print(letter)
# Output:
# h
# e
# l
# l
# o

# Loop through a tuple:
numbers = (1, 2, 3)
for number in numbers:
    print(number)

# --------------------------------------------
# NESTED LOOPS
# --------------------------------------------

# A loop inside another loop

for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(2):
        print(f"  Inner loop: {j}")
# Output:
# Outer loop: 0
#   Inner loop: 0
#   Inner loop: 1
# Outer loop: 1
#   Inner loop: 0
#   Inner loop: 1
# Outer loop: 2
#   Inner loop: 0
#   Inner loop: 1

# Real-world example: Grocery list by category
categories = ["Fruits", "Vegetables"]
items = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Vegetables": ["Carrot", "Lettuce"]
}

for category in categories:
    print(f"\n{category}:")
    for item in items[category]:
        print(f"  - {item}")
# Output:
# Fruits:
#   - Apple
#   - Banana
#   - Orange
# Vegetables:
#   - Carrot
#   - Lettuce

# --------------------------------------------
# WHILE LOOPS
# --------------------------------------------

# WHILE loops repeat as long as a condition is True

count = 1
while count <= 5:
    print(count)
    count += 1  # Important! Update the variable
# Output: 1, 2, 3, 4, 5

# How it works:
# 1. Check if condition is True
# 2. If True, run the code
# 3. Go back to step 1
# 4. If False, exit the loop

# Warning: Make sure the condition eventually becomes False!
# Otherwise, you'll have an infinite loop

# Real-world example: Keep asking until correct
password = "secret"
attempts = 0

while attempts < 3:
    guess = input("Enter password: ")
    if guess == password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Wrong! {3 - attempts} attempts left")
else:
    print("Account locked!")

# --------------------------------------------
# FOR VS WHILE
# --------------------------------------------

# Use FOR when you know how many times to repeat:
for i in range(10):
    print(i)

# Use WHILE when you repeat until a condition changes:
number = 100
while number > 1:
    print(number)
    number = number // 2
# Output: 100, 50, 25, 12, 6, 3, 1

# --------------------------------------------
# INFINITE LOOPS (BE CAREFUL!)
# --------------------------------------------

# An infinite loop never stops
# Only use when you mean to (like for servers)

# Example (DO NOT RUN THIS):
# while True:
#     print("This runs forever!")
#     # Need a 'break' statement to exit

# Safe infinite loop with break:
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # Exit after 5 iterations

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Calculate total
prices = [10.99, 5.50, 8.00, 12.25]
total = 0

for price in prices:
    total += price

print(f"Total: ${total}")

# Example 2: Find even numbers
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")

# Example 3: Countdown timer
countdown = 10
while countdown > 0:
    print(f"Time remaining: {countdown} seconds")
    countdown -= 1
print("Time's up!")

# Example 4: User menu
while True:
    print("\nMenu:")
    print("1. Start game")
    print("2. Settings")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Starting game...")
        break
    elif choice == "2":
        print("Opening settings...")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

# Example 5: Generate multiplication table
number = 5
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")

# Example 6: Validate input
valid = False
while not valid:
    age = int(input("Enter your age (1-120): "))
    if 1 <= age <= 120:
        valid = True
        print(f"Age {age} accepted")
    else:
        print("Invalid age. Try again.")

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Basic FOR loop
# Use a loop to display numbers 1 through 10


# Exercise 2: Loop with calculations
# Use a loop to calculate and display:
# 1 squared = 1
# 2 squared = 4
# 3 squared = 9
# ... up to 10


# Exercise 3: Count even numbers
# Use a loop to count how many even numbers
# are between 1 and 20. Display the count.


# Exercise 4: Loop through a list
# Create a list of 5 of your favorite foods.
# Use a loop to display each one with a number:
# 1. Pizza
# 2. Pasta
# etc.


# Exercise 5: WHILE loop
# Create a variable: balance = 100
# Use a while loop to withdraw $15 at a time
# until balance is below $10.
# Display balance after each withdrawal.


# Exercise 6: Nested loops
# Create a simple multiplication table for 1-5.
# Display: 1×1=1, 1×2=2, etc.


# Exercise 7: Break example
# Use a loop from 1 to 100.
# Display each number.
# Stop (break) when you reach 15.


# Exercise 8: Continue example
# Use a loop from 1 to 10.
# Display each number EXCEPT 5.
# Use continue to skip 5.


# Exercise 9: Search in list
# Create a list: cities = ["Paris", "London", "Tokyo", "New York"]
# Use a loop to search for "Tokyo".
# If found, display "Found Tokyo!" and break.
# If not found, display "Tokyo not in list" (use for-else).


# Exercise 10: Sum of numbers
# Ask the user to enter numbers (you can simulate this with a list).
# Keep adding the numbers until total reaches 100 or more.
# Display how many numbers were added and the final total.


# Exercise 11: Password validator
# Create a simple password checker.
# Give the user 3 attempts to enter the correct password.
# Use a loop that breaks when password is correct
# or runs out of attempts.


# Exercise 12: Pattern maker
# Use nested loops to create this pattern:
# *
# **
# ***
# ****
# *****
