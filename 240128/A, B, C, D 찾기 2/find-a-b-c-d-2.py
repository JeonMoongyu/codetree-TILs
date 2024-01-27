import sys

arr = list(map(int,input().split()))


def f_list(a,b,c,d):
    return [a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]    


for a in range(1,41):
    for b in range(1,41):
        for c in range(1,41):
            for d in range(1,41):
                satisfied = True
                temp = [ elem for elem in arr ]
                for val in f_list(a,b,c,d):
                    if temp.count(val) > 0:
                        idx = temp.index(val)
                        temp = temp[:idx] + temp[idx+1:]
                    else:
                        satisfied = False
                if satisfied:
                    ans = sorted([a,b,c,d])
                    for elem in ans:
                        print(elem, end=" ")
                    sys.exit()