n = int(input())
arr = list(map(int,input().split()))

ans = 99*100
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        curr_arr = [ arr[k] for k in range(n) if k!=j ]
        sum_of_diff = 0
        for k in range(n-2):
            sum_of_diff += abs(curr_arr[k+1] - curr_arr[k])
        ans = min(ans,sum_of_diff)
    arr[i] //= 2
print(ans)