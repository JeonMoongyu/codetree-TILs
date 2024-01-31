a, b, c = tuple(map(int,input().split()))
a, b, c = tuple(sorted([a, b, c]))

print(max(c-b,b-a)-1)