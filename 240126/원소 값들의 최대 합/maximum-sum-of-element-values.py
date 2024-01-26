n,m = tuple(map(int,input().split()))
perm = [0] + list(map(int,input().split()))

ans = 0
for i in range(1,n+1):
    sum_val = 0
    for _ in range(m):
        i = perm[i]
        sum_val += perm[i]
    ans = max(ans,sum_val)

print(ans)