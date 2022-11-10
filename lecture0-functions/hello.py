# define the main function
def main():
    # ask user for their name and clean it up
    name = input("What is your name? ").strip().title()
    hello(name)


def hello(to="world"):
    print("hello,", to)


# call main
main()



"""

# split user's name into first and last name
first, last = name.split(" ")

# say hello to user in different ways

# 'f' means format string
print(f"hello, {first}")

# print using multiple arguments
print("hello,", first)

# change end char to space
print("hello,", end=" ")
print(first)
"""