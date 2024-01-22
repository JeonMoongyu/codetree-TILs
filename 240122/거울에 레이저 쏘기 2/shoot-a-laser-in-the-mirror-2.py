n = int(input())
grid = [
    list(input())
    for _ in range(n)
]

k = int(input())
if (k-1) // n == 0:
    i, j = -1, k-1
    direc = 2
elif (k-1) // n == 1:
    i, j = k-1-n, n
    direc = 1
elif (k-1) // n == 2:
    i, j = n, 3*n-k
    direc = 3
else:
    i, j = 4*n-k, -1
    direc = 0

di, dj = [0,0,1,-1], [1,-1,0,0] # E,W,S,N


def next_dir(direc, mirror):
    if mirror == "\\":
        return (direc+2)%4
    if mirror == "/":
        return (3-direc)%4


def is_range(i,j):
    return 0<=i and i<n and 0<=j and j<n


ans = 0
while True:
    ni, nj = i+di[direc], j+dj[direc]
    if not is_range(ni,nj):
        break
    else:
        direc = next_dir(direc, grid[ni][nj])
        ans += 1
        i, j = ni, nj

print(ans)