def print_gcd(n,m):
    while m != 0:
        tmp = m
        m = n%m
        n = tmp
    print(n)

n,m = tuple(map(int,input().split()))
print_gcd(n,m)