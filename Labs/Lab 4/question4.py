# CNS3102
# Python Programming
# Sem 2 2023/2024
# Lab 4 Questions : Lists

# Q4: List Sorting and Concatenation
# • Create two lists: list1 containing [3, 7, 1, 9] and list2 containing [2, 6, 8, 4].
list1 = [3, 7, 1, 9]
list2 = [2, 6, 8, 4]
# • Sort both lists in ascending order.
list1.sort()
list2.sort()
# • Concatenate both lists and store the result in a new list named sorted_list.
sorted_list = list1 + list2
# • Print sorted_list.
print(f"sorted_list = ", sorted_list)