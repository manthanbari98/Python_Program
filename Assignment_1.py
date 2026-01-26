"""
Problem Statement 1: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

Addition = num_1 + num_2
Subtraction = num_1 - num_2
Multiplication = num_1 * num_2
Division = round((num_1 / num_2),2)

print("Addition:",Addition)
print("Subtraction:",Subtraction)
print("Multiplication:",Multiplication)
print("Division:",Division)


"""
Problem Statement 2: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print("Hello, "+first_name+" "+last_name+"! Welcome to the Python Program.")

