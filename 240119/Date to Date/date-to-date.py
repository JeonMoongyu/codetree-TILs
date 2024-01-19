days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def f(m,d):
    return sum(days[1:m])+d

m1,d1,m2,d2 = tuple(map(int,input().split()))
print(f(m2,d2)-f(m1,d1)+1)