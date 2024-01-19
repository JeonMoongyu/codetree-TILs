days_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def f(m,d):
    return sum(days_month[1:m]) + d

m1,d1,m2,d2 = tuple(map(int,input().split()))
diff = f(m2,d2) - f(m1,d1)
print(days_week[diff%7])