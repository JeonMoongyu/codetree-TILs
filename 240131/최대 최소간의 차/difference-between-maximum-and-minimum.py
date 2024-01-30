n,k = tuple(map(int,input().split()))
arr = list(map(int,input().split()))


def cost(m):  # m ~ m+k
    result = 0
    for elem in arr:
        if elem < m:
            result += m - elem
        if elem > m + k:
            result += elem - m - k
    return result


ans = 10000 * 100
for m in range(1,10000):
    ans = min(ans, cost(m))

print(ans)