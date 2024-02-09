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


string = input()
stack = Stack()
answer = True
for ch in string:
    if ch == '(':
        stack.push(1)
    else:
        if stack.empty():
            answer = False
        else:
            stack.pop()
if not stack.empty():
    answer = False

if answer:
    print("Yes")
else:
    print("No")