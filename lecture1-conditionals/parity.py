def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()

"""
# this is pythonic but redundant

    return True if n % 2 == 0 else False
"""