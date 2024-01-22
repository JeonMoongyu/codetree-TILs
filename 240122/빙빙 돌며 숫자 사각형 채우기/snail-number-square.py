n,m = tuple(map(int,input().split()))
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
d = 0
dis, djs = [0,1,0,-1], [1,0,-1,0]


def in_range(i,j):
    return 0<=i and i<n and 0<=j and j<n


i, j = 0, 0
arr[i][j] = 1
for _ in range(n*m-1):
    ni, nj = i+dis[d], j+djs[d]
    if not in_range(ni,nj) or arr[ni][nj] != 0:
        d = (d+1)%4
        ni, nj = i+dis[d], j+djs[d]
    arr[ni][nj] = arr[i][j] + 1
    i, j = ni, nj

for row in arr:
    for ent in row:
        print(ent, end=" ")
    print()