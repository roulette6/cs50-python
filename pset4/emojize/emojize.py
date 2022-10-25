import emoji


def main():
    before = input("Input: ").strip()

    after = emoji.emojize(before, language="alias")

    print(f"Output: {after}")


if __name__ == "__main__":
    main()
