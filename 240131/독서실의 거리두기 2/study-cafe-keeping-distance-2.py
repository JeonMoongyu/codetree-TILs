n = int(input())
arr = list(map(int,list(input())))

indices = [ i for i in range(n) if arr[i]==1 ]
distances = [ indices[j+1]-indices[j] for j in range(len(indices)-1) ]

ans = 0
if arr[0] == 0:
    ans = max(ans,min(indices[0],min(distances)))
if arr[-1] == 0:
    ans = max(ans,min(n-1-indices[-1],min(distances)))

idx = 0
for k in range(len(distances)):
    if distances[k] > distances[idx]:
        idx = k

distances[k] //= 2
ans = max(ans,min(distances))

print(ans)