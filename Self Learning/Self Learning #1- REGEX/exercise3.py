# CNS3102
# Python Programming
# Self-Learning Exercise - REGEX


# Pattern Identification

# Exercise 3:

# Task: Provide a multi-line string containing a mix of letters, digits, and special characters.
# String:
#   The product ID is ABC123XYZ,
#   and the price is $99.99.
# Question: Write a regular expression to identify all occurrences of words (sequences of letters) in the provided multi-line string. Explain how your regex works and why it correctly identifies the words in the string.
# The output would be: ['The', 'product', 'ID', 'is', 'ABC', 'XYZ', 'and', 'the', 'price', 'is']

import re

# Provided multi-line string
string = """
The product ID is ABC123XYZ,
and the price is $99.99.
"""

# Regular expression to identify all occurences of words (sequences of letters)
regex = r'\b[A-Za-z]+(?:\d+[A-Za-z]*)*\b'

# Using re.findall() to find all occurences of the regex in the string
words = re.findall(regex, string)

# Printing the words found in the string
print(words)


# Explanation of the regular expression `r'\b[A-Za-z]+\b'`

# ﹒ `\b`: Matches a word boundry, ensuring that the match occurs at the beginning or end of a word.
# ﹒ `[A-Za-z]: Matches any uppercase or lowercase letter.`
# ﹒ `+`: Matches one or more occurences of the preceding expression (i.e., `[A-Za-z]`). This ensures that all consecutive letters are matched as a single word.
# ﹒ `\b`: Matches a word boundary, ensuring that the match occurs at the end of a word.

# Therefore, the regular expression correctly identifies all occurences of words (sequences of letters) in the provided multi-line string.