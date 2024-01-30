import sys

n, l = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

for h in range(100,-1,-1):
    cnt_1 = 0 # not less than h
    cnt_2 = 0 # equal to h-1
    for elem in arr:
        if elem >= h:
            cnt_1 += 1
        elif elem == h-1:
            cnt_2 += 1
    cnt_3 = min(cnt_2, l)
    if cnt_1 + cnt_3 >= h:
        print(h)
        sys.exit()