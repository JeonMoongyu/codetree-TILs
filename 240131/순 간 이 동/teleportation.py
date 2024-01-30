a, b, x, y = tuple(map(int,input().split()))

ans1 = abs(a-b)
ans2 = abs(a-x) + abs(y-b)
ans3 = abs(a-y) + abs(x-b)

print(min(ans1,ans2,ans3))