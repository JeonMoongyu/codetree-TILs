n = int(input())

commands = []
for _ in range(n):
    x,s = input().split()
    commands.append((int(x),s))

white = [0] * 200000
black = [0] * 200000
curr = 100000
for x,s in commands:
    if s == 'L':
        for i in range(x):
            white[curr-i] = 1
            black[curr-i] = 0
        curr -= x-1
    elif s == 'R':
        for i in range(x):
            white[curr+i] = 0
            black[curr+i] = 1
        curr += x-1

print(sum(white), sum(black))