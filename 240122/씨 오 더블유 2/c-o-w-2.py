n = int(input())
string = input()
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if string[i]=='C' and string[j]=='O' and string[k]=='W':
                ans += 1
print(ans)