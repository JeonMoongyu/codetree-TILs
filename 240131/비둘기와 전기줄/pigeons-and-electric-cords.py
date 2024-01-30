n = int(input())
data = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


def f(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    return f(arr[:-1]) if arr[-1]==arr[-2] else f(arr[:-1])+1


ans = 0
for p in range(1,11):
    where = []
    for i,w in data:
        if p == i:
            where.append(w)
    ans += f(where)

print(ans)