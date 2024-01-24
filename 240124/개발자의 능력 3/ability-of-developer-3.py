arr = list(map(int,input().split()))

total_sum = sum(arr)


def get_diff(i,j,k):
    sum1 = arr[i]+arr[j]+arr[k]
    sum2 = total_sum - sum1
    return abs(sum1-sum2)


ans = 3000000
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            ans = min(ans,get_diff(i,j,k))

print(ans)