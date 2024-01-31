n = int(input())
matches = [ tuple(map(int,input().split())) for _ in range(n) ]


def win_1(a,b): # 1<2<3<1
    return a==2 and b==1 or a==3 and b==2 or a==1 and b==3


def win_2(a,b): # 1<3<2<1
    return a==3 and b==1 or a==2 and b==3 or a==1 and b==2


ans1, ans2 = 0, 0
for a,b in matches:
    if win_1(a,b):
        ans1 += 1
    if win_2(a,b):
        ans2 += 1

print(max(ans1,ans2))