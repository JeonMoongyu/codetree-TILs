k,n = tuple(map(int,input().split()))
data1 = [
    list(map(int,input().split()))
    for _ in range(k)
]
data2 = [
    [ (data1[i][j],j+1) for j in range(n)]
    for i in range(k)
]
for i in range(k):
    data2[i].sort(key = lambda x: x[0])

ans = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            continue
        satisfied = True
        for a_match in data2:
            if a_match[a-1][1] > a_match[b-1][1]:
                satisfied = False
        if satisfied:
            ans += 1

print(ans)