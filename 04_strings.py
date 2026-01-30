# ============================================
# STRINGS (TEXT)
# ============================================

# --------------------------------------------
# WHAT ARE STRINGS?
# --------------------------------------------

# Strings are text data.
# Anything inside quotes is a string.

name = "Alice"           # This is a string
message = 'Hello!'       # Single or double quotes both work
course = "Python 101"    # Can include letters, numbers, and spaces

# --------------------------------------------
# STRING LENGTH
# --------------------------------------------

course = "coding 101"
print(len(course))  # Displays: 10 (counts all characters including space)

# len() tells you how many characters are in a string

# --------------------------------------------
# ACCESSING CHARACTERS (INDEXING)
# --------------------------------------------

# Each character in a string has a position (index)
# Positions start at 0, not 1!

#   c  o  d  i  n  g     1  0  1
#   0  1  2  3  4  5  6  7  8  9

course = "coding 101"

print(course[0])   # First character: c
print(course[1])   # Second character: o
print(course[7])   # Eighth character: 1

# Negative indexing (counting from the end):
print(course[-1])  # Last character: 1
print(course[-2])  # Second to last: 0

# --------------------------------------------
# SLICING (GETTING PARTS OF STRINGS)
# --------------------------------------------

# Syntax: string[start:end]
# Gets characters from start up to (but not including) end

course = "coding 101"

print(course[0:6])   # "coding" (positions 0 to 5)
print(course[:6])    # "coding" (same as above, start assumed to be 0)
print(course[7:])    # "101" (position 7 to the end)
print(course[:])     # "coding 101" (everything)

# Real-world example:
email = "alice@email.com"
username = email[:5]  # Gets "alice"
domain = email[6:]    # Gets "email.com"
print(username)  # alice
print(domain)    # email.com

# --------------------------------------------
# ESCAPE CHARACTERS
# --------------------------------------------

# Use backslash (\) to include special characters

# Include quotes inside strings:
message = "She said \"Hello!\""  # She said "Hello!"
print(message)

# Common escape characters:
# \n  = new line
# \"  = double quote
# \'  = single quote
# \\  = backslash itself

text = "Line 1\nLine 2"
print(text)
# Output:
# Line 1
# Line 2

# --------------------------------------------
# STRING CONCATENATION (COMBINING)
# --------------------------------------------

first = "John"
last = "Smith"

# Using + to combine strings:
full_name = first + " " + last
print(full_name)  # John Smith

# Real-world example:
greeting = "Hello, "
name = "Alice"
message = greeting + name + "!"
print(message)  # Hello, Alice!

# --------------------------------------------
# F-STRINGS (FORMATTED STRINGS)
# --------------------------------------------

# F-strings let you put variables directly inside strings
# Put 'f' before the quote and use {} for variables

first_name = "Sarah"
age = 25

# With f-string:
message = f"My name is {first_name} and I am {age} years old."
print(message)  # My name is Sarah and I am 25 years old.

# Without f-string (harder to read):
message = "My name is " + first_name + " and I am " + str(age) + " years old."

# More examples:
price = 19.99
item = "book"
print(f"The {item} costs ${price}")  # The book costs $19.99

# You can even do calculations inside {}:
quantity = 3
print(f"Total: ${price * quantity}")  # Total: $59.97

# --------------------------------------------
# STRING METHODS
# --------------------------------------------

course = "  coding 101  "

# .upper() - make all letters UPPERCASE
print(course.upper())  # "  CODING 101  "

# .lower() - make all letters lowercase
print(course.lower())  # "  coding 101  "

# .title() - capitalize first letter of each word
print(course.title())  # "  Coding 101  "

# .strip() - remove spaces from beginning and end
print(course.strip())  # "coding 101"

# .find() - find the position of text
position = course.find("101")
print(position)  # 9 (position where "101" starts)

# .replace() - replace text
new_course = course.replace("101", "102")
print(new_course)  # "  coding 102  "

# Check if text is in string:
print("coding" in course)      # True
print("python" in course)      # False
print("Swift" not in course)   # True

# --------------------------------------------
# REAL-WORLD EXAMPLES
# --------------------------------------------

# Example 1: Create a personalized email
customer_name = "Emily"
order_number = "12345"
total = 89.99

email_body = f"""
Hello {customer_name},

Your order #{order_number} has been confirmed.
Total amount: ${total}

Thank you for your purchase!
"""
print(email_body)

# Example 2: Process user input
website = "  WWW.EXAMPLE.COM  "
cleaned = website.strip().lower()
print(cleaned)  # www.example.com

# Example 3: Extract information
full_name = "Dr. Jane Smith"
has_title = "Dr." in full_name
print(has_title)  # True

# Example 4: Format phone number
phone = "1234567890"
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(formatted)  # (123) 456-7890

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: String basics
# Create a variable with your favorite movie title.
# Display its length.
# Display the first character.
# Display the last character.


# Exercise 2: Slicing
# Create a variable: sentence = "Python is awesome"
# Extract and display:
# - The word "Python"
# - The word "awesome"
# - The first 6 characters


# Exercise 3: F-strings
# Create variables for:
# - Your name
# - Your city
# - Your age
# Use an f-string to display: "I am [name], [age] years old, from [city]"


# Exercise 4: String methods
# Create a variable: text = "  HELLO world  "
# Use methods to:
# 1. Remove the spaces
# 2. Make it all lowercase
# 3. Replace "world" with "Python"
# 4. Display the result


# Exercise 5: Real-world scenario
# You work at a bookstore.
# Create variables for:
# - Book title
# - Author name
# - Price
# Use f-strings to create a display message like:
# "Title: [book] by [author] - $[price]"
