# test with pytest test, where test is a folder of tests.
# the entire folder will execute if there's a file named __init__.py
# regardless of whether __init__.py is empty

def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
