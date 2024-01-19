def f(a,b,c):
    return 24*60*a + 60*b +c

a,b,c = tuple(map(int,input().split()))
if f(a,b,c) >= f(11,11,11):
    print(f(a,b,c)-f(11,11,11))
else:
    print(-1)