import sys

n,m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

ans = sys.maxsize
max_val = sum(arr)
while True:
    curr_sum = 0
    num_of_int = 1
    for elem in arr:
        if curr_sum + elem > max_val:
            curr_sum = elem
            num_of_int += 1
        else:
            curr_sum += elem
    if num_of_int > m:
        print(max_val+1)
        sys.exit()
    max_val -= 1