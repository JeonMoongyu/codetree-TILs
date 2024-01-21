n = int(input())
plane = [
    [0 for _ in range(200)]
    for _ in range(200)
]

for _ in range(n):
    x,y = tuple(map(int,input().split()))
    for i in range(x+100,x+108):
        for j in range(y+100,y+108):
            plane[i][j] = 1

area = 0 
for i in range(200):
    for j in range(200):
        area += plane[i][j]
print(area)