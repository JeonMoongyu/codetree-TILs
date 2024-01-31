n = int(input())
segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

segments.sort(key= lambda x: x[0])
a1 = min([ segments[i][0] for i in range(1,n) ])
a2 = max([ segments[i][1] for i in range(1,n) ])

segments.sort(key= lambda x: x[1])
b1 = min([ segments[i][0] for i in range(n-1) ])
b2 = max([ segments[i][1] for i in range(n-1) ])

print(min(a2-a1,b2-b1))