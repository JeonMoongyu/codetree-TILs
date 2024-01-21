plane = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

for _ in range(2):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    for i in range(x1+1000,x2+1000):
        for j in range(y1+1000,y2+1000):
            plane[i][j] = 1

x1,y1,x2,y2 = tuple(map(int,input().split()))
for i in range(x1+1000,x2+1000):
    for j in range(y1+1000,y2+1000):
        plane[i][j] = 0

area = 0
for i in range(2000):
    for j in range(2000):
        area += plane[i][j]
print(area)