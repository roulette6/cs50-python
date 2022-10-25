import sys
import csv


def main():
    # verify correct num args
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # save filename arguments to vars
    before = sys.argv[1]
    after = sys.argv[2]

    # try open old file
    try:
        old_file = open(before)
    except:
        sys.exit(f"Could not read {before}")
    else:
        # create list for dict of separated data
        clean_data = []

        # populate clean_data with data from old file file
        with old_file:
            reader = csv.DictReader(old_file)
            for row in reader:
                # split last and first names into separate vars
                last, first = row["name"].replace(" ", "").split(",")

                # create a dict per row and append to list of clean data
                clean_data.append({"last": last, "first": first, "house": row["house"]})

        with open(after, "w", newline="") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            # write a row for each record in clean_data dict
            for record in clean_data:
                writer.writerow(
                    {
                        "first": record["first"],
                        "last": record["last"],
                        "house": record["house"],
                    }
                )


def split_name(name):
    return name


if __name__ == "__main__":
    main()
