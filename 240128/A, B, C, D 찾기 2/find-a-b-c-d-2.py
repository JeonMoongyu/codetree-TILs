import sys

arr = list(map(int,input().split()))
arr.sort()


def f_list(a,b,c,d):
    return [a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]    


for a in range(1,41):
    for b in range(1,41):
        for c in range(1,41):
            for d in range(1,41):
                if sorted(f_list(a,b,c,d)) == arr:
                    ans = sorted([a,b,c,d])
                    for elem in ans:
                        print(elem, end=" ")
                    sys.exit()