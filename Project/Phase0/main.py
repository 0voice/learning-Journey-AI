from student_manager import StudentManager
from maze_path_finder import find_path
from queue_system import queue_system
from expression_evaluator import expression_evaluator

if __name__ == '__main__':
    print("Select Project to Run:")
    print("1. Student Manager")
    print("2. Maze Path")
    print("3. Queue System")
    print("4. Expression Evaluator")

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
