import inflect


def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    print(adieu(names))


def adieu(list):
    p = inflect.engine()
    inflected = p.join(list)
    return "Adieu, adieu, to " + inflected


if __name__ == "__main__":
    main()
