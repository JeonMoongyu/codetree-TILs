n, m = tuple(map(int,input().split()))
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def in_range(i,j):
    return 0<=i and i<n and 0<=j and j<m


di, dj = [0,1,0,-1], [1,0,-1,0] # E,S,W,N
i, j = 0, 0
dir_num = 0
arr[i][j] = 'A'
for _ in range(n*m-1):
    ni, nj = i + di[dir_num], j + dj[dir_num]
    if not in_range(ni,nj) or arr[ni][nj] != 0:
        dir_num = (dir_num+1)%4
        ni, nj = i + di[dir_num], j + dj[dir_num]
    if arr[i][j] == 'Z':
        arr[ni][nj] = 'A'
    else:
        arr[ni][nj] = chr(ord(arr[i][j])+1)
    i, j = ni, nj

for row in arr:
    for ent in row:
        print(ent, end=" ")
    print()