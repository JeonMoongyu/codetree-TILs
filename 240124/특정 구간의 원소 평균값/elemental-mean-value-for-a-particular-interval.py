n = int(input())
arr = list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(i,n):
        sum_val = 0
        for k in range(i,j+1):
            sum_val += arr[k]
        if sum_val%(j-i+1) != 0:
            continue
        avg_val = sum_val // (j-i+1)
        for k in range(i,j+1):
            if avg_val == arr[k]:
                ans += 1
                break
print(ans)