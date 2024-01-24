n,k = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

ans = 0
for i in range(n-k+1):
    sum_val = sum(arr[i:i+k])
    ans = max(ans,sum_val)

print(ans)