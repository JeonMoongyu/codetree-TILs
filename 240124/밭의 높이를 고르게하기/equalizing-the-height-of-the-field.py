n,h,t = tuple(map(int,input().split()))
heights = list(map(int,input().split()))

ans = 200*t
for i in range(n-t+1):
    cost = 0
    for j in range(i,i+t):
        cost += abs(h-heights[j])
    ans = min(ans,cost)

print(ans)