n,m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

def f(a,b):
    global arr
    sum_val = 0
    for i in range(a-1,b):
        sum_val += arr[i]
    return sum_val

for _ in range(m):
    a,b = tuple(map(int,input().split()))
    print(f(a,b))