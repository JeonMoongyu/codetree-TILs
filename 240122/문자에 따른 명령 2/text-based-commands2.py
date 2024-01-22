commands = input()
dx, dy = [0,-1,0,1], [1,0,-1,0]
x, y = 0, 0
dir_num = 0
for com in commands:
    if com == 'L':
        dir_num = (dir_num+1)%4
    elif com == 'R':
        dir_num = (dir_num+3)%4
    else:
        x += dx[dir_num]
        y += dy[dir_num]
print(x,y)