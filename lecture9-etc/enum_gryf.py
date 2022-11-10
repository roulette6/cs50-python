students = ["Hermione", "Harry", "Ron"]

"""
# instead of this
for i in range(len(students)):
    print(i + 1, students[i])
"""

# no need to index into each list position
# as above
for i, student in enumerate(students):
    print(i + 1, student)