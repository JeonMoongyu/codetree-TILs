n = int(input())
segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            points = [0] * 101
            for t in range(n):
                if t == i or t == j or t == k:
                    continue
                a = segments[t][0]
                b = segments[t][1]
                for p in range(a,b+1):
                    points[p] += 1
            if max(points) == 1:
                ans += 1
                

print(ans)