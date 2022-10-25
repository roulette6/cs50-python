from datetime import date
import sys
import inflect


def main():

    # prompt for bday in ISO format YYYY-MM-DD
    dob = get_dob()

    # print delta btw today and dob
    print(sing_it(dob))


def get_dob():
    try:
        return date.fromisoformat(input("Date of Birth: "))
    # exit if date not provided in ISO format
    except ValueError:
        sys.exit("Invalid date")


def sing_it(date_obj):
    delta = date.today() - date_obj
    minutes = days_to_minutes(delta.days)

    # convert minutes to words
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"


def days_to_minutes(days):
    return days * 24 * 60


if __name__ == "__main__":
    main()
