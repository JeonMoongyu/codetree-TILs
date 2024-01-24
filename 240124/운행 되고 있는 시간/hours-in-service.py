n = int(input())
hours = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    cnt = [0 for _ in range(1000)]
    for j,(a,b) in enumerate(hours):
        if i == j:
            continue
        for k in range(a,b):
            cnt[k] += 1
    op_hour = 0
    for num in cnt[1:]:
        if num != 0:
            op_hour += 1
    ans = max(ans,op_hour)

print(ans)