import random


def main():
    level = get_number("Level: ")
    number = random.randint(1, level)

    while True:
        guess = get_number("Guess: ")
        results = compare_numbers(guess, number)
        if results:
            exit()


def get_number(prompt):
    while True:
        try:
            i = int(input(prompt))
        except ValueError:
            continue
        else:
            if i > 0:
                return i


def compare_numbers(i, j):
    if i == j:
        print("Just right!")
        return True
    elif i > j:
        print("Too large!")
        return False
    else:
        print("Too small!")
        return False


if __name__ == "__main__":
    main()
