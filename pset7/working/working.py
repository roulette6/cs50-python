import re
import sys


def main():
    print(convert(input("Hours: ")))


# pattern for 24 hr time is add 12 to PM times
def convert(s):
    # 6 groups: hh mm a|pm hh mm a|pm
    if match := re.search(
        r"(\d{1,2})(?::)?(\d\d)? ([AP]M) to (\d{1,2})(?::)?(\d\d)? ([AP]M)",
        s,
        re.IGNORECASE,
    ):
        times = [
                int(match.group(1)),
                match.group(2),
                match.group(3),
                int(match.group(4)),
                match.group(5),
                match.group(6),
            ]
        if validate(times):
            # convert PM hours as needed
            if times[2] == "PM":
                times[0] += 12 if times[0] != 12 else 0
            if times[5] == "PM":
                times[3] += 12 if times[3] != 12 else 0

            # convert 12 AM
            if times[2] == "AM" and times[0] == 12:
                times[0] = 0
            if times[5] == "AM" and times[3] == 12:
                times[3] = 0

            # if there are minutes...
            if times[1]:
                time1 = f"{times[0]:02}:{times[1]}"
            else:
                time1 = f"{times[0]:02}:00"
            if times[4]:
                time2 = f"{times[3]:02}:{times[4]}"
            else:
                time2 = f"{times[3]:02}:00"

            return f"{time1} to {time2}"
        else:
            raise ValueError
    else:
        raise ValueError


def validate(group):
    # verify valid hours
    if not 1 <= group[0] <= 12 or not 1 <= group[3] <= 12:
        return False

    # verify whether both minutes were provided
    if group[1] and group[4]:
        # verify valid minutes
        if not 0 <= int(group[1]) < 60 or not 0 <= int(group[4]) < 60:
            return False

    # assume no errors unless an error is found
    return True


if __name__ == "__main__":
    main()
