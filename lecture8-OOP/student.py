"""
the difference between varname and _varname is that
varname is the name of the property and _varname is
the name of the instance variable.

Unfortunately, Python doesn't prevent users from
manually setting instance variables b/c you're on
the honor system 😢
Don't manually set instance vars starting with _

class methods can be called without instantiating an
object first.
"""


class Student:
    # constructor method
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # method for printing object
    def __str__(self):
        return f"{self.name} from {self.house}"

    # getter
    @property
    def name(self):
        return self._name

    # setter
    # if someone tries to manually change an attribute,
    # the setter gets called and the validation kicks in
    @name.setter
    def name(self, name):
        # Pythonic way of if a != ""
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # getter
    @property
    def house(self):
        return self._house

    # setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError(f"Invalid house: {house}")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # constructor call
    return Student(name, house)


if __name__ == "__main__":
    main()
