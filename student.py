import record


class Student:

    def __init__(self):
        show_records = record.Record()
        show_records.read_file()

    def add_student(self, first_name, last_name, student_id="SE-0000"):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.student_id = student_id
        new_student = record.Record()
        new_student.save_file(self.student_id, self.first_name, self.last_name)
        print("New Student Added")

    def delete_student(self):
        student_id = input("What's the Student ID: ")
        remove_student = record.Record()
        remove_student.delete_row(student_id)


mark = Student()
# mark.add_student("Olivia", "woodSmith", "SE-0007")
# mark.delete_student()