n,s = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
total_sum = sum(arr)

ans = 20000
for i in range(n):
    for j in range(i+1,n):
        sum_val = total_sum - arr[i] - arr[j]
        ans = min(ans,abs(sum_val-s))

print(ans)