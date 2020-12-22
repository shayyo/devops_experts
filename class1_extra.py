import sys
import datetime

# 1 - Write a program which prints 'Hello' on screen and then print your name on
# a separate line.
name = input("What is your name: ")
print("Hello")
print(name)

print("=" * 20)

# 2 - Write a program to print the sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum of the two numbers is: {num1 + num2}")

print("=" * 20)

# 3 - Write a program which will print the Python version number installed on
# your machine.
print("Python version installed is: ", sys.version_info)

print("=" * 20)

# 4 - Write a program which will reverse a word (e.g. hello  olleh)
mystring = "hello"
print(mystring[::-1])

print("=" * 20)

# 5 - Write a program which will print the amount of letters in a given word (e.g.
# hello  5)
print(len("hello"))

print("=" * 20)

# 6 - Write a program which will print the current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

print("=" * 20)

# 7 - Write a program which:
# A. contains 2 variables X & Y
# B. Give X & Y values (e.g. X = 1, Y = 5)
# C. Using if-else check which is bigger, and print the bigger number.
x = 54
y = 5
if x > y:
    print("x is bigger than y")
elif y > x:
    print("y is bigger than x")
else:
    print("x and y are equal")

print("=" * 20)

# - 8 Write a program which will check whether or not the number 120 is bigger
# than 5 and smaller than 200, if so, print MATCH

x = 120
y = 5
max_number = 200
if y < x < 200:
    print("MATCH")




