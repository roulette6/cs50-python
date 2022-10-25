import pyfiglet
import random
import sys


def main():
    arguments = evaluate_args(["-f", "--font"])

    match arguments:
        case "one":
            f = pyfiglet.Figlet(font=random_font())
        case "two":
            try:
                f = pyfiglet.Figlet(font=sys.argv[2])
            except pyfiglet.FontNotFound:
                sys.exit("Invalid font")

    msg = input("Input: ").strip()
    print("Output:", f.renderText(msg), sep="\n")


def evaluate_args(flags):
    if len(sys.argv) == 1:
        return "one"
    elif len(sys.argv) == 3 and sys.argv[1] in flags:
        return "two"
    else:
        sys.exit("Invalid usage")


def random_font():
    fonts = [
        "3-d",
        "3x5",
        "5lineoblique",
        "acrobatic",
        "alligator",
        "alligator2",
        "alphabet",
        "avatar",
        "banner",
        "banner3-D",
        "banner3",
        "banner4",
        "barbwire",
        "basic",
        "bell",
        "big",
        "bigchief",
        "binary",
        "block",
        "bubble",
        "bulbhead",
        "calgphy2",
        "caligraphy",
        "catwalk",
        "chunky",
        "coinstak",
        "colossal",
        "computer",
        "contessa",
        "contrast",
        "cosmic",
        "cosmike",
        "cricket",
        "cyberlarge",
        "cybermedium",
        "cybersmall",
        "diamond",
        "digital",
        "doh",
        "doom",
        "dotmatrix",
        "drpepper",
        "eftichess",
        "eftifont",
        "eftipiti",
        "eftirobot",
        "eftitalic",
        "eftiwall",
        "eftiwater",
        "epic",
    ]
    return random.choice(fonts)


if __name__ == "__main__":
    main()
