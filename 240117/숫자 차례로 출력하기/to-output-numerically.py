def f(n):
    if n == 0:
        return
    print(n, end=" ")
    f(n-1)

def g(n):
    if n==0:
        return
    g(n-1)
    print(n, end=" ")

n = int(input())
g(n)
print()
f(n)