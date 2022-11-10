# type hint for var and for the func itself
def bark(n: int) -> str:
    """
    Bark n times

    :param n: Number of times to bark
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n barks, one per line
    :rtype: str
    """
    return "woof\n" * n


# type hint
number: int = int(input("Number: "))
barks: str = bark(number)
print(barks, end="")
