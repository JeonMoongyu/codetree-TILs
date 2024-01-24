n,m = tuple(map(int,input().split()))
a_seq = list(map(int,input().split()))
b_seq = list(map(int,input().split()))

ans = 0
for i in range(n-m+1):
    if sorted(a_seq[i:i+m]) == sorted(b_seq):
        ans += 1

print(ans)