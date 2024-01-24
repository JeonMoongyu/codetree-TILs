n,m = tuple(map(int,input().split()))
arr = [
    list(input())
    for _ in range(n)
]


def in_range(i,j):
    return 0<=i and i<n and 0<=j and j<m


dis, djs = [0,-1,-1,-1,0,1,1,1], [1,1,0,-1,-1,-1,0,1]

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            for di,dj in zip(dis,djs):
                if in_range(i+di,j+dj) and in_range(i+di*2,j+dj*2) and\
                   arr[i+di][j+dj]=='E' and arr[i+di*2][j+dj*2]=='E':
                   ans += 1

print(ans)