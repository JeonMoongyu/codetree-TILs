n,budget = tuple(map(int,input().split()))
prices = [
    int(input())
    for _ in range(n)
]

ans = 0
for i in range(n):
    prices[i] //= 2
    sorted_prices = sorted(prices)
    prices[i] *= 2

    sum_prices = 0
    cnt = 0
    for j in range(n):
        sum_prices += sorted_prices[j]
        if sum_prices > budget:
            break
        cnt += 1
    ans = max(ans,cnt)

print(ans)