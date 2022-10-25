def main():
    fraction = get_fraction("Fraction: ")
    percent = decimal_to_percent(fraction)

    print(percent)


def get_fraction(prompt):
    while True:
        fraction = input("Fraction: ").split("/")

        try:
            fraction = int(fraction[0]) / int(fraction[1])
        except (ValueError, ZeroDivisionError) as error:
            pass
        else:
            if fraction <= 1: return fraction


def decimal_to_percent(value):
    percent = round(value * 100)

    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return str(percent) + "%"


if __name__ == "__main__":
    main()