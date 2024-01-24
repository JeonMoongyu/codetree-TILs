n,k = tuple(map(int,input().split()))
arr = [0 for _ in range(10001)]

for _ in range(n):
    pos, alp = input().split()
    pos = int(pos)
    if alp == 'G':
        arr[pos] = 1
    else: # alp == 'H'
        arr[pos] = 2

ans = 0
for i in range(1,10000-k):
    sum_val = 0
    for j in range(i,i+k+1):
        sum_val += arr[j]
    ans = max(ans,sum_val)

print(ans)