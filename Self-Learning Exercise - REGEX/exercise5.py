# CNS3102
# Python Programming
# Self-Learning Exercise


# Exercise 5:

# Task: Provide a multi-line string containing spaces, tabs, and newline characters mixed in.
# String:
#   The quick brown
#   fox jumps
#   over
#   the
#   lazy dog.
# Question: Write a regular expression to remove all whitespace characters (spaces, tabs, and newline characters) from the provided multi-line string. Explain how your regex works and why it correctly removes the whitespace characters.
# The output would be: a single line without any whitespace characters.

import re

# Multi-line string containing spaces, tabs, and newline characters
text = """
The quick brown
fox jumps
over
the
lazy dog.
"""

# Regular expression pattern to match whitespace characters
pattern = r'\s+'

# Using re.sub() to remove whitespace characters
result = re.sub(pattern, '', text)

print(result)

# Explanation:

# ﹒ `\s`: Matches any whitespace character (spaces, tabs, newlines).
# ﹒ `+`: Matches one or more occurences of the preceding pattern (whitespace characters in this case).
# ﹒ The `re.sub()` function is used to replace all matches of the pattern with an empty string, effective removing the whitespace characters.