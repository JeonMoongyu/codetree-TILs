string = input()
leng = len(string)
ans = 0
for i in range(leng):
    for j in range(i+1,leng):
        if string[i] == '(' and string[j] == ')':
            ans += 1

print(ans)