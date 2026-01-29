"""
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

# with open("sample.txt","wt") as fh:
#     fh.write("This is a sample text file.\nIt contains multiple lines.")

# try:
#     with open("sample.tx","rt") as fh:
#         line_1 = fh.readline()
#         line_2 = fh.readline()

#     print("Reading file content:")
#     print("Line 1:",line_1)
#     print("Line 2:",line_2)

# except FileNotFoundError:
#         print("The file 'sample.txt' was not found.")


"""
Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

# with open("output.txt", "wt") as fh:
#     fh.write(input("Enter your message here."))

# with open("output.txt", "at") as fh:
#     fh.write("\n" + input("Enter your message here."))

with open("output.txt", "rt") as fh:
    content = fh.readlines()
print(f"File content:\n{content}")






