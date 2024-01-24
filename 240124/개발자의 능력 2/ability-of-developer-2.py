arr = list(map(int,input().split()))


def max_diff(a,b,c):
    return max(abs(a-b),abs(a-c),abs(b-c))


ans = 2000000
for i1 in range(6):
    for i2 in range(i1+1,6):
        for j1 in range(6):
            for j2 in range(j1+1,6):
                if j1 == i1 or j1 == i2 or j2 == i1 or j2 == i2:
                    continue
                sum1 = arr[i1] + arr[i2]
                sum2 = arr[j1] + arr[j2]
                sum3 = sum(arr) - sum1 - sum2
                ans = min(ans,max_diff(sum1,sum2,sum3))

print(ans)