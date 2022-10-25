def main():
    msg = input()
    msg = emote(msg)
    print(msg)


def emote(text):
    text = text.replace(":(", "🙁")
    text = text.replace(":)", "🙂")
    return text

main()