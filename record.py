import csv


class Record:

    def save_file(self, student_id, first_name, last_name):
        try:
            with open("students.csv", "a", newline="\n", encoding="utf-8") as inp:
                writer = csv.writer(inp)
                writer.writerow([student_id, first_name, last_name])
        except Exception:
            print("Could not save file")

    def read_file(self):
        students = []
        try:
            with open("students.csv", "r") as out:
                for row in csv.reader(out):
                    students.append(row)
            print(students)
        except Exception:
            print("Could not read file")

    def delete_row(self, student_id):
        students = []
        try:
            with open("students.csv", "r") as out:
                for row in csv.reader(out):
                    if row[0] != student_id:
                        students.append(row)
            print(students)
            with open("students.csv", "w", newline="\n", encoding="utf-8") as inp:
                writer = csv.writer(inp)
                for student in students:
                    writer.writerow(student)
        except Exception:
            print("Could not delete record")