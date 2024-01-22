n, t = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
ans, cnt = 0, 0
for elem in arr:
    if elem > t:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)