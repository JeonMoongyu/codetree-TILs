n = int(input())

commands = []
for _ in range(n):
    x, sgn = input().split()
    commands.append((int(x),sgn))

line = [0]*2000 # offset is 1000

curr = 1000 # offset is considered
for x,sgn in commands:
    if sgn == 'L':
        for i in range(x):
            line[curr-i-1] += 1
        curr -= x
    if sgn == 'R':
        for i in range(x):
            line[curr+i] += 1
        curr += x

cnt = 0
for elem in line:
    if elem >= 2:
        cnt += 1
print(cnt)