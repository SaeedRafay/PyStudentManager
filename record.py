import csv


class Record:

    def read_file(self):
        students = []
        try:
            with open("students.csv", "r") as out:
                for row in csv.reader(out):
                    students.append(row)
            print(*students[::-1], sep='\n')
        except Exception:
            print("Could not read file")

    def save_row(self, student_id, first_name, last_name):
        try:
            with open("students.csv", "a", newline="\n", encoding="utf-8") as inp:
                writer = csv.writer(inp)
                writer.writerow([student_id, first_name, last_name])
        except Exception:
            print("Could not save file")

    def delete_row(self, student_id):
        students = []
        try:
            with open("students.csv", "r") as out:
                for row in csv.reader(out):
                    if row[0] != student_id:
                        students.append(row)
            print(*students[::-1], sep='\n')
            with open("students.csv", "w", newline="\n", encoding="utf-8") as inp:
                writer = csv.writer(inp)
                for student in students:
                    writer.writerow(student)
        except Exception:
            print("Could not delete record")