n,m = tuple(map(int,input().split()))
pairs = [
    tuple(map(int,input().split()))
    for _ in range(m)
]

ans = 0
for x in range(n+1):
    for y in range(x+1,n+1):
        cnt = 0
        for a,b in pairs:
            if x==a and y==b or x==b and y==a:
                cnt += 1
        ans = max(ans,cnt)

print(ans)