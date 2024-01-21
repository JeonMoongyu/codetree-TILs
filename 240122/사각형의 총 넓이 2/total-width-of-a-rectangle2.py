n = int(input())
plane = [
    [0 for _ in range(200)]
    for _ in range(200)
]

for _ in range(n):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    for i in range(x1+100,x2+100):
        for j in range(y1+100,y2+100):
            plane[i][j] = 1

area = 0
for i in range(200):
    for j in range(200):
        area += plane[i][j]
print(area)