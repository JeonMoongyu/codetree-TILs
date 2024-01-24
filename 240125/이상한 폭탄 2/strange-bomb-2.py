n,k = tuple(map(int,input().split()))
bombs = [
    int(input())
    for _ in range(n)
]

ans = -1
for i in range(n-k):
    exists = False
    for j in range(i+1,i+k+1):
        if bombs[j] == bombs[i]:
            exists = True
            break
    if exists:
        ans = max(ans,bombs[i])

print(ans)