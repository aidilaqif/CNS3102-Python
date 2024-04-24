# 2. Please demonstrate the use of regex for the statement.

#   Malaysia saw a drastic increase of online scams over the last two
#   years during the Covid-19 pandemic. According to the Royal
#   Malaysia Police’s (PDRM) commercial crimes investigation
#   department (CCID), a total of 71,833 scams, amounting to more
#   than RM5.2 billion losses, was reported from 2020 until May 2022.

#   (a) Check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
#   (b) Check that a string contains only a certain set of characters (in this case A-Z) with boundary.
#   (c) Check whether a string starts and ends with the same character.
#   (d) Search the start and end index for the keywords of “Covid”.
#   (e) Demonstrate the use of split(), sub() and escape() method.

import re

string = "Malaysia saw a drastic increase of online scams over the last two years during the Covid-19 pandemic. According to the Royal Malaysia Police’s (PDRM) commercial crimes investigation department (CCID), a total of 71,833 scams, amounting to more than RM5.2 billion losses, was reported from 2020 until May 2022."

pattern  = r"\bCovid\b"
match = re.search(pattern, string)
if match:
    start_index = match.start()
    end_index = match.end()
    print(f"Start index: {start_index}, End index: {end_index}")
else:
    print("Keyword 'Covid' not found.")