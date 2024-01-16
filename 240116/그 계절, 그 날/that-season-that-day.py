def is_leap_year(y):
    if y%400==0:
        return True
    if y%100==0:
        return False
    if y%4==0:
        return True
    return False


def last_day(y,m):
    if m==2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    if m==4 or m==6 or m==9 or m==11:
        return 30
    return 31


def exist_day(y,m,d):
    return d <= last_day(y,m)


def season(m):
    if m <= 2:
        return "Winter"
    if m <= 5:
        return "Spring"
    if m <= 8:
        return "Summer"
    if m <= 11:
        return "Fall"
    return "Winter"


y,m,d = tuple(map(int,input().split()))
if exist_day(y,m,d):
    print(season(m))
else:
    print(-1)