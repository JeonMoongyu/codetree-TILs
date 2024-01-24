arr = list(map(int,input().split()))


def are_all_diff(a,b,c):
    return a!=b and b!=c and a!=c


def max_diff(a,b,c):
    return max(abs(a-b),abs(b-c),abs(a-c))


ans = 2001
for i in range(5):
    for j in range(5):
        for k in range(j+1,5):
            if i==j or i==k:
                continue
            sum1 = arr[i]
            sum2 = arr[j] + arr[k]
            sum3 = sum(arr) - sum1 - sum2
            if are_all_diff(sum1,sum2,sum3):
                ans = min(ans,max_diff(sum1,sum2,sum3))
if ans == 2001:
    print(-1)
else:
    print(ans)