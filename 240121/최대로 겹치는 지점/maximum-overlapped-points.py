n = int(input())
segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
points = [0] * 101
for a,b in segments:
    for i in range(a,b+1):
        points[i] += 1
print(max(points[1:]))