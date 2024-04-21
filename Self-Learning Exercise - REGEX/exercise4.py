# CNS3102
# Python Programming
# Self-Learning Exercise


# Pattern Identification

# Exercise 4:

# Task: Provide a single-line string containing spaces and tabs mixed in.
# String: "The quick brown fox jumps over the lazy dog."
# Question: Write a regular expression to remove all whitespace characters (spaces and tabs) from the provided string. Explain how your regex works and why it correctly removes the whitespace characters.
# The output would be: "Thequickbrownfoxjumpsoverthelazydog."

import re

# String containing spaces and tabs mixed in
text = "The quick brown fox jumps over the lazy dog."

# Regular expression pattern to match whitespace characters
pattern = r'\s+'

# Using re.sub() to remove whitespace characters
result = re.sub(pattern, '', text)

print(result)

#Explanation:
# ﹒ `\s`: Matches any whitespace characters (spaces, tabs, newlines).
# ﹒ `+`: Matches one or more occurences of the precedign pattern (whitespace characters in this case).
# ﹒ The `re.sub()` function is used to replace all matches of the pattern with an empty string, effectively removing the whitespace characters.
