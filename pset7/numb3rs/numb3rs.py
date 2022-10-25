import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if octets := re.search(r"(^\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if  1 < int(octets.group(1)) < 256:
            for octet in octets.group(2,3,4):
                if 0 <= int(octet) < 256:
                    continue
                else:
                    return False
            return True
    return False


if __name__ == "__main__":
    main()

