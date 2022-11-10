"""
set is a data type that doesn't allow duplicates
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

"""
# A set automatically does what I did below
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

"""
