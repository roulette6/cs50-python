def main():
    number = get_number()
    meow(number)


def meow(n):
    # using _ is Pythonic when throwaway var for counting
    for _ in range(n):
        print("meow")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


main()


"""
# the below also works
print("meow\n" * 3, end="")
"""

"""
i = 0

while i < 3:
    print("meow")
    i += 1
"""