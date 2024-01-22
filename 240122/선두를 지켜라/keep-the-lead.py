n,m = tuple(map(int,input().split()))
a = [0]
for _ in range(n):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        a.append(a[-1]+v)
b = [0]
for _ in range(m):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        b.append(b[-1]+v)


ans = 0
head = ""
for i in range(1,len(a)):
    if head == "" and a[i]!=b[i]:
        head = 'A' if a[i]>b[i] else 'B'
    elif head == 'A' and a[i]<b[i]:
        ans += 1
        head = 'B'
    elif head == 'B' and a[i]>b[i]:
        ans += 1
        head = 'A'

print(ans)