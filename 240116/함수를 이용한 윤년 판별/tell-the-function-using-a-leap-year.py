def leap_year(y):
    if y%400==0:
        return True
    if y%100!=0:
        return True
    if y%4==0:
        return True
    return False

y = int(input())
if leap_year(y):
    print("true")
else:
    print("false")