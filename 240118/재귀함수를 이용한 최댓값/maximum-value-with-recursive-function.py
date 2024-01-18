n = int(input())
arr = list(map(int,input().split()))

def f_arr(m):
    global arr
    if m==1:
        return arr[0]
    if arr[m-1] >= f_arr(m-1):
        return arr[m-1]
    else:
        return f_arr(m-1)


print(f_arr(n))