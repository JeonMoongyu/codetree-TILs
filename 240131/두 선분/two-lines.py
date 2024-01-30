x1,x2,x3,x4 = tuple(map(int,input().split()))

intersecting = True

if x2 < x3:
    intersecting = False
if x4 < x1:
    intersecting = False

answer = "intersecting" if intersecting else "nonintersecting"
print(answer)