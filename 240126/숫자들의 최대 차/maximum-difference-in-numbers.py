n,k = tuple(map(int,input().split()))
elts = [ int(input()) for _ in range(n) ]

ans = 0
for m in range(1,10001-k):
    cnt = 0
    for elem in elts:
        if m <= elem and elem <= m+k:
            cnt += 1
    ans = max(ans,cnt)

print(ans)