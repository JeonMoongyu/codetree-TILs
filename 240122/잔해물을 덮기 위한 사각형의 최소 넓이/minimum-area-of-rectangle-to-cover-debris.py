plane = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

for k in range(1,-1,-1):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    for i in range(x1+1000,x2+1000):
        for j in range(y1+1000,y2+1000):
            plane[i][j] = k

a1,b1,a2,b2 = 2000,2000,0,0
is_all_0 = True
for i in range(2000):
    for j in range(2000):
        if plane[i][j] == 1:
            is_all_0 = False
            a1 = min(a1,i)
            b1 = min(b1,j)
            a2 = max(a2,i)
            b2 = max(b2,j)

if is_all_0:
    print(0)
else: 
    print( (a2-a1+1)*(b2-b1+1) )