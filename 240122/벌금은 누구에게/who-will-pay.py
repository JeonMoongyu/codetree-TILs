n,m,k = tuple(map(int,input().split()))
penalties = [ 0 for _ in range(n+1) ]
no_penalty = True
for _ in range(m):
    student = int(input())
    penalties[student] += 1
    if penalties[student] == k:
        no_penalty = False
        print(student)
if no_penalty:
    print(-1)