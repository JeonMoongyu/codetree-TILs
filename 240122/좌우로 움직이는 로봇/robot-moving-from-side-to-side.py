n, m = tuple(map(int,input().split()))

a = [0]
for _ in range(n):
    t, d = input().split()
    t = int(t)
    d = 1 if d == 'R' else -1
    for __ in range(t):
        a.append(a[-1]+d)       

b = [0]
for _ in range(m):
    t, d = input().split()
    t = int(t)
    d = 1 if d == 'R' else -1
    for __ in range(t):
        b.append(b[-1]+d) 

if len(a) > len(b):
    length = len(a)
    b += [ b[-1] for _ in range(len(a)-len(b)) ]
elif len(a) < len(b):
    length = len(b)
    a += [ a[-1] for _ in range(len(b)-len(a)) ]

ans = 0
for i in range(1,length):
    if a[i-1] != b[i-1] and a[i] == b[i]:
        ans += 1
print(ans)