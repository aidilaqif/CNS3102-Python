# The interpreter acts as a simple calculator:
# you can type an expression at it and it will write the value.
# Expression syntax is straightforward: the operators +, -, * and /
# work just like in most other languages (for example, Pascal or C);
# parentheses (()) can be used for grouping. For example:

print("Part 1: ")
print("1. 2 + 2 = " + str(2 + 2))
print("2. 50 - 5*6 = " + str(50 - 5*6))
print("3. (50 - 5*6) / 4 = " + str((50 - 5*6) / 4))
print("4. 8 / 5 = " + str(8 / 5)) # division always returns a floating point number
print()

# The integer numbers (e.g. 2, 4, 20) have type int,
# the ones with a fractional part (e.g. 5.0, 1.6) have type float.
# We will see more about numeric types later in the tutorial.
# Division (/) always returns a float.
# To do floor division and get an integer result
# (discarding any fractional result) you can use the // operator;
# to calculate the remainder you can use %:

print("Part 2: ")
print("1. 17 / 3 = " + str(17 / 3)) # classic division returns a float
print("2. 17 // 3 = " + str(17 // 3)) # floor division discards the fractional part
print("17 % 3 = " + str(17 % 3)) # the % operator returns the remainder of the division
print("5 * 3 + 2 = " + str(5 * 3 + 2)) # result * divisor + remainder
print()

# With Python, it is possible to use the ** operator to calculate powers 1:
print("Part 3: ")
print("1. 5 ** 2 = " + str(5 ** 2)) # 5 squared
print("2. 2 ** 7 = " + str(2 ** 7)) # 2 to the power of 7
print()

# The equal sign (=) is used to assign a value to a variable.
# Afterwards, no result is displayed before the next interactive prompt:
print("Part 4: ")
width = 20
height = 5 * 9
print("width * height = " + str(width * height))
print()

# If a variable is not "defined" (assigned a value), tryin to use it will give you an error:
# print("Part 5: ")
# print(n) # try to access an undefined variable
# print()

# There is full support for floating point; operators with mixed type operands
# convert the integer operand to floating point:
print("Part 6: ")
print("4 * 3.75 -1 = " + str(4 * 3.75 - 1))
print()

# In interactive mode, the last printed expression is assigned to the variable _.
# This means that when you are using Python as a desk calculator,
# it is somewhat easier to continue calculations, for example:
tax = 12.5 / 100
print("tax = 12.5 / 100")
price = 100.50
print("price = 100.50")
last_result = price * tax # Perform calculations and store the result in last_result
print ("price * tax = " + str(last_result))
last_result = price + last_result # Use last_result in subsequent calculations
print("last_result = price + last_result = " + str(last_result))
last_result = round(last_result, 2) # Use last_result with round function
print("last_result = round(last_result, 2) = " + str(last_result))

# This variable should be treated as read-only by the user.
# Don’t explicitly assign a value to it — you would create an independent local variable
# with the same name masking the built-in variable with its magic behavior.

# In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction.
# Python also has built-in support for complex numbers,
# and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).