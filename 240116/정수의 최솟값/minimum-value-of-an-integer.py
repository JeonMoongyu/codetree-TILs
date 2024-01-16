def mini(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= c:
        return b
    else:
        return c

a,b,c = tuple(map(int,input().split()))
print(mini(a,b,c))