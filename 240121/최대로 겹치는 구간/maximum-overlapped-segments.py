n = int(input())
segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
line = [0] * 200 # offset is 100
for a,b in segments:
    for i in range(a+100,b+100):
        line[i] += 1
print(max(line))