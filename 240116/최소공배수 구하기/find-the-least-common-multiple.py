def print_lcm(n,m):
    n0, m0 = n, m
    while m != 0:
        temp = m
        m = n%m
        n = temp
    print(n0*m0//n)

n,m = tuple(map(int,input().split()))
print_lcm(n,m)