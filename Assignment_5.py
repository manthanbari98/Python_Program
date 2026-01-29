"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

student_results = {"Alice" : 85, "Mark" : 79, "Jason" : 87, "Jenny" : 91}

student_results["Rob"] = 74  #just for practise
print(student_results)

student_name = input("Enter student's name:")
if student_name == student_results.keys:
    print(f"{student_name}'s marks: {student_results[student_name]}")
else:
    print("Student not found")

"""
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""

original_list = list(range(1,11))
print(f"Original List: {(original_list)}")

first_five = original_list[:6]
reversed_five = first_five[::-1]

print("Extracted first five elements:",first_five)
print("Reversed extracted elements",reversed_five)



