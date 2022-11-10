def main():
    yell("This", "is", "CS50")


def yell(*words):
    # list comprehension is more Pythonic than
    # the commented example below.
    uppercased = [word.upper() for word in words]
    print(*uppercased)


"""
# functional programming
def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
"""

if __name__ == "__main__":
    main()
