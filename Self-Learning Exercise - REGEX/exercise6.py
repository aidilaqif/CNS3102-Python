# CNS3102
# Python Programming
# Self-Learning Exercise


# Exercise 6:

# Task: Provide a multi-line string containing students' information, including email
# addresses and phone numbers.
# String:
    # Student 1:
    # Name: John Doe
    # Email: john.doe@example.com
    # Phone: 123-456-7890

    # Student 2:
    # Name: Jane Smith
    # Email: jane.smith@example.com
    # Phone: (987) 654-3210

    # Student 3:
    # Name: Alex Johnson
    # Email: alex.johnson@example.com
    # Phone: 555-123-4567

# Question: Write regular expressions to extract all email addresses and phone numbers from the provided multi-line string. Explain how your regex works and why it correctly extracts the email addresses and phone numbers.
# The output would be:

# Email addresses found:
    # john.doe@example.com
    # jane.smith@example.com
    # alex.johnson@example.com

# Phone numbers found:
    # 123-456-7890
    # (987) 654-3210
    # 555-123-4567

import re

# Multi-line string containing students' information
text = """
Student 1:
Name: John Doe
Email: john.doe@example.com
Phone: 123-456-7890

Student 2:
Name: Jane Smith
Email: jane.smith@example.com
Phone: (987) 654-3210

Student 3:
Name: Alex Johnson
Email: alex.johnson@example.com
Phone: 555-123-4567
"""

# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Regular expression pattern to match phone numbers
phone_pattern = r'\b(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})\b'

# Using re.findall() to find all email address in the text
emails = re.findall(email_pattern, text)

#Using re.findall() to find all phone numbers in the text
phones = re.findall(phone_pattern, text)

print("Email addresses found: ")
for email in emails:
    print(email)

print("\nPhone numbers found: ")
for phone in phones:
    print(phone)