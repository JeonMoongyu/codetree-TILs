n,m = tuple(map(int,input().split()))
grid = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]


def in_range(i,j):
    return 1<=i and i<=n and 1<=j and j<=n


dis, djs = [0,0,1,-1], [1,-1,0,0]


def is_comfortable(i,j):
    cnt = 0
    for d in range(4):
        ni, nj = i+dis[d], j+djs[d] 
        if in_range(ni,nj):
            cnt += grid[ni][nj]
    return cnt == 3
    

for _ in range(m):
    r, c = tuple(map(int,input().split()))
    grid[r][c] = 1
    if is_comfortable(r,c):
        print(1)
    else:
        print(0)