students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

# anon function that takes "student" as param
# and returns key to sort by
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

"""
# list comprehension with conditional
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
"""
