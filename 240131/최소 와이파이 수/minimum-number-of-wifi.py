n, m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

ans = 0
curr = 0
while curr <= n-1:
    if arr[curr] == 1:
        ans += 1
        curr += 2*m + 1
    else: # arr[curr] == 0
        curr += 1
    
print(ans)