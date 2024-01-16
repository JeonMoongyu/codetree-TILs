def is_369_number(n):
    satisfied = False
    for i in range(6):
        dig = (n//(10**i))%10
        if dig==3 or dig==6 or dig==9:
            satisfied = True
    return satisfied


def is_wanted_number(n):
    return n%3==0 or is_369_number(n)


a,b = tuple(map(int,input().split()))
cnt = 0
for i in range(a,b+1):
    if is_wanted_number(i):
        cnt += 1
print(cnt)