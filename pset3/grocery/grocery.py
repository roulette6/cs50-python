def main():

    grocery_list = get_items()

    print_items(grocery_list)


def get_items():
    items = []

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            print()
            items.sort()
            return items
        else:
            items.append(item)



def print_items(items):
    numbered = {}

    for item in items:
        numbered[item] = items.count(item)

    for item, number in numbered.items():
        print(number, item)


if __name__ == "__main__":
    main()