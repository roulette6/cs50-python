import random


def main():
    score = 0
    level = get_level()

    integers = []

    for _ in range(20):
        integers.append(generate_integer(level))

    i = 0
    while i < 20:
        answer = integers[i] + integers[i + 1]
        prompt = str(integers[i]) + " + " + str(integers[i + 1]) + " = "

        for j in range(3):

            guess = get_int(prompt)
            if guess == answer:
                score += 1
                break
            else:
                print("EEE")

            if j == 2:
                print(f"{prompt} {answer}")

        i += 2

    print(f"Score: {score}")


def get_level():
    x = 0
    while x not in [1, 2, 3]:
        try:
            x = int(input("Level: "))
        except ValueError:
            continue
    return x


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue


if __name__ == "__main__":
    main()
