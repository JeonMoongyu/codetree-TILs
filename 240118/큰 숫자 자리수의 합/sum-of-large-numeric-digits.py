def f(n):
    if n < 10:
        return n
    return f(n//10) + n%10

a,b,c = tuple(map(int,input().split()))
print(f(a*b*c))