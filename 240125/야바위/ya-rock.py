n = int(input())
data = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

max_score = 0
for i in range(1,4):
    curr = i
    score = 0
    for a,b,c in data:
        if curr == a:
            curr = b
        elif curr == b:
            curr = a
        if curr == c:
            score += 1
    max_score = max(max_score,score)

print(max_score)