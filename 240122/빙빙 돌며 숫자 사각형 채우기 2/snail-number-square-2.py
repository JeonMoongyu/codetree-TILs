n, m = tuple(map(int,input().split()))
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
di, dj = [0,-1,0,1], [1,0,-1,0] # E,N,W,S


def is_range(i,j):
    return 0<=i and i<n and 0<=j and j<m


i, j = 0, 0
dir_num = 3
arr[i][j] = 1
for k in range(2,n*m+1):
    ni, nj = i + di[dir_num], j + dj[dir_num]
    if not is_range(ni,nj) or arr[ni][nj] != 0:
        dir_num = (dir_num+1)%4
        ni, nj = i + di[dir_num], j + dj[dir_num]
    arr[ni][nj] = k
    i, j = ni, nj

for row in arr:
    for ent in row:
        print(ent, end=" ")
    print()