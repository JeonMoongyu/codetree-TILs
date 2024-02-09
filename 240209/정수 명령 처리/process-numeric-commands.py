class Stack:
    def __init__(self):
        self.items = []
    

    def push(self, data):
        self.items.append(data)
    

    def size(self):
        return len(self.items)
    

    def empty(self):
        return not self.items
    

    def top(self):
        if not self.empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")
    

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")


n = int(input())
stack = Stack()
for _ in range(n):
    command = input()

    if command.startswith("push"):
        num = int(command.split()[1])
        stack.push(num)
    
    elif command == "pop":
        print(stack.pop())
    
    elif command == "size":
        print(stack.size()) 
    
    elif command == "empty":
        if stack.empty():
            print(1)
        else:
            print(0)
    
    else:
        print(stack.top())