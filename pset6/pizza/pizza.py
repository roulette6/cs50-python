import sys
import csv
from tabulate import tabulate


def main():
    # confirm two args
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    file_name = sys.argv[1]
    # verify file name is at least 5 chars
    # before attempting to check extension
    if len(file_name) > 4:
        if file_name[-4:] != ".csv":
            sys.exit("Not a CSV file")
    else:
        sys.exit("Not a CSV file")

    # try opening the file in a try block
    try:
        file = open(file_name, newline="", encoding="utf-8")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        # table to populate with rows
        table = []
        # use with file for automatic file closing
        with file:
            reader = csv.reader(file)
            # append each row from file to table
            for row in reader:
                table.append(row)

    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
