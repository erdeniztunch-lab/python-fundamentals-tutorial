# ============================================
# TERMINAL / COMMAND LINE BASICS
# ============================================

# --------------------------------------------
# WHAT IS THE TERMINAL?
# --------------------------------------------

# The terminal (also called command line, command prompt, or shell)
# is a text-based way to control your computer.
# Instead of clicking icons, you type commands.

# Why learn it?
# - Run Python programs
# - Install packages
# - Navigate files and folders
# - Use programming tools

# --------------------------------------------
# OPENING THE TERMINAL
# --------------------------------------------

# Windows:
# Method 1: Press Windows + R, type "cmd", press Enter
# Method 2: Search for "Command Prompt" in Start menu
# Method 3: Search for "PowerShell" (more modern)

# Mac:
# Method 1: Press Command + Space, type "terminal", press Enter
# Method 2: Go to Applications → Utilities → Terminal

# Linux:
# Method 1: Press Ctrl + Alt + T
# Method 2: Search for "terminal" in applications menu

# --------------------------------------------
# BASIC NAVIGATION COMMANDS
# --------------------------------------------

# pwd - Print Working Directory (shows where you are)
# Windows: cd (without arguments)
# Mac/Linux: pwd
# Example output: /Users/yourname/Documents

# ls - List files and folders (Mac/Linux)
# dir - List files and folders (Windows)
# Shows what's in your current folder

# cd - Change Directory (move to a different folder)
# Examples:
# cd Documents        → Go into Documents folder
# cd ..              → Go up one level (to parent folder)
# cd ~               → Go to your home folder (Mac/Linux)
# cd C:\Users        → Go to specific path (Windows)

# --------------------------------------------
# EXAMPLE SESSION: NAVIGATE TO YOUR CODE
# --------------------------------------------

# Let's say your Python file is in Documents/python_code

# Step 1: Check where you are
# Mac/Linux:
#   pwd
# Windows:
#   cd

# Step 2: List what's here
# Mac/Linux:
#   ls
# Windows:
#   dir

# Step 3: Move to Documents
#   cd Documents

# Step 4: Check what's in Documents
# Mac/Linux:
#   ls
# Windows:
#   dir

# Step 5: Move to python_code folder
#   cd python_code

# Step 6: Now you can run your Python file
#   python hello.py

# --------------------------------------------
# RUNNING PYTHON IN THE TERMINAL
# --------------------------------------------

# Three ways to use Python in terminal:

# 1. RUN A PYTHON FILE
# Command: python filename.py
# or on some systems: python3 filename.py
# Example:
#   python 01_what_is_python.py
# This runs all the code in the file

# 2. INTERACTIVE MODE (Python REPL)
# Command: python
# or: python3
# Example session:
"""
$ python
Python 3.11.0
>>> 2 + 3
5
>>> name = "Alice"
>>> print(name)
Alice
>>> exit()
$
"""
# Type 'exit()' or press Ctrl+D (Mac/Linux) or Ctrl+Z (Windows) to quit

# 3. RUN PYTHON CODE DIRECTLY
# Command: python -c "your code here"
# Example:
#   python -c "print('Hello!')"
# Runs the code without creating a file

# --------------------------------------------
# USEFUL TERMINAL COMMANDS
# --------------------------------------------

# CREATE A NEW FOLDER
# Mac/Linux: mkdir folder_name
# Windows: mkdir folder_name
# Example:
#   mkdir my_python_projects

# CREATE A NEW FILE
# Mac/Linux: touch filename.py
# Windows: type nul > filename.py
# Example:
#   touch hello.py

# DELETE A FILE
# Mac/Linux: rm filename.py
# Windows: del filename.py
# Example:
#   rm old_code.py

# COPY A FILE
# Mac/Linux: cp source.py destination.py
# Windows: copy source.py destination.py
# Example:
#   cp program.py backup.py

# CLEAR THE SCREEN
# Mac/Linux: clear
# Windows: cls
# Makes the terminal look clean again

# --------------------------------------------
# INSTALLING PYTHON PACKAGES
# --------------------------------------------

# pip is Python's package installer
# It comes with Python

# INSTALL A PACKAGE
# Command: pip install package_name
# or: pip3 install package_name
# Example:
#   pip install requests
# This downloads and installs the 'requests' package

# LIST INSTALLED PACKAGES
# Command: pip list
# Shows all packages you have installed

# UPGRADE A PACKAGE
# Command: pip install --upgrade package_name
# Example:
#   pip install --upgrade requests

# UNINSTALL A PACKAGE
# Command: pip uninstall package_name
# Example:
#   pip uninstall requests

# --------------------------------------------
# CHECKING YOUR PYTHON VERSION
# --------------------------------------------

# Command: python --version
# or: python3 --version

# Example output:
#   Python 3.11.0

# If you see "command not found" or "not recognized":
# Python might not be installed or not in your PATH

# --------------------------------------------
# COMMON TERMINAL PROBLEMS
# --------------------------------------------

# Problem 1: "python is not recognized" (Windows)
# Solution: Python isn't installed or not in PATH
# Fix: Reinstall Python and check "Add to PATH" during installation

# Problem 2: "command not found: python" (Mac/Linux)
# Solution: Try python3 instead of python
# Some systems use python3 for Python 3

# Problem 3: File not found when running code
# Solution: Make sure you're in the right folder
# Use 'cd' to navigate to where your file is

# Problem 4: Permission denied
# Mac/Linux Solution: Add 'sudo' before command
# Example: sudo pip install package_name
# You'll need to enter your password

# --------------------------------------------
# KEYBOARD SHORTCUTS IN TERMINAL
# --------------------------------------------

# Ctrl + C - Stop running program
# Use when program is stuck or you want to cancel

# Ctrl + L (Mac/Linux) or cls (Windows) - Clear screen
# Makes terminal look clean

# Up Arrow - Previous command
# Repeats the last command you typed

# Tab - Auto-complete
# Start typing a filename or folder and press Tab

# Ctrl + D (Mac/Linux) or Ctrl + Z (Windows) - Exit Python interactive mode

# --------------------------------------------
# EXAMPLE: COMPLETE WORKFLOW
# --------------------------------------------

"""
# Let's create and run a Python program

# 1. Open terminal

# 2. Navigate to where you want to work
cd Documents

# 3. Create a new folder for Python projects
mkdir my_python

# 4. Go into that folder
cd my_python

# 5. Create a new Python file
touch hello.py

# 6. Edit the file (opens in your default editor)
# On Mac/Linux: nano hello.py
# On Windows: notepad hello.py
# Type this code:
#   print("Hello, World!")
# Save and exit

# 7. Run your program
python hello.py

# Output: Hello, World!

# 8. Open Python interactive mode to test some code
python

# 9. Try some Python
>>> 5 + 3
8
>>> name = "Python"
>>> print(f"I love {name}!")
I love Python!

# 10. Exit Python
>>> exit()

# 11. You're back in the terminal
"""

# --------------------------------------------
# TIPS FOR TERMINAL BEGINNERS
# --------------------------------------------

# 1. Don't be afraid to make mistakes
#    - The terminal won't break your computer
#    - Most commands are reversible

# 2. Use Tab completion
#    - Type first few letters, press Tab
#    - Saves time and prevents typos

# 3. Keep a cheat sheet handy
#    - Write down commands you use often
#    - Refer to this file when needed

# 4. Practice regularly
#    - The more you use it, the more natural it becomes
#    - Try doing tasks in terminal instead of clicking

# 5. Read error messages carefully
#    - They usually tell you exactly what's wrong
#    - Google the error if you don't understand

# --------------------------------------------
# QUICK REFERENCE CHART
# --------------------------------------------

"""
Task                    Mac/Linux           Windows
----------------------------------------------------------
Show current location   pwd                 cd
List files             ls                  dir
Change folder          cd folder           cd folder
Go up one level        cd ..               cd ..
Go to home folder      cd ~                cd %USERPROFILE%
Clear screen           clear               cls
Create folder          mkdir name          mkdir name
Create file            touch file.py       type nul > file.py
Delete file            rm file.py          del file.py
Run Python file        python file.py      python file.py
Open Python mode       python              python
Install package        pip install pkg     pip install pkg
Check Python version   python --version    python --version
"""

# ============================================
# PRACTICE EXERCISES
# ============================================

# Try these in your terminal:

# Exercise 1: Navigation
# 1. Open your terminal
# 2. Check where you are (pwd or cd)
# 3. List what's in the current folder (ls or dir)
# 4. Navigate to your Documents folder
# 5. Come back to where you started

# Exercise 2: Create and Run
# 1. Create a new folder called "python_practice"
# 2. Navigate into it
# 3. Create a file called "test.py"
# 4. Write a simple print statement in it
# 5. Run it with python test.py

# Exercise 3: Interactive Python
# 1. Open Python interactive mode
# 2. Do some calculations
# 3. Create a variable
# 4. Print the variable
# 5. Exit Python mode

# Exercise 4: Check Your Setup
# 1. Check your Python version
# 2. Try running 'pip list' to see installed packages
# 3. Install a simple package (try: pip install emoji)
# 4. Uninstall it (pip uninstall emoji)

# Exercise 5: Navigate Like a Pro
# 1. Without clicking anything:
# 2. Navigate to your Desktop
# 3. Create a folder called "code_test"
# 4. Navigate into it
# 5. Create a Python file
# 6. Navigate back to Desktop
# 7. All using just terminal commands!
