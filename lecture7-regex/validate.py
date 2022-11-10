import re

"""
regex reminders:
+       1 or more repetitions
?       0 or 1 repetition
{m}     m repetitions
{m,n}   m-n repetitions
[]      only these characters allowed
[^]     anything but these characters
\d      decimal digit
\D      not a decimal digit
\s      whitespace char
\S      not a whitespace char
\w      word char (a-zA-Z0-9_)
\W      not a word char
A|B     either A or B
(...)   a group
(?:...) non-capturing version

# regex functions
re.search(pattern, string, flags=0)
re.match(pattern, string, flags=0) # starts from the beginning
re.fullmatch(pattern, string, flags=0)
"""

email = input("What's your email? ").strip()

# the "r" before the pattern means raw string
# and is required so Python interprets the
# escape character correctly

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

"""
if username and domain.endswith(".edu"):
"""
