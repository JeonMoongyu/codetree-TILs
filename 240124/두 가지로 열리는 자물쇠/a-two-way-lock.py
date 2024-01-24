n = int(input())
a1,b1,c1 = tuple(map(int,input().split()))
a2,b2,c2 = tuple(map(int,input().split()))


def dist(i,a):
    small, large = min(i,a), max(i,a)
    return min(large-small,small+n-large)


def is_close(i,j,k,a,b,c):
    return dist(i,a)<=2 and dist(j,b)<=2 and dist(k,c)<=2


ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if is_close(i,j,k,a1,b1,c1) or is_close(i,j,k,a2,b2,c2):
                ans += 1

print(ans)