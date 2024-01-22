n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
dis, djs = [0,1,0,-1], [1,0,-1,0]


def in_range(i,j):
    return 0<= i and i<n and 0<=j and j<n


ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for di, dj in zip(dis,djs):
            if in_range(i+di,j+dj) and arr[i+di][j+dj] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)