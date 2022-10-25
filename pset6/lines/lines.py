import sys


def main():

    lines = 0

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
    except:
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                line = line.lstrip()
                if len(line) > 1:
                    if not line.startswith("#"):
                        lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(lines)


if __name__ == "__main__":
    main()
