n = int(input())
dx, dy = [1,-1,0,0],[0,0,-1,1]
x, y = 0, 0

def d_num(direc):
    if direc == 'E':
        return 0
    if direc == 'W':
        return 1
    if direc == 'S':
        return 2
    else:
        return 3

for _ in range(n):
    direc, dist = input().split()
    direc = d_num(direc)
    dist = int(dist)
    x += dx[direc] * dist
    y += dy[direc] * dist

print(x,y)