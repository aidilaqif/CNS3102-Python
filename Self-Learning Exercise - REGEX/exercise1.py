# CNS3102
# Python Programming
# Self-Learning Exercise - REGEX


# Pattern Identification

# Exercise 1:

# Task: Provide a single-line string containing a mix of letters, diigts and special
# String: "The product ID is ABC123XYZ, and the price is $99.99."
# Question: Write a regular expression to identify all occurrences of digits in the provided string. Explain how your regex works and why it correctly identifies the digits in the string.
# The output would be: ['123', '99', '99']

import re

# Provided string
string = "The product ID is ABC123XYZ, and the price is $99.99"

# Regular expression to identify all occurences of digits
regex = r'\d+'

# Using re.findall() to find all occurences of the regex in string
digits = re.findall(regex, string)

# Printing the digits found in the string
print(digits)


# Explanation of the regular expression `r'\d+'`:

# ﹒ `\d`: Mathces any digit (equivalent to `[0-9]`)
# ﹒ `+`: Mathces one or more occurences of the preceding expression (i.e., `\d`). This ensures that all consecutive digits are matched as a single occurence.

# Therefore, the regular expression correctly identifies all occurences of digits in the provided string.