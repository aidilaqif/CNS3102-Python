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

# Read the input file
with open (file_name, "r") as file:
    lines = file.readlines()

# Count the number of lines for looping
num_lines = len(lines)

# Declare the keywords count
keywords_count = {
    "portfolio": 0,
    "employer": 0,
    "data": 0
}

# Looping based on the number of lines
for line in lines:
    # Looping to count the keywords
    for keyword in keywords_count.keys():
        if keyword in line.lower():
            keywords_count[keyword] += 1

#Print the counts
for keyword, count in keywords_count.items():
    print(f"'{keyword}': {count}")