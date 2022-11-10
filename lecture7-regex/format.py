import re

name = input("What's your name? ").strip()
# two capture groups
# check out the walrus operator to ask a bool q
if matches := re.search(r"^(.+), *(.+)$", name):
# if search returned values, change name var
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    name =  matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
