n = int(input())
arr = list(map(int, input().split()))


def f(m):
    if m==1:
        return arr[0]
    return f(m-1) if f(m-1)>=arr[m-1] else arr[m-1]


print(f(n))