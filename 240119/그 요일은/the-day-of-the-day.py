days_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
days_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def f(m,d):
    return sum(days_month[1:m])+d

m1,d1,m2,d2 = tuple(map(int,input().split()))
weekday = input()

for i in range(7):
    if weekday == days_week[i]:
        k = i

cnt = 0
diff = f(m2,d2) - f(m1,d1)
for n in range(1,diff+1):
    if n%7==k:
        cnt += 1

print(cnt)