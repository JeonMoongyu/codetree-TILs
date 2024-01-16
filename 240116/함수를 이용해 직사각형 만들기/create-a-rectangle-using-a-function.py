def print_1s(n,m):
    for _ in range(n):
        print("1"*m)

n,m = tuple(map(int,input().split()))
print_1s(n,m)