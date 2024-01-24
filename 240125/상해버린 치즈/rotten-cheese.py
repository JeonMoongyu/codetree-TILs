n,m,d,s = tuple(map(int,input().split()))
data = [
    tuple(map(int,input().split()))
    for _ in range(d)
]
sick = [
    tuple(map(int,input().split()))
    for _ in range(s)
]

ans = 0
for cheese in range(1,m+1):
    
    time = [0] * (n+1)
    for p,c,t in data:
        if c != cheese:
            continue
        if time[p] == 0:
            time[p] = t
        elif time[p] > t:
            time[p] = t

    possible = True
    for p,t in sick:
        if time[p] == 0:
            possible = False
        if time[p] >= t:
            possible = False
    
    if possible:
        pill = 0
        for t in time[1:]:
            if t != 0:
                pill += 1
        ans = max(ans,pill)

print(ans)