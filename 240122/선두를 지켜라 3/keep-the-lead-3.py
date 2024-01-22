n, m = tuple(map(int,input().split()))

a = [0]
for _ in range(n):
    v, t = tuple(map(int,input().split()))
    for _ in range(t):
        a.append(a[-1]+v)

b = [0]
for _ in range(m):
    v, t = tuple(map(int,input().split()))
    for _ in range(t):
        b.append(b[-1]+v)


def comp(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1


ans = 0
for t in range(1,len(a)):
    if comp(a[t-1],b[t-1]) != comp(a[t],b[t]):
        ans += 1
print(ans)