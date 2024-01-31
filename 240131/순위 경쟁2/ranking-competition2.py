n = int(input())

arr = []
curr_a, curr_b = 0, 0
for _ in range(n):
    c, s = input().split()
    s = int(s)
    if c == 'A':
        curr_a += s
    else:
        curr_b += s
    arr.append((curr_a,curr_b))

honors = [0] # 1:A, 0:A,B, -1:B
for a,b in arr:
    if a > b:
        honors.append(1)
    elif a == b:
        honors.append(0)
    else:
        honors.append(-1)

ans = 0
for i in range(n):
    if honors[i] != honors[i+1]:
        ans += 1

print(ans)