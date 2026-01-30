"""
═══════════════════════════════════════════════════════════════════════════
PYTHON FUNDAMENTALS - MODULE 3: WORKING WITH STRINGS
═══════════════════════════════════════════════════════════════════════════

What you will learn in this module:
✓ String basics and creation
✓ String indexing and slicing
✓ Escape characters
✓ String concatenation and formatting
✓ Common string methods
✓ String operations and membership

Goal: Master string manipulation in Python
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. STRING BASICS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("1. STRING BASICS")
print("=" * 70)

print("""
A string is a sequence of characters enclosed in quotes.
Strings are immutable (cannot be changed after creation).
""")

# Creating strings
single_quote = 'Hello World'
double_quote = "Hello World"
multi_line = '''This is a
multi-line
string'''

print("📌 Creating Strings:")
print(f"   Single quotes: {single_quote}")
print(f"   Double quotes: {double_quote}")
print(f"   Multi-line:")
print(f"   {multi_line}")

# String length
course = "Python Programming"
print(f"\n📌 String Length:")
print(f"   String: '{course}'")
print(f"   Length: {len(course)} characters")

# ═══════════════════════════════════════════════════════════════════════════
# 2. STRING INDEXING
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. STRING INDEXING")
print("=" * 70)

course = "Python"
print(f"\nString: '{course}'")
print("\nPositive Indexing (left to right):")
print("   P  y  t  h  o  n")
print("   0  1  2  3  4  5")

print("\nNegative Indexing (right to left):")
print("   P  y  t  h  o  n")
print("  -6 -5 -4 -3 -2 -1")

print("\n📌 Accessing Characters:")
print(f"   course[0] = '{course[0]}'  (first character)")
print(f"   course[2] = '{course[2]}'  (third character)")
print(f"   course[-1] = '{course[-1]}' (last character)")
print(f"   course[-2] = '{course[-2]}' (second to last)")

# 🌍 REAL-WORLD EXAMPLE: Email Validation
print("\n🌍 Real-World Example: Email Domain Extraction")
print("-" * 70)

email = "user@company.com"
print(f"Email: {email}")
print(f"First character: {email[0]}")
print(f"@ symbol position: {email[4]}")
print(f"Last character: {email[-1]}")

# ═══════════════════════════════════════════════════════════════════════════
# 3. STRING SLICING
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. STRING SLICING")
print("=" * 70)

print("""
Slicing allows you to extract a portion of a string.
Syntax: string[start:end:step]
- start: beginning index (inclusive)
- end: ending index (exclusive)
- step: increment (default is 1)
""")

course = "Python Programming"
print(f"String: '{course}'")
print(f"Length: {len(course)}")

print("\n📌 Basic Slicing:")
print(f"   course[0:6] = '{course[0:6]}'  (characters 0-5)")
print(f"   course[7:18] = '{course[7:18]}' (characters 7-17)")

print("\n📌 Slicing Shortcuts:")
print(f"   course[:6] = '{course[:6]}'    (start to index 6)")
print(f"   course[7:] = '{course[7:]}'  (index 7 to end)")
print(f"   course[:] = '{course[:]}'   (entire string)")

print("\n📌 Negative Indexing in Slicing:")
print(f"   course[-11:] = '{course[-11:]}'  (last 11 characters)")
print(f"   course[:-11] = '{course[:-11]}'       (all except last 11)")

print("\n📌 Step Parameter:")
print(f"   course[::2] = '{course[::2]}'  (every 2nd character)")
print(f"   course[::-1] = '{course[::-1]}'  (reverse string)")

# 🌍 REAL-WORLD EXAMPLE: Credit Card Masking
print("\n🌍 Real-World Example: Credit Card Number Masking")
print("-" * 70)

credit_card = "1234567890123456"
print(f"Original: {credit_card}")

# Show only last 4 digits
masked = "**** **** **** " + credit_card[-4:]
print(f"Masked: {masked}")

# Extract parts
first_four = credit_card[:4]
last_four = credit_card[-4:]
print(f"First 4 digits: {first_four}")
print(f"Last 4 digits: {last_four}")

# ═══════════════════════════════════════════════════════════════════════════
# 4. ESCAPE CHARACTERS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. ESCAPE CHARACTERS")
print("=" * 70)

print("""
Escape characters are special characters preceded by a backslash (\\).
They represent characters that are difficult to type or have special meaning.
""")

print("📌 Common Escape Characters:\n")

# New line
print("1. \\n (New line):")
print("   Hello\\nWorld becomes:")
print("   Hello\nWorld")

# Tab
print("\n2. \\t (Tab):")
print("   Name\\tAge becomes:")
print("   Name\tAge")

# Backslash
print("\n3. \\\\ (Backslash):")
print("   C:\\\\Users\\\\Documents becomes:")
print("   C:\\Users\\Documents")

# Quotes
print("\n4. \\' and \\\" (Quotes):")
quote = "He said, \"Hello!\""
print(f"   {quote}")

name = 'It\'s a beautiful day'
print(f"   {name}")

# 🌍 REAL-WORLD EXAMPLE: Receipt Printer
print("\n🌍 Real-World Example: Receipt Generator")
print("-" * 70)

receipt = """
╔══════════════════════════════╗
║      PYTHON STORE            ║
║      Receipt #12345          ║
╠══════════════════════════════╣
║ Item\t\tPrice   ║
║ Laptop\t\t$999.99 ║
║ Mouse\t\t$29.99  ║
║ Keyboard\t$79.99  ║
╠══════════════════════════════╣
║ Total:\t\t$1109.97║
╚══════════════════════════════╝
"""
print(receipt)

# ═══════════════════════════════════════════════════════════════════════════
# 5. STRING CONCATENATION
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. STRING CONCATENATION")
print("=" * 70)

first_name = "John"
last_name = "Smith"

print("📌 Using + Operator:")
full_name = first_name + " " + last_name
print(f"   first_name + ' ' + last_name = '{full_name}'")

print("\n📌 Repeating Strings:")
print(f"   'Python' * 3 = '{'Python' * 3}'")
print(f"   '-' * 20 = '{'-' * 20}'")

# ⚠️ Concatenation limitations
print("\n⚠️ Cannot concatenate string with numbers directly:")
print("   age = 25")
print("   'Age: ' + age  # ❌ TypeError")
print("   'Age: ' + str(age)  # ✅ Works")

age = 25
message = "Age: " + str(age)
print(f"   Result: '{message}'")

# ═══════════════════════════════════════════════════════════════════════════
# 6. STRING FORMATTING
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("6. STRING FORMATTING (F-STRINGS)")
print("=" * 70)

print("""
F-strings (formatted string literals) provide a clean way to embed
expressions and variables directly into strings.
""")

first_name = "Alice"
last_name = "Johnson"
age = 28
balance = 1234.56

print("📌 Basic F-String:")
message = f"My name is {first_name} {last_name}"
print(f"   {message}")

print("\n📌 Expressions in F-Strings:")
print(f"   In 5 years, I'll be {age + 5} years old")
print(f"   My name has {len(first_name)} letters")

print("\n📌 Number Formatting:")
print(f"   Balance: ${balance:.2f}  (2 decimal places)")
print(f"   Balance: ${balance:,.2f}  (with thousands separator)")

large_number = 1000000
print(f"   Large number: {large_number:,}  (formatted)")

print("\n📌 Alignment and Padding:")
print(f"   {'Left':<10}|  (left-aligned, width 10)")
print(f"   {'Center':^10}|  (centered, width 10)")
print(f"   {'Right':>10}|  (right-aligned, width 10)")

# 🌍 REAL-WORLD EXAMPLE: Invoice Generator
print("\n🌍 Real-World Example: Professional Invoice")
print("-" * 70)

company_name = "Tech Solutions Inc."
invoice_number = 12345
customer_name = "John Doe"
date = "2024-01-30"

items = [
    ("Web Development", 2500.00),
    ("SEO Optimization", 750.00),
    ("Hosting (1 year)", 120.00)
]

print(f"""
{'=' * 50}
           {company_name}
{'=' * 50}
Invoice #: {invoice_number}
Date: {date}
Customer: {customer_name}
{'=' * 50}

{'Description':<30} {'Amount':>15}
{'-' * 50}
""")

subtotal = 0
for description, amount in items:
    print(f"{description:<30} ${amount:>14.2f}")
    subtotal += amount

tax = subtotal * 0.08
total = subtotal + tax

print(f"""{'-' * 50}
{'Subtotal:':<30} ${subtotal:>14.2f}
{'Tax (8%):':<30} ${tax:>14.2f}
{'=' * 50}
{'TOTAL:':<30} ${total:>14.2f}
{'=' * 50}
""")

# ═══════════════════════════════════════════════════════════════════════════
# 7. STRING METHODS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("7. COMMON STRING METHODS")
print("=" * 70)

course = "  Python Programming  "
print(f"Original string: '{course}'")

print("\n📌 Case Conversion Methods:")
print(f"   upper(): '{course.upper()}'")
print(f"   lower(): '{course.lower()}'")
print(f"   title(): '{course.title()}'")
print(f"   capitalize(): '{course.capitalize()}'")

print("\n📌 Whitespace Removal Methods:")
print(f"   strip(): '{course.strip()}'  (both ends)")
print(f"   lstrip(): '{course.lstrip()}'  (left side)")
print(f"   rstrip(): '{course.rstrip()}'  (right side)")

text = "Python Programming"
print(f"\nWorking with: '{text}'")

print("\n📌 Search Methods:")
print(f"   find('Programming'): {text.find('Programming')}")
print(f"   find('Java'): {text.find('Java')}")  # Returns -1 if not found
print(f"   index('gram'): {text.index('gram')}")  # Raises error if not found

print("\n📌 Replace Method:")
print(f"   replace('Python', 'Java'): '{text.replace('Python', 'Java')}'")
print(f"   replace('m', 'M'): '{text.replace('m', 'M')}'")

print("\n📌 Boolean Methods:")
email = "user@example.com"
print(f"String: '{email}'")
print(f"   startswith('user'): {email.startswith('user')}")
print(f"   endswith('.com'): {email.endswith('.com')}")
print(f"   isalpha(): {email.isalpha()}")
print(f"   isdigit(): {'12345'.isdigit()}")
print(f"   isalnum(): {'Python3'.isalnum()}")

print("\n📌 Split and Join:")
sentence = "Python is awesome"
words = sentence.split()
print(f"   split(): {words}")

joined = "-".join(words)
print(f"   join(): '{joined}'")

# 🌍 REAL-WORLD EXAMPLE: Text Processing
print("\n🌍 Real-World Example: User Registration Form Processing")
print("-" * 70)


def process_registration(username, email, password):
    """Process and validate user registration data"""
    # Clean up input
    username = username.strip().lower()
    email = email.strip().lower()

    print(f"Processing registration for: {username}")

    # Validate username
    if not username or len(username) < 3:
        print("   ❌ Username must be at least 3 characters")
        return False

    if not username.isalnum():
        print("   ❌ Username must contain only letters and numbers")
        return False

    # Validate email
    if not email or '@' not in email:
        print("   ❌ Invalid email address")
        return False

    if not email.endswith(('.com', '.org', '.net')):
        print("   ❌ Email must end with .com, .org, or .net")
        return False

    # Validate password
    if len(password) < 8:
        print("   ❌ Password must be at least 8 characters")
        return False

    print("   ✅ Registration successful!")
    print(f"   Username: {username}")
    print(f"   Email: {email}")
    return True


# Test cases
print("\nTest Case 1:")
process_registration("  JohnDoe  ", "  JOHN@EMAIL.COM  ", "SecurePass123")

print("\nTest Case 2:")
process_registration("ab", "invalidemail", "short")

# ═══════════════════════════════════════════════════════════════════════════
# 8. MEMBERSHIP OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("8. MEMBERSHIP OPERATORS (in, not in)")
print("=" * 70)

course = "Python Programming"

print(f"String: '{course}'")
print("\n📌 'in' operator (checks if substring exists):")
print(f"   'Python' in course: {'Python' in course}")
print(f"   'Java' in course: {'Java' in course}")

print("\n📌 'not in' operator (checks if substring doesn't exist):")
print(f"   'Ruby' not in course: {'Ruby' not in course}")
print(f"   'Programming' not in course: {'Programming' not in course}")

# Case sensitivity
print("\n⚠️ Note: Operators are case-sensitive:")
print(f"   'python' in course: {'python' in course}")
print(f"   'Python' in course: {'Python' in course}")

# 🌍 REAL-WORLD EXAMPLE: Content Moderation
print("\n🌍 Real-World Example: Comment Moderation System")
print("-" * 70)

BANNED_WORDS = ['spam', 'fake', 'scam', 'virus']


def moderate_comment(comment):
    """Check if comment contains banned words"""
    comment_lower = comment.lower()

    print(f"Checking comment: '{comment}'")

    for word in BANNED_WORDS:
        if word in comment_lower:
            print(f"   ❌ Comment rejected! Contains banned word: '{word}'")
            return False

    print("   ✅ Comment approved!")
    return True


# Test comments
print("\nTest 1:")
moderate_comment("This is a great product!")

print("\nTest 2:")
moderate_comment("Click here for a FREE prize! No spam!")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📝 PRACTICE EXERCISES")
print("=" * 70)

print("""
Exercise 1: String Indexing and Slicing
---------------------------------------
Given: text = "Python Programming"
a) Get the first character
b) Get the last character
c) Get "Python"
d) Get "Programming"
e) Reverse the entire string

Exercise 2: String Methods
--------------------------
Given: email = "  USER@EXAMPLE.COM  "
a) Remove whitespace and convert to lowercase
b) Check if it contains "@"
c) Split the email at "@" to get username and domain
d) Check if domain ends with ".com"

Exercise 3: F-String Formatting
-------------------------------
Create a product display with the following information:
- Product: "Laptop"
- Price: 1299.99
- Stock: 5
- On sale: True

Format it as:
Product: Laptop
Price: $1,299.99
Stock: 5 units
Status: ON SALE (if on_sale is True, otherwise "Regular Price")

Exercise 4: Text Processing
---------------------------
Write a function that takes a full name and returns:
- First name
- Last name
- Initials (e.g., "John Doe" → "J.D.")
- Name length (excluding spaces)

Exercise 5: Password Validator
------------------------------
Create a function that validates passwords with these rules:
- At least 8 characters long
- Contains at least one number
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- No spaces allowed

Test with:
- "password123"
- "Password123"
- "Pass 123"
- "SHORT1"

Exercise 6: Real-World Application
----------------------------------
Create a simple URL parser that extracts:
- Protocol (http/https)
- Domain name
- Path

Example:
Input: "https://www.example.com/products/laptop"
Output:
  Protocol: https
  Domain: www.example.com
  Path: /products/laptop

Bonus Exercise: Text Analyzer
-----------------------------
Create a function that analyzes a paragraph and returns:
- Total character count
- Total word count
- Average word length
- Most common word (simple version - split and count)

Test with: "Python is awesome. Python is powerful. Python is easy."
""")

print("\n" + "=" * 70)
print("🎯 END OF MODULE 3")
print("=" * 70)
print("\nNext Module: Operators")
print("Keep practicing and happy coding! 🚀")
