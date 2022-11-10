def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for letter in word:
        if letter not in vowels:
            word = word.replace(letter, "")

    return word


if __name__ == "__main__":
    main()
