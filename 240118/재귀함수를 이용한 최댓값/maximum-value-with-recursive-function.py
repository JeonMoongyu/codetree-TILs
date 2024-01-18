def f(n,arr):
    if n==1:
        return arr[0]
    return arr[n-1] if f(n-1,arr)<arr[n-1] else f(n-1,arr)


n = int(input())
arr = list(map(int,input().split()))
print(f(n,arr))