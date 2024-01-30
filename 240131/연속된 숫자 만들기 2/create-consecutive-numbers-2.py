a, b, c = tuple(map(int,input().split()))

a, b, c = tuple(sorted([a, b, c]))

if b-a == 1 and c-b == 1:
    print(0)
elif b-a == 2 or c-b == 2:
    print(1)
else:
    print(2)