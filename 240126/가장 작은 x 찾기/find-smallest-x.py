import sys

n = int(input())
data = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

for x in range(1, data[0][1]):
    satisfied = True
    curr_x = x
    for a,b in data:
        curr_x *= 2
        if curr_x < a or curr_x > b:
            satisfied = False
            break
    if satisfied:
        print(x)
        sys.exit()