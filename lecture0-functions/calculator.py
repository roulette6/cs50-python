def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)


main()

"""
# print with commas
print(f"{z:,}")

# print rounded to two decimal places
print(f"{z:.2f}")
"""