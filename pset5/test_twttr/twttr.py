def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    for letter in word:
        if is_vowel(letter):
            word = word.replace(letter, "")

    return word


def is_vowel(char):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    if char in vowels:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
