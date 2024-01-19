class Point:
    def __init__(self, x=0, y=0, num=0):
        self.x = x
        self.y = y
        self.num = num

n = int(input())
points = []
for i in range(1,n+1):
    x,y = tuple(map(int,input().split()))
    points.append(Point(x,y,i))

points.sort(key = lambda p: (abs(p.x)+abs(p.y), p.num))
for point in points:
    print(point.num)