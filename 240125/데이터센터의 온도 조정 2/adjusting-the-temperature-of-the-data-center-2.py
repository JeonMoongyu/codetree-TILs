n,c,g,h = tuple(map(int,input().split()))
temp = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

min_temp = sorted(temp, key= lambda x: x[0])[0][0]
max_temp = sorted(temp, key= lambda x: x[1])[n-1][1]
left_end = max(0,min_temp-1)
right_end = max_temp+5

work = [0] * (right_end+1)
for ta,tb in temp:
    for t in range(left_end,ta):
        work[t] += c
    for t in range(ta,tb):
        work[t] += g
    for t in range(tb,right_end+1):
        work[t] += h
print(max(work))