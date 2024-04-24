# CNS3102
# Python Programming
# Self-Learning Exercise - REGEX


# Pattern Identification

# Exercise 2:

# Task: Provide a single-line string containing a mix of letters, digits, and special characters.
# String: "The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and one digit."
# Question: Write a regular expression to identify all occurrences of lowercase letters in the provided string. Explain how your regex works and why it correctly identifies the lowercase letters in the string.
# The output would be: ['assword', 'must', 'contain', 'at', 'least', 'characters', 'and', 'include', 'at', 'least', 'one', 'uppercase', 'letter', 'one', 'lowercase', 'letter', 'and', 'one', 'digit']

import re

# Provided string
string = "The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and one digit."

# Regular expression to identify all occurences of lowercase letters
regex = r'\b[a-z]+\b'

# Using re.findall() to find all occurences of the regex in the string
lowercase_letters = re.findall(regex, string)

# Printing the lowercase letters found in the string
print(lowercase_letters)

# Explanation of the regular expression `r\b[a-z]+\b`:

# ﹒ `\b`: Matches a word boundary, ensuring that the match occurs at the beginning or end of a word.
# ﹒ `[a-z]`: Matches any lowercase letter from 'a' to 'z'.
# ﹒ `+`: Matches one or more occurences of the preceding expression (i.e., `[a-z]`). This ensures that all consecutive lowercase letters are matched as a single occurence.
# ﹒ `\b`: Matches a word boundary, ensuring that the match occurs at the end of a word.

# Therefore, the regular expression correctly identifies all occurences of lowercase letters in the provided string.
