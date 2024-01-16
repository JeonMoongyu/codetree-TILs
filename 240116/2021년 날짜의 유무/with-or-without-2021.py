def exist_2021(m,d):
    if m == 2:
        if 1 <= d and d <= 28:
            return True
    if m==4 or m==6 or m==9 or m==11:
        if 1 <= d and d <= 30:
            return True
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if 1 <= d and d <= 31:
            return True
    return False

m,d = tuple(map(int,input().split()))
if exist_2021(m,d):
    print("Yes")
else:
    print("No")