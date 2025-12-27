# functions.py
# Day 3 Python practice – Functions

print("=== Python Functions ===")

# Simple function
def greet():
    print("Hello! Welcome to Python programming.")

greet()

# Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Shamal")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum is:", result)

# Function with logic
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("5 is", check_even_odd(5))
print("8 is", check_even_odd(8))
