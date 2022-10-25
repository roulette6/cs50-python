def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        valid_start(s) and
        valid_length(s) and
        valid_numbers(s) and
        s.isalnum()
    ):
        return True


def valid_start(s):
    return s[0:2].isalpha()


def valid_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def valid_numbers(s):
    numbers = []
    s_length = len(s)

    for i in range(s_length):
        # if there are numbers
        if s[i].isnumeric():
            numbers.append(s[i])

            # if there are more characters
            # and the next one is a letter
            if i + 1 < s_length:
                if s[i + 1].isalpha():
                    return False

        # first cannot be a zero
        if len(numbers) > 0:
            if numbers[0] == "0":
                return False

    # otherwise return True
    return True


if __name__ == "__main__":
    main()