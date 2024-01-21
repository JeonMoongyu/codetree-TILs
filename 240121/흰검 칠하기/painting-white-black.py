n= int(input())
tiles = [("",0,0)] * 200000

commands = []
for _ in range(n):
    x,s = input().split()
    commands.append((int(x),s))

curr = 0
for x,s in commands:
    if s == 'L':
        for i in range(x):
            c,w,b = tiles[curr-i]
            c = "W"
            w += 1
            tiles[curr-i] = (c,w,b)
        curr -= x-1
    else:
        for i in range(x):
            c,w,b = tiles[curr+i]
            c = "B"
            b += 1
            tiles[curr+i] = (c,w,b)
        curr += x-1

cnt = [0,0,0]
for c,w,b in tiles:
    if w >= 2 and b >= 2:
        cnt[2] += 1
    elif c == "W":
        cnt[0] += 1
    elif c == "B":
        cnt[1] += 1
for num in cnt:
    print(num, end=" ")