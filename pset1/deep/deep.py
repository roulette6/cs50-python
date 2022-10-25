def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    print(check_it(answer))


def check_it(ans):
    ans = ans.strip().lower()

    match ans:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


main()