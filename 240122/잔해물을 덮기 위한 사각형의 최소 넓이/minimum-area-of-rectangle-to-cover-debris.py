plane = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

for k in range(1,-1,-1):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    for i in range(x1+1000,x2+1000):
        for j in range(y1+1000,y2+1000):
            plane[i][j] = k

a1,b1,a2,b2 = -1,-1,-1,-1

def is_all_0(arr):
    for elem in arr:
        if elem != 0:
            return False
    return True

for i in range(2000):
    if is_all_0(plane[i]) == False:
        a1 = i
        break
for i in range(1999,-1,-1):
    if is_all_0(plane[i]) == False:
        a2 = i
        break

for j in range(2000):
    col_j = [ plane[i][j] for i in range(2000) ]
    if is_all_0(col_j) == False:
        b1 = j
        break
for j in range(1999,-1,-1):
    col_j = [ plane[i][j] for i in range(2000) ]
    if is_all_0(col_j) == False:
        b2 = j
        break

print( (a2-a1+1)*(b2-b1+1) )