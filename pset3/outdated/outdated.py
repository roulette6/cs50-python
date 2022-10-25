def main():

    year, month, day = get_date()
    print(f"{year}-{month:02d}-{day:02d}")



# get date as m/d/yyyy or Month d, yyyy
def get_date():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        date = input("Date: ").strip().title()

        if "/" in date:
            date = date.split("/")
            if date[0].isalpha():
                continue
        elif "," in date:
            date = date.replace(",", "").split(" ")
        else:
            continue

        try:
            year = int(date[2])
        except ValueError:
            continue

        month = get_month(date[0], months)

        try:
            day = int(date[1])
        except ValueError:
            continue

        if (validate_year(year) and
            validate_month(month, months) and
            validate_day(day)):
            return year, month, day


def get_month(month, months):
    try:
        return int(month) if month.isnumeric() else months[month]
    except KeyError:
        return -1


def validate_month(month, months):
    if month in months:
        return True
    elif 1 <= int(month) <= 12:
        return True
    else:
        return False

def validate_day(day):
    return True if 1 <= day <= 31 else False


def validate_year(year):
    return True if int(year) > 1 else False


if __name__ == "__main__":
    main()