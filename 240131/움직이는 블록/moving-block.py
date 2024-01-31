n = int(input())
arr = [ int(input()) for _ in range(n) ]
avg = sum(arr)//n
ans = 0
for elem in arr:
    if elem > avg:
        ans += elem - avg
print(ans)