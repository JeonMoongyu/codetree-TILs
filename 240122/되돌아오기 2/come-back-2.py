commands = input()
dxs, dys = [1,0,-1,0], [0,1,0,-1]
x, y = 0, 0
direc = 1
ans = -1
for i in range(len(commands)):  
    if commands[i] == "F":
        x += dxs[direc]
        y += dys[direc]
        if x==0 and y==0:
            ans = i+1
            break
    elif commands[i] == "L":
        direc = (direc+1)%4
    else:
        direc = (direc+3)%4

print(ans)