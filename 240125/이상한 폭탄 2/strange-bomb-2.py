n,k = tuple(map(int,input().split()))
bombs = [
    int(input())
    for _ in range(n)
]


def in_range(i):
    return 0<=i and i<n

ans = -1
for i in range(n):
    for j in range(i+1,n):
        if j-i > k:
            continue
        if bombs[i] == bombs[j]:
            ans = max(ans,bombs[i])

print(ans)