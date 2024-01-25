n = int(input())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


ans = n
for i in range(2,101,2):
    for j in range(2,101,2):
        cnt = [0] * 4
        for x,y in points:
            if x > i and y > j:
                cnt[0] += 1
            elif x < i and y > j:
                cnt[1] += 1
            elif x < i and y < j:
                cnt[2] += 1
            else:
                cnt[3] += 1
        ans = min(ans,max(cnt))

print(ans)