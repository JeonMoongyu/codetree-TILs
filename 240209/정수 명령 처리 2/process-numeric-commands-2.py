from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    
    def push(self, item):
        self.dq.append(item)
    

    def empty(self):
        return not self.dq

    
    def size(self):
        return len(self.dq)
    

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
    

    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq[0]


n = int(input())
queue = Queue()
for _ in range(n):
    command = input()

    if command.startswith("push"):
        num = int(command.split()[1])
        queue.push(num)
    
    elif command == "pop":
        print(queue.pop())

    elif command == "size":
        print(queue.size())
    
    elif command == "empty":
        if queue.empty():
            print(1)
        else:
            print(0)
    
    else:
        print(queue.front())