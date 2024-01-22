n = int(input())
cnt = []
form = int(input())
for _ in range(1,n):
    new = int(input())
    if new == form:
        cnt[-1] += 1
    else:
        cnt.append(1)
    form = new
print(max(cnt))