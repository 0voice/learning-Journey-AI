class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}"

class StudentManager:
    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.student_id] = student

    def remove(self, student_id):
        self.students.pop(student_id, None)

    def display(self):
        for student in self.students.values():
            print(student)

    def run(self):
        while True:
            cmd = input("\n1. Add\n2. Remove\n3. Display\n4. Exit\nSelect option: ")
            if cmd == '1':
                name = input("Name: ")
                age = input("Age: ")
                sid = input("Student ID: ")
                self.add(Student(name, age, sid))
            elif cmd == '2':
                sid = input("Enter ID to remove: ")
                self.remove(sid)
            elif cmd == '3':
                self.display()
            elif cmd == '4':
                break
