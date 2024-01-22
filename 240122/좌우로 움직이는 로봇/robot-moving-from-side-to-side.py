n, m = tuple(map(int,input().split()))

a = [0]
for _ in range(n):
    t, d = input().split()
    t = int(t)
    d = 1 if d == 'R' else -1
    for __ in range(t):
        a.append(a[-1]+d)       

b = [0]
for _ in range(n):
    t, d = input().split()
    t = int(t)
    d = 1 if d == 'R' else -1
    for __ in range(t):
        b.append(b[-1]+d) 

ans = 0
for i in range(2,len(a)):
    if a[i-1] != b[i-1] and a[i] == b[i]:
        ans += 1
print(ans)