k,n = tuple(map(int,input().split()))
data = [
    list(map(int,input().split()))
    for _ in range(k)
]

ans = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            continue
        satisfied = True
        for arr in data:
            rank_a = arr.index(a) # +1
            rank_b = arr.index(b) # +1
            if rank_a > rank_b:
                satisfied = False
        if satisfied:
            ans += 1

print(ans)