a, b = tuple(map(int,input().split()))
c, d = tuple(map(int,input().split()))

if d < a or b < c:
    print(b-a+d-c)
else:
    print(max(b,d)-min(a,c))