n,k = tuple(map(int,input().split()))
bombs = [
    int(input())
    for _ in range(n)
]


def cnt_exp(m):
    idx = [ i for i in range(n) if bombs[i]==m ]
    count = 0
    for j in range(len(idx)):
        if j+1 < len(idx) and idx[j+1] - idx[j] <= k or \
           j-1 >= 0 and idx[j] - idx[j-1] <= k:
            count += 1
    return count


bomb, num = cnt_exp(bombs[0]), bombs[0]
for i in range(1,n):
    if cnt_exp(bombs[i]) > bomb:
        bomb = cnt_exp(bombs[i])
        num = bombs[i]
    elif cnt_exp(bombs[i]) == bomb and bombs[i] > num:
        num = bombs[i]
print(num)