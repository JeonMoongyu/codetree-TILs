n,k = tuple(map(int,input().split()))
bombs = [
    int(input())
    for _ in range(n)
]


def in_range(i):
    return 0<=i and i<n

ans = -1
for i in range(n):
    exists = False
    for j in range(i+1,i+k+1):
        if in_range(j) and bombs[j] == bombs[i]:
            exists = True
            break
    if exists:
        ans = max(ans,bombs[i])

print(ans)