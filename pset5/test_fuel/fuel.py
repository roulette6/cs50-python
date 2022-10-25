def main():
    while True:
        fraction = input("Fraction: ")

        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break

    print(gauge(percentage))


def convert(fraction):
    fraction = fraction.split("/")
    decimal = int(fraction[0]) / int(fraction[1])

    if decimal > 1:
        raise ValueError

    return round(decimal * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
