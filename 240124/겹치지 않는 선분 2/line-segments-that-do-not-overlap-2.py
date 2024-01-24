n = int(input())
segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i,(x1,x2) in enumerate(segments):
    overlap = False
    for j,(z1,z2) in enumerate(segments):
        if i == j:
            continue
        if (x1-z1) * (x2-z2) < 0:
            overlap = True
    if not overlap:
        ans += 1

print(ans)