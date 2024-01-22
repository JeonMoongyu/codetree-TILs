n, t = tuple(map(int,input().split()))
commands = input()
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]


def in_range(i,j):
    return 0<=i and i<n and 0<=j and j<n


di, dj = [0,-1,0,1], [1,0,-1,0] #ENWS
dir_num = 1
i, j = (n-1)//2, (n-1)//2
sum_val = 0
sum_val += arr[i][j]
for command in commands:
    if command == 'F' and in_range(i+di[dir_num],j+dj[dir_num]):
        i += di[dir_num]
        j += dj[dir_num]
        sum_val += arr[i][j]
    elif command == 'L':
        dir_num = (dir_num+1)%4
    elif command == 'R':
        dir_num = (dir_num+3)%4
print(sum_val)