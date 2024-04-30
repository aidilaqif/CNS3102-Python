# CNS3102
# Python Programming
# Sem 2 2023/2024
# Lab 4 Questions : Lists

# Q5: List Manipulation without Functions
# • Create a list named mixed_list containing integers, floats, and strings.
mixed_list = [1, 1.5, "apple", 2, 2.5, "orange"]
# • Write code to remove all integers from the list.
mixed_list = [x for x in mixed_list if not isinstance(x, int)]
# • Print the modified list.
print(f"mixed_list = ", mixed_list)
# • Write code to append the word "Python" to the end of the list.
mixed_list.append("Python")
# • Print the final list.
print(f"mixed_list = ", mixed_list)