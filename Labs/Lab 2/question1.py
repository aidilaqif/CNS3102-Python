# Question 1
#The following formula can be used to generate (pseudo-)random numbers [1]:
    # x = x * 48271 % 2147483647
# In a Python script, generate and show the first 5 random numbers produced, given an initial value of x = 1.

# Print the header ofr the random numbers
print("5 random numbers: \n")

# Initialize the starting value for x
x = 1

# Loop to generate and print 5 random numbers
for n in range(1, 6): # Loop from 1 to 5 (stop at 6)
    x = x * 48271 % 2147483647 # Generate the next random number based on X(1), X(2), .... , X(n)
    print(f"{n}. {x}") # Print the index and the random number
