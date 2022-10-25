import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^<iframe.*?(?:")?https?://(?:www\.)?youtube\.com/embed/(.{11})(?:")?.*></iframe>$', s):
        return "https://youtu.be/" + match.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
