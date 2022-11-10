students = ["Hermione", "Harry", "Ron"]

# dict comprehension
# create dict whose keys will be the name of the students
# in the list indicated
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
