import sys

n = int(input())
pop = list(map(int,input().split()))
min_dist = sys.maxsize 
for house in range(1,n+1):
    sum_dist = 0
    for i in range(1,n+1):
        sum_dist += abs(i-house) * pop[i-1]
    min_dist = min(min_dist, sum_dist)
print(min_dist)