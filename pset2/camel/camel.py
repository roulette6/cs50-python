def main():
    camel_case = input("CamelCase: ")
    snake_case = camel_to_snake(camel_case)
    print(f"snake_case: {snake_case}")


def camel_to_snake(text):
    for char in text:
        if char.isupper():
            snaked = "_" + char.lower()
            text = text.replace(char, snaked)

    return text


if __name__ == "__main__":
    main()