# CNS3102
# Python Programming
# Sem 2 2023/2024
# Lab 4 Questions : Lists

# Q3: List Comprehension
# • Create a list named squares containing the squares of all numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1,11)]
# • Create a list named even_squares containing the squares of even numbers from 1 to 10 using list comprehension.
even_squares = [x**2 for x in range(1,11) if x % 2 ==0]
# • Print both lists.
print(f"squares = ",squares)
print(f"even squares = ", even_squares)