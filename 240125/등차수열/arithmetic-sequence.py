n = int(input())
seq = list(map(int,input().split()))

ans = 0
for k in range(1,101):
    for i in range(n):
        for j in range(i+1,n):
            if 2*k == seq[i] + seq[j]:
                ans += 1

print(ans)