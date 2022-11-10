import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


"""
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


# anon function that takes "student" as param and
# returns key to sort by
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""

"""
def get_name(student):
    return student["name"]

# sort list of dicts by key indicated in get_name function
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

"""