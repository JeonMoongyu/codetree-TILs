days_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
days_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def f(m,d):
    return sum(days_month[1:m])+d

m1,d1,m2,d2 = tuple(map(int,input().split()))
weekday = input()

k = 0
for i in range(7):
    if weekday == days_week[i]:
        k = i
        break
k = 7 if k == 0 else k

diff = f(m2,d2) - f(m1,d1)
print((diff-k)//7+1)