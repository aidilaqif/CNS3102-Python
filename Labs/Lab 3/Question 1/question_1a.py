# Question 1: Please download the file from putrablast. Save the attached input file in your machine.
#   You are required to:
#       a. Read the input file
#       b. Count the number of lines in that input file and print
#       c. Count the following keywords in the input file using an apporiate string buil-in method and print:
#           (1) portfolio
#           (2) employer
#           (3) data

import os

# Declare file name
file_name = "lab-regex-input.txt"

# Check if file exist in directory
if os.path.isfile(file_name):
    # if file exist, open and read
    with open(file_name, "r") as file:
        contents = file.read()
    print("File exists. \nContents:")
    print(contents)
else:
    print("File does not exist")