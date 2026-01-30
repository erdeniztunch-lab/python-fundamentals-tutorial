# Python for Complete Beginners 🐍

Welcome! This repository contains short lessons and exercises for people new to programming. The files are small, focused, and ready to run.

---

## Quick start ✅

1. Install Python 3.10+ (project tested with Python 3.13.7).
2. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. (Optional) Install linting/formatting tools:

```powershell
pip install --upgrade pip
pip install flake8 black pylint
```

---

## What You'll Learn

- How Python works
- Variables and data types
- Working with text and numbers
- Making decisions with if/else
- Repeating code with loops
- Creating reusable functions

## How to Use This Guide

### Files in Order

Work through the files in this order:

0. **00_terminal_basics.py** - Terminal basics: running Python and using the shell
1. **01_what_is_python.py** - What Python is and how it works
2. **02_expressions_and_statements.py** - Expressions and statements
3. **03_variables.py** - Variables and basic types
4. **04_strings.py** - Working with text and string methods
5. **05_numbers_and_arithmetic.py** - Numbers and arithmetic operations
6. **06_comparisons_and_logic.py** - Comparison and logical operators
7. **07_conditional_statements.py** - if / elif / else usage
8. **08_loops.py** - for and while loops
9. **09_functions.py** - Defining and using functions
10. **10_code_quality_and_linting.py** - Code style, linting, and formatting tips

### How to Read the Files

Each file contains:
- **Clear explanations** in comments (lines starting with #)
- **Working examples** you can run
- **Real-world examples** to show practical uses
- **Practice exercises** at the end

### How to Run the Code

#### Method 1: Run Entire File
```bash
# Open your terminal/command prompt
# Navigate to this folder
# Run the file:
python 01_what_is_python.py
```

#### Method 2: Try Individual Lines
1. Open Python in interactive mode:
   ```bash
   python
   ```
2. Type code line by line and press Enter
3. Type `exit()` to quit

#### Method 3: Use an IDE
- Open the file in VS Code, PyCharm, or similar
- Click the "Run" button
- The output appears in the terminal panel

## Practice Tips

1. **Read the explanations** - Don't skip the comments!
2. **Run the examples** - See what they do
3. **Do the exercises** - This is how you learn
4. **Experiment** - Change values and see what happens
5. **Make mistakes** - They help you learn

## Common Beginner Mistakes

### 1. Forgetting Indentation
```python
# ❌ WRONG
if age > 18:
print("Adult")  # Needs to be indented!

# ✅ CORRECT
if age > 18:
    print("Adult")  # Indented with 4 spaces
```

### 2. Using Single = Instead of Double ==
```python
# ❌ WRONG
if age = 18:  # This is assignment, not comparison!

# ✅ CORRECT
if age == 18:  # This checks if equal
```

### 3. Forgetting Quotes on Strings
```python
# ❌ WRONG
name = Alice  # Python thinks Alice is a variable!

# ✅ CORRECT
name = "Alice"  # Now it's text
```

### 4. Wrong Variable Names
```python
# ❌ WRONG
2name = "Bob"      # Can't start with number
first-name = "Sue" # Can't use dashes

# ✅ CORRECT
name2 = "Bob"
first_name = "Sue"
```

### 5. Mixing Up Return and Print
```python
# These are different!
def add(a, b):
    print(a + b)  # Displays but doesn't give back value

def add(a, b):
    return a + b  # Gives back value to use later
```

## Getting Help

### If You Get an Error

1. **Read the error message** - It tells you what's wrong
2. **Check the line number** - Where the error occurred
3. **Look for common mistakes** - See list above
4. **Search online** - Copy error message into Google

### Common Errors Explained

**SyntaxError**: You wrote something Python doesn't understand
- Check for missing colons (:)
- Check for mismatched quotes
- Check indentation

**NameError**: Python doesn't know that variable
- Did you define it?
- Did you spell it correctly?

**TypeError**: Using wrong type of data
- Example: Adding a number and a string

**IndentationError**: Spacing is wrong
- Use 4 spaces for each level
- Don't mix tabs and spaces

## What to Do After This Guide

Once you complete all files:

1. **Build something small**
   - Calculator
   - To-do list
   - Simple game

2. **Learn more Python**
   - Lists and dictionaries
   - File handling
   - Working with dates
   - Web scraping

3. **Practice regularly**
   - Code every day, even for 15 minutes
   - Do coding challenges on websites like:
     - HackerRank
     - CodeWars
     - LeetCode (start with easy)

4. **Build projects**
   - Start small
   - Gradually increase difficulty
   - Share your code on GitHub

## Linting & formatting (recommended) ✨

- Check style with `flake8`:

```powershell
flake8 .
```

- Run `pylint` for detailed feedback:

```powershell
pylint 01_what_is_python.py
```

- Auto-format code with `black`:

```powershell
black .
```

These tools help keep examples consistent and teach good habits.

---

## Resources

### Free Learning Resources
- Python.org official tutorial
- Codecademy Python course
- freeCodeCamp Python tutorial on YouTube
- W3Schools Python tutorial

### Communities
- Reddit: r/learnpython
- Stack Overflow (for questions)
- Python Discord servers
- Local coding meetups

## Contributing ✍️

- Found a typo or clearer wording? Send a pull request
- Add small improvements to examples or exercises
- Keep changes focused and include brief descriptions in commits

---

## Remember

- **Everyone starts as a beginner**
- **Making mistakes is part of learning**
- **Practice is more important than perfection**
- **Ask questions when you're stuck**
- **Celebrate small wins**

Good luck and enjoy learning Python! 🐍