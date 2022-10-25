def main():
    # initialize vars
    due = 50
    total = 0
    owed = 0

    # keep asking for coins until total reaches 50
    while True:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))

        due, total, owed, done = update_values(due, coin, total, owed)

        if done:
            break

    print(f"Change Owed: {owed}")


# define a function that updates values

def update_values(due, coin, total, owed):
    price = 50
    done = False

    if coin in [5, 10, 25]:
        total = total + coin

        # if paid in full
        if total == price:
            due = 0
            owed = 0
            done = True
        # if overpaid
        elif total > price:
            due = 0
            owed = total - price
            done = True
        # if underpaid
        else:
            due = price - total

    return [due, total, owed, done]


if __name__ == "__main__":
    main()