n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
for i in range(n-1):
    a[i+1] = a[i] - b[i] + a[i+1]
    ans += a[i] - b[i]

print(ans)