a, b = tuple(map(int,input().split()))
c, d = tuple(map(int,input().split()))
arr = [0] * 100

for i in range(100):
    if a<=i and i<b or c<=i and i<d:
        arr[i] = 1

print(sum(arr))