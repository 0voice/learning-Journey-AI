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
