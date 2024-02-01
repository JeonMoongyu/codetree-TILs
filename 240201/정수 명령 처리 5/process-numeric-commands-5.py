n = int(input())
arr = []

for _ in range(n):
    command = list(input().split())
    if command[0] == "push_back":
        arr.append(int(command[1]))
    if command[0] == "pop_back":
        arr.pop()
    if command[0] == "size":
        print(len(arr))
    if command[0] == "get":
        print(arr[int(command[1])-1])