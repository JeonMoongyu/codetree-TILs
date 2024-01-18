n = int(input())
arr = list(map(int,input().split()))


def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def f(m):
    if m==1:
        return arr[0]
    return f(m-1)*arr[m-1]//gcd(f(m-1),arr[m-1])


print(f(n))