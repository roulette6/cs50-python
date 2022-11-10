import random

"""
The class below will be a container for related properties
and methods, but will not be instantiated, so it doesn't
need an __init__ method. This class has class variables
and class methods.
"""
class Hat:
    # class variable, not instance variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")