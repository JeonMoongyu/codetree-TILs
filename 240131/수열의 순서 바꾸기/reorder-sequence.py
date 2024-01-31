n = int(input())
arr = list(map(int,input().split()))

idx_1, idx_n = 0, 0
for i in range(n):
    if arr[i] == 1:
        idx_1 = i
    if arr[i] == n:
        idx_n = i

if arr == [ k for k in range(1,n+1) ]:
    print(0)
elif idx_n > idx_1:
    print(idx_n+1)
else:
    print(idx_1)