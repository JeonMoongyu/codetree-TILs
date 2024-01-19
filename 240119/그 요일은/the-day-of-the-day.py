days_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def f(m,d):
    return sum(days_month[1:m])+d

m1,d1,m2,d2 = tuple(map(int,input().split()))
weekday = input()
diff = f(m2,d2) - f(m1,d1)
print(diff//7+1)