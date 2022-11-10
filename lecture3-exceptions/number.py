def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
        # else execs if there's no exception


main()

"""
try:
    one statement
except ValueError:
    handle error
else:
    this execs if try works
"""

"""
# pass catches an error but doesn't do anything
try:
    foo
except ValueError:
    pass
"""