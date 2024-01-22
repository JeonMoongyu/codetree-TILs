import sys

n = int(input())
people = [
    int(input())
    for _ in range(n)
]

min_dist = sys.maxsize 
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += ((n+j-i)%n) * people[j]
    min_dist = min(min_dist, sum_dist)
print(min_dist)