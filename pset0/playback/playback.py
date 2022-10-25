def main():
    fast = input()
    print(slow_down(fast))


def slow_down(fast):
    return fast.replace(" ", "...")


main()