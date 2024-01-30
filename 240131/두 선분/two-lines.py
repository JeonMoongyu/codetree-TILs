x1,x2,x3,x4 = tuple(map(int,input().split()))

intersecting = False

if x3 <= x1 and x1 <= x4:
    intersecting = True
if x3 <= x2 and x2 <= x4:
    intersecting = True

answer = "intersecting" if intersecting else "nonintersecting"
print(answer)