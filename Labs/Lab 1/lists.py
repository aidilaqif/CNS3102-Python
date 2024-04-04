# Python knows a number of compound data types, used to group together other values.
# The most versatile is the list,
# which can be written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.

print("Part 1: ")
squares = [1, 4, 9, 16, 25]
print("squares = " + str(squares))
print()

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print("Part 2: ")
print("squares[0] = " + str(squares[0])) # indexing returns the item
print("squares[-1] = " + str(squares[-1])) # indexing returns the last item on the list
print("squares[-3:] = " + str(squares[-3:])) # slicing returns a new list
print()

# All slice operations return a new list containing the requested elements.
# This means that the following slice returns a new (shallow) copy of the list:
print("Part 3: ")
print("squares[:] = " + str(squares[:]))
print()

# Lists also support operations like concatenation:
print("Part 4: ")
print("squares + [36, 49, 64, 81, 100] = " + str(squares + [36, 49, 64, 81, 100]))
print()

# Unlike strings, which are immutable, lists are a mutable type,
# i.e. it is possible to change their content:
print("Part 5: ")
cubes = [1, 8, 27, 65, 125] # something's wrong here
print("cubes = [1, 8, 27, 65, 125]")
print("4 ** 3 = " + str(4 ** 3))
cubes [3] = 64 # replace the wrong value
print("cubes [3] = 64")
print("cubes = " + str(cubes))
print()

# You can also add new items at the end of the list,
# by using the append() method (we will see more about methods later):
print("Part 6: ")
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print("cubes = " + str(cubes))
print()

# Assignment to slices is also possible,
# and this can even change the size of the list or clear it entirely:
print("Part 7: ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("letters = " + str(letters))
letters[2:5] = ['C', 'D', 'E'] # replace some values
print("letters[2:5] = " + str(letters[2:5]))
print("letters = " + str(letters))
letters[2:5] = [] # now remove them
print("letters = " + str(letters))
letters[:] = [] # clear the list by replacing all the elements with an empty list
print("letters = " + str(letters))
print()

# The built-in function len() also applies to lists:
print("Part 8: ")
letters = ['a', 'b', 'c', 'd']
print("letters = " + str(letters))
size = len(letters)
print("len(letters) = " + str(size))
print()

# It is possible to nest lists (create lists containing other lists), for example:
print("Part 9: ")
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("a = " + str(a))
print("n = " + str(n))
print("x = " + str(x))
print("x[0] = " + str(x[0]))
print("x[0][1] = " + str(x[0][1]))
print()