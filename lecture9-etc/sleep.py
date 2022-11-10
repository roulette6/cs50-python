def main():
    n = int(input("What's n? "))
    for line in sheep(n):
        print(line)


# yield is like saying return one value at a time
# without returning and exiting the function
def sheep(n):
    for i in range(n + 1):
        yield "🐑" * i


"""
# this function would hang if you passed 1,000,000 as the input
def sheep(n):
    flock = []
    for i in range(n + 1):
        flock.append("🐑" * i)
    return flock

"""

if __name__ == "__main__":
    main()
