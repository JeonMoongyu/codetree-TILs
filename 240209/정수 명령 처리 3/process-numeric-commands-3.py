from collections import deque

n = int(input())
dq = deque()
for _ in range(n):
    command = input()

    if command.startswith("push_front"):
        num = int(command.split()[1])
        dq.appendleft(num)
    
    elif command.startswith("push_back"):
        num = int(command.split()[1])
        dq.append(num)
    
    elif command == "pop_front":
        print(dq.popleft())
    
    elif command == "pop_back":
        print(dq.pop())
    
    elif command == "size":
        print(len(dq))
    
    elif command == "empty":
        print(0 if dq else 1)
    
    elif command == "front":
        print(dq[0])
    
    else:
        print(dq[-1])