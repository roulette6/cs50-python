name = input("What's your name: ")
names = []

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# read mode is the default
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

"""
with open("names.txt") as file:
    for line in sorted(file):
        print("hello," line.rstrip())
"""

"""
# save all lines in a list
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.strip())
"""

"""
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""

"""
names = []

for _ in range(3):
    names.append(input("What's your name: "))

for name in sorted(names):
    print(f"Hello, {name}")
"""