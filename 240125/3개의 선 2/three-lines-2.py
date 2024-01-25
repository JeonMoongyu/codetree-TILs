import sys

n = int(input())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


def count_x(arr):
    cnt = [0] * 11
    for x,y in arr:
        cnt[x] = 1
    return sum(cnt)


def count_y(arr):
    cnt = [0] * 11
    for x,y in arr:
        cnt[y] = 1
    return sum(cnt)


if count_x(points) <= 3 or count_y(points) <= 3:
    print(1)
    sys.exit()
else:
    for x_rem in range(11):
        points_rem = [ points[i] for i in range(n) if points[i][0] != x_rem ]
        if count_y(points_rem) <= 2:
            print(1)
            sys.exit()
    for y_rem in range(11):
        points_rem = [ points[i] for i in range(n) if points[i][1] != y_rem ]
        if count_x(points_rem) <= 2:
            print(1)
            sys.exit()
print(0)