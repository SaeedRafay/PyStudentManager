students = []


class Student:

    def __init__(self, first_name, last_name, student_id="SE-0000"):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student Added: " + self.first_name + " " + self.last_name


mark = Student("mark", "smith")
print(mark)