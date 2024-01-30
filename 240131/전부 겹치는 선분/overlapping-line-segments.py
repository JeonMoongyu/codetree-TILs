n = int(input())
c1, c2 = 1, 100
for _ in range(n):
    x1, x2 = tuple(map(int,input().split()))
    c1 = max(c1,x1)
    c2 = min(c2,x2)

if c2 < c1:
    print("No")
else:
    print("Yes")