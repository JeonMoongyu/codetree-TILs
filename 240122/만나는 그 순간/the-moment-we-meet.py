n, m = tuple(map(int,input().split()))
a = [0]
for _ in range(n):
    d, t = input().split()
    t = int(t)
    d = -1 if d == 'L' else 1
    for _ in range(t):
        a.append(a[-1]+d)
b= [0]
for _ in range(m):
    d, t = input().split()
    t = int(t)
    d = -1 if d == 'L' else 1
    for _ in range(t):
        b.append(b[-1]+d)
when = 0
for i in range(1,len(a)):
    if a[i] == b[i]:
        when = i
        break
print(when)