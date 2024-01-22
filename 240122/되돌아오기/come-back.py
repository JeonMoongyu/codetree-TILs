n = int(input())
mapper = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}
dxs, dys = [1,-1,0,0], [0,0,-1,1]
x, y = 0, 0

commands = []
for _ in range(n):
    direc, dist = input().split()
    direc = mapper[direc]
    dist = int(dist)
    commands.append((direc,dist))

dxs, dys = [1,-1,0,0], [0,0,-1,1]
x, y = 0, 0
t = 0
ans = -1
for direc, dist in commands:
    for _ in range(dist):
        x += dxs[direc]
        y += dys[direc]
        t += 1
        if x==0 and y==0:
            ans = t
            break
    if ans != -1:
        break

print(ans)