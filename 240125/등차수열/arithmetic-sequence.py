n = int(input())
seq = list(map(int,input().split()))

ans = 0
for k in range(1,101):
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if 2*k == seq[i] + seq[j]:
                cnt += 1
    ans = max(ans,cnt)

print(ans)