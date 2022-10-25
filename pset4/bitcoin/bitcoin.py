import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        qty = float(sys.argv[1])
    except ValueError:
        sys.exit("Value is not a float")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Error retrieving bitcoin price")

    json = response.json()
    total = qty * json["bpi"]["USD"]["rate_float"]
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
