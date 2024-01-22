n = int(input())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)


orig_dist = 0
for i in range(n-1):
    x1,y1 = points[i]
    x2,y2 = points[i+1]
    orig_dist += dist(x1,y1,x2,y2)

min_dist = orig_dist
for j in range(1,n-1):
    x0,y0 = points[j-1]
    x1,y1 = points[j]
    x2,y2 = points[j+1]
    cheated_dist = orig_dist - dist(x0,y0,x1,y1) - dist(x1,y1,x2,y2) + dist(x0,y0,x2,y2) 
    min_dist = min(min_dist,cheated_dist)

print(min_dist)