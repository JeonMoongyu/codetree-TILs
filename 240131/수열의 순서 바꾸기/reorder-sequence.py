n = int(input())
arr = list(map(int,input().split()))

ans = 0
while arr != [ k for k in range(1,n+1) ]:
    for i in range(1,n):
        if arr[i] == (arr[0] - 1 if arr[0] > 1 else n):
            arr = arr[1:i+1] + [arr[0]] + arr[i+1:]
            ans += 1
            break

print(ans)