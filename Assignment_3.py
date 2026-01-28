"""
Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

# Factorail using 'for loop':
# number = int(input("Enter the number to find its factorial: "))

# factorial = 1

# for n in range(1,number+1):
#     factorial *= n

# print(f"Factorial of {number} is {factorial}")

# Factorial using 'while loop':
number = int(input("Enter the number to find its factorial: "))
entered_number = number
factorial = 1

while number > 0 :
    factorial *= number
    number -= 1

print(f"Factorial of {entered_number} is {factorial}")

#Factorial using function :

# number = int(input("Enter the number to find its factorial: "))

# def factorial (number):
#     if number ==0 or number == 1:
#         return 1
#     return number * factorial(number-1)


# print(f"Factorial of {number} is {factorial(number)}")

"""
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
"""

# import math

# number = int(input("Enter the number to find its factorial: "))

# square_root = math.sqrt(number)
# logarithm = math.log(number)
# sine = math.sin(number)

# print(f"Square root of {number} is : {square_root}")
# print(f"Logarithm of {number} is : {logarithm}")
# print(f"Sine of {number} is : {sine}")

