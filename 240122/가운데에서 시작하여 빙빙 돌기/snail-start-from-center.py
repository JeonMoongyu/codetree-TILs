n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_range(i,j):
    return 0<=i and i<n and 0<=j and j<n

di, dj = [0,1,0,-1], [1,0,-1,0]
dir_num = 2
i, j = n-1, n-1
arr[i][j] = n*n
for _ in range(n*n-1):
    ni, nj = i + di[dir_num], j + dj[dir_num] 
    if not in_range(ni,nj) or arr[ni][nj] != 0:
        dir_num = (dir_num+1)%4
        ni, nj = i + di[dir_num], j + dj[dir_num] 
    arr[ni][nj] = arr[i][j] - 1
    i, j = ni, nj

for row in arr:
    for ent in row:
        print(ent, end=" ")
    print()