def swap(n,m):
    return m,n


n,m = tuple(map(int,input().split()))
n,m = swap(n,m)
print(n,m)