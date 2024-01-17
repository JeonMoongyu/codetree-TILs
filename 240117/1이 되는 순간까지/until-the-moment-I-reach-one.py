def f(n):
    if n == 1:
        return 0
    m = n//2 if n%2==0 else n//3
    return f(m) + 1

n = int(input())
print(f(n))