n = int(input())
coins = [
    list(map(int,input().split()))
    for _ in range(n)
]
ans = 0
for i in range(n):
    for j in range(n-2):
        ans = max(ans, coins[i][j]+coins[i][j+1]+coins[i][j+2])
print(ans)