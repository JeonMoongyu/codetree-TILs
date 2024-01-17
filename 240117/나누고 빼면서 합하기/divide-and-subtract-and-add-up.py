n,m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

def f(m,arr):
    sum_val = 0
    while m >= 1:
        sum_val += arr[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return sum_val

print(f(m,arr))