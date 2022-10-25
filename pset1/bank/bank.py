def main():
    greeting = input("Greeting: ")
    print(check_greeting(greeting))


def check_greeting(greeting):
    greeting = greeting.strip().lower()

    if greeting[0:5] == "hello":
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"


main()