def main():
    message = input()
    message = indoor(message)
    print(message)

def indoor(msg):
    return msg.lower()


main()