n = int(input())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
area = 40000*40000
for i in range(n):
    x_left, x_right, y_bot, y_top = 40000,1,40000,1
    for j in range(n):
        if j == i:
            continue
        x, y = points[j]
        x_left = min(x_left,x)
        x_right = max(x_right,x)
        y_bot = min(y_bot,y)
        y_top = max(y_top,y)
    area = min(area, (y_top-y_bot)*(x_right-x_left))
print(area)