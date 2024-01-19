def f(a,b):
    return 60*a + b

a,b,c,d = tuple(map(int,input().split()))
print(f(c,d)-f(a,b))