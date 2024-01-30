a, b, c = tuple(map(int,input().split()))

a, b, c = tuple(sorted([a, b, c]))

if b-a == 2 or c-b == 2:
    print(1)
else:
    print(2)