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
    for j in range(n):
        for j in range(ans,n):
            if sum(sorted_prices[:j]) <= budget:
                ans = j+1
print(ans)