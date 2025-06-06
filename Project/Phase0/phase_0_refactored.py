# Refactored Phase 0 Projects in Python (Improved Structure and Readability)

# 1️⃣ Student Management System
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

# 2️⃣ Maze Path Finder (DFS)
def find_path(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    path = []

    def dfs(x, y):
        if not (0 <= x < rows and 0 <= y < cols) or maze[x][y] == 1 or visited[x][y]:
            return False
        path.append((x, y))
        visited[x][y] = True
        if (x, y) == (rows - 1, cols - 1):
            return True
        if dfs(x+1, y) or dfs(x, y+1) or dfs(x-1, y) or dfs(x, y-1):
            return True
        path.pop()
        return False

    if dfs(0, 0):
        print("Path found:", path)
    else:
        print("No path found")

# 3️⃣ Queue System Simulation
from collections import deque

def queue_system():
    q = deque()
    ticket = 1
    while True:
        action = input("\n1. Take a number\n2. Call next\n3. Exit\nSelect: ")
        if action == '1':
            q.append(f"A{ticket:03d}")
            print(f"Your number is: A{ticket:03d}")
            ticket += 1
        elif action == '2':
            print("Next:", q.popleft() if q else "No one in queue")
        elif action == '3':
            break

# 4️⃣ Expression Evaluator (Infix to Postfix)
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output, stack = [], []
    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    output.extend(reversed(stack))
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(eval(f"{a}{token}{b}"))
    return stack[0]

def expression_evaluator():
    expr = input("Enter infix expression (space-separated): ")
    postfix = infix_to_postfix(expr)
    print("Postfix:", postfix)
    print("Result:", evaluate_postfix(postfix))

# Run All Modules Interactively (Optional)
if __name__ == '__main__':
    print("Select Project to Run:\n1. Student Manager\n2. Maze Path\n3. Queue System\n4. Expression Evaluator")
    choice = input("Enter number: ")
    if choice == '1':
        StudentManager().run()
    elif choice == '2':
        test_maze = [
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 0, 0]
        ]
        find_path(test_maze)
    elif choice == '3':
        queue_system()
    elif choice == '4':
        expression_evaluator()
