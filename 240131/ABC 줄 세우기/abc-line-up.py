n = int(input())


def alp_to_num(x):  # 'A' to 0, 'Z' to 25
    return ord(x)-ord('A')


arr = list(input().split())
for i in range(n):
    arr[i] = alp_to_num(arr[i])


ans = 0
for i in range(n-1):
    for j in range(i,n):
        if arr[j] == i:
            ans += j-i
            for k in range(j,i,-1):
                arr[k] = arr[k-1]
            arr[i] = i
print(ans)